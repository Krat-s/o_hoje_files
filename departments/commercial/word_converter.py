import os
import re
import json
import time
import queue
import shutil
import tempfile
import threading
import subprocess
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ==================== CONFIGURAÇÃO ====================
# Pasta onde os arquivos chegam (os originais FICAM aqui, intocados)
PASTA_PARA_MONITORAR = r"C:\Users\terravista.JORNALOHOJE\Downloads\0 - word_para_converter"

# Pasta onde os convertidos (M1 - ..., M2 - ...) são gravados.
# Precisa ser DIFERENTE da pasta monitorada.
PASTA_SAIDA = r"C:\Users\terravista.JORNALOHOJE\Downloads"

# Motor de conversão:
#   "libreoffice" -> usa o LibreOffice (não precisa de Word)
#   "word"        -> usa o Microsoft Word instalado (precisa: pip install pywin32)
MOTOR = "word"

CAMINHO_LIBREOFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"

# >>> FORMATOS DE ENTRADA ACEITOS <<<
# Para aceitar mais um formato, adicione a extensão aqui (minúscula, com ponto).
# Ex.: ".txt", ".html". Para parar de aceitar um, remova da lista.
EXTENSOES_ENTRADA = {
    ".docx", ".docm", ".dotx",   # Word moderno
    ".doc", ".dot",              # Word 97-2003
    ".rtf",                      # Rich Text
    ".odt",                      # LibreOffice/OpenOffice
    ".wpd", ".wps",              # WordPerfect / MS Works
}

# Formato de saída:
#   "doc97" -> Word 97-2003 (.doc)                  [libreoffice e word]
#   "doc95" -> Word 95 (.doc)                       [só libreoffice]
#   "rtf"   -> Rich Text Format (.rtf)              [libreoffice e word]
FORMATO = "doc97"

# True  = se o arquivo já chegar como .doc, só copia (com o prefixo M) sem
#         reconverter. Só vale quando FORMATO = "doc97".
# False = converte tudo, inclusive .doc.
REPASSAR_DOC_SEM_CONVERTER = False
# ======================================================

FORMATOS_LIBREOFFICE = {
    "doc97": ("doc", "doc:MS Word 97"),
    "doc95": ("doc", "doc:MS Word 95"),
    "rtf":   ("rtf", "rtf:Rich Text Format"),
}
FORMATOS_WORD = {
    "doc97": ("doc", 0),   # wdFormatDocument97
    "rtf":   ("rtf", 6),   # wdFormatRTF
}

if MOTOR not in ("libreoffice", "word"):
    raise SystemExit(f"MOTOR inválido: '{MOTOR}'. Use 'libreoffice' ou 'word'.")

_TABELA = FORMATOS_LIBREOFFICE if MOTOR == "libreoffice" else FORMATOS_WORD
if FORMATO not in _TABELA:
    raise SystemExit(
        f"FORMATO '{FORMATO}' não é suportado pelo motor '{MOTOR}'. "
        f"Opções: {', '.join(_TABELA)}"
    )
EXT_SAIDA, PARAMETRO_FORMATO = _TABELA[FORMATO]

# Registro dos arquivos já processados (fica ao lado do script, não na pasta do Quark)
ARQUIVO_REGISTRO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "registro_processados.json")

fila = queue.Queue()
em_processamento = set()
lock = threading.RLock()


# ---------------------- registro anti-reprocessamento ----------------------
def _chave(caminho):
    return os.path.normcase(os.path.abspath(caminho))


def _assinatura(caminho):
    st = os.stat(caminho)
    return [st.st_size, int(st.st_mtime)]


def _carregar_registro():
    try:
        with open(ARQUIVO_REGISTRO, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


registro = _carregar_registro()


def ja_processado(caminho):
    try:
        assinatura = _assinatura(caminho)
    except OSError:
        return False
    with lock:
        return registro.get(_chave(caminho)) == assinatura


def registrar(caminho, assinatura):
    with lock:
        registro[_chave(caminho)] = assinatura
        temporario = ARQUIVO_REGISTRO + ".tmp"
        with open(temporario, "w", encoding="utf-8") as f:
            json.dump(registro, f, ensure_ascii=False, indent=1)
        os.replace(temporario, ARQUIVO_REGISTRO)


# ---------------------- utilidades ----------------------
def aguardar_arquivo_estavel(caminho, tentativas=60):
    """Espera o tamanho parar de mudar e o arquivo poder ser aberto."""
    ultimo_tamanho = -1
    for _ in range(tentativas):
        try:
            tamanho = os.path.getsize(caminho)
            if tamanho > 0 and tamanho == ultimo_tamanho:
                with open(caminho, "rb"):
                    pass
                return True
            ultimo_tamanho = tamanho
        except OSError:
            pass
        time.sleep(1)
    return False


def proximo_numero():
    """Próximo número F disponível, lendo a pasta de SAÍDA."""
    maior = 0
    for nome in os.listdir(PASTA_SAIDA):
        m = re.match(r"^M(\d+) - ", nome)
        if m:
            maior = max(maior, int(m.group(1)))
    return maior + 1


# ---------------------- motores ----------------------
def converter_com_libreoffice(origem, pasta_temp):
    perfil = Path(pasta_temp, "perfil_lo").as_uri()  # perfil isolado: evita conflito com LO aberto
    comando = [
        CAMINHO_LIBREOFFICE,
        f"-env:UserInstallation={perfil}",
        "--headless",
        "--convert-to", PARAMETRO_FORMATO,
        "--outdir", pasta_temp,
        os.path.abspath(origem),
    ]
    r = subprocess.run(comando, capture_output=True, text=True, timeout=180)

    base = os.path.splitext(os.path.basename(origem))[0]
    gerado = os.path.join(pasta_temp, f"{base}.{EXT_SAIDA}")
    if not os.path.exists(gerado) or os.path.getsize(gerado) == 0:
        raise RuntimeError(
            f"LibreOffice não gerou o arquivo (código {r.returncode}). "
            f"stdout: {r.stdout.strip()} | stderr: {r.stderr.strip()}"
        )
    return gerado


def converter_com_word(origem, pasta_temp):
    import win32com.client

    base = os.path.splitext(os.path.basename(origem))[0]
    destino = os.path.join(pasta_temp, f"{base}.{EXT_SAIDA}")

    word = win32com.client.DispatchEx("Word.Application")  # instância própria
    word.Visible = False
    word.DisplayAlerts = 0
    word.AutomationSecurity = 3  # desativa macros (ex.: .docm)
    try:
        doc = word.Documents.Open(
            FileName=os.path.abspath(origem),
            ConfirmConversions=False,
            ReadOnly=True,
            AddToRecentFiles=False,
            NoEncodingDialog=True,
        )
        try:
            doc.SaveAs2(FileName=destino, FileFormat=PARAMETRO_FORMATO)
        finally:
            doc.Close(False)
    finally:
        word.Quit()

    if not os.path.exists(destino) or os.path.getsize(destino) == 0:
        raise RuntimeError("Word não gerou o arquivo de saída")
    return destino


# ---------------------- processamento ----------------------
def processar(caminho_origem):
    nome_base, ext = os.path.splitext(os.path.basename(caminho_origem))
    ext = ext.lower()

    if not aguardar_arquivo_estavel(caminho_origem):
        raise RuntimeError("arquivo não ficou disponível (ainda em gravação ou bloqueado)")

    # Evento duplicado (ex.: created + moved do mesmo arquivo): ignora em silêncio
    if ja_processado(caminho_origem):
        return

    assinatura = _assinatura(caminho_origem)
    repassar = REPASSAR_DOC_SEM_CONVERTER and FORMATO == "doc97" and ext == ".doc"

    with tempfile.TemporaryDirectory() as tmp:
        if repassar:
            fonte = caminho_origem
        elif MOTOR == "word":
            fonte = converter_com_word(caminho_origem, tmp)
        else:
            fonte = converter_com_libreoffice(caminho_origem, tmp)

        numero = proximo_numero()
        nome_final = f"M{numero} - {nome_base}.{EXT_SAIDA}"
        destino_final = os.path.join(PASTA_SAIDA, nome_final)
        destino_parcial = destino_final + ".part"

        # COPIAR (não mover): o arquivo herda as permissões da pasta de destino
        shutil.copyfile(fonte, destino_parcial)
        os.replace(destino_parcial, destino_final)

    registrar(caminho_origem, assinatura)
    acao = "Copiado (já era .doc)" if repassar else "Convertido"
    print(f"✅ {acao}: {os.path.basename(caminho_origem)}  ->  {nome_final}\n")


def worker():
    if MOTOR == "word":
        import pythoncom
        pythoncom.CoInitialize()

    while True:
        caminho = fila.get()
        try:
            processar(caminho)
        except Exception as e:
            print(f"❌ Erro em {os.path.basename(caminho)}: {e}\n")
        finally:
            with lock:
                em_processamento.discard(caminho)
            fila.task_done()


# ---------------------- watchdog ----------------------
class Handler(FileSystemEventHandler):
    def _enfileirar(self, caminho):
        caminho = os.path.abspath(caminho)
        nome = os.path.basename(caminho)
        ext = os.path.splitext(nome)[1].lower()

        # Ignora temporários/locks do Office e do LibreOffice e extensões não aceitas
        if nome.startswith("~$") or nome.startswith(".~lock."):
            return
        if ext not in EXTENSOES_ENTRADA:
            return
        if os.path.normcase(os.path.dirname(caminho)) != os.path.normcase(os.path.abspath(PASTA_PARA_MONITORAR)):
            return
        if ja_processado(caminho):
            return

        with lock:
            if caminho in em_processamento:
                return
            em_processamento.add(caminho)

        print(f"✨ Novo arquivo detectado: {nome}")
        fila.put(caminho)

    def on_created(self, event):
        if not event.is_directory:
            self._enfileirar(event.src_path)

    def on_moved(self, event):
        # Downloads de navegador (.crdownload -> .docx) chegam aqui
        if not event.is_directory:
            self._enfileirar(event.dest_path)

def testar_monitoramento():
    print("🚀 Testando monitoramento da pasta de conversão de Word...")

def _watch_folder_converter():
        print("🚀 Iniciando monitoramento da pasta de conversão de Word...")
        pasta_in = os.path.normcase(os.path.abspath(PASTA_PARA_MONITORAR))
        pasta_out = os.path.normcase(os.path.abspath(PASTA_SAIDA))
        if pasta_in == pasta_out:
            raise SystemExit(
                "ERRO: PASTA_SAIDA não pode ser igual a PASTA_PARA_MONITORAR "
                "(isso causaria um loop infinito)."
            )

        os.makedirs(PASTA_PARA_MONITORAR, exist_ok=True)
        os.makedirs(PASTA_SAIDA, exist_ok=True)

        if MOTOR == "libreoffice" and not os.path.exists(CAMINHO_LIBREOFFICE):
            print(f"⚠️ LibreOffice não encontrado em '{CAMINHO_LIBREOFFICE}'.")

        threading.Thread(target=worker, daemon=True).start()

        # Arquivos que já estavam na pasta ao iniciar (os já processados são pulados)
        for nome in os.listdir(PASTA_PARA_MONITORAR):
            Handler()._enfileirar(os.path.join(PASTA_PARA_MONITORAR, nome))

        observer = Observer()
        observer.schedule(Handler(), path=PASTA_PARA_MONITORAR, recursive=False)
        observer.start()

        print(f"🚀 Monitorando: {PASTA_PARA_MONITORAR}")
        print(f"📂 Saída:       {PASTA_SAIDA}")
        print(f"Motor: {MOTOR} | Formato de saída: {FORMATO} (.{EXT_SAIDA})")
        print(f"Entradas aceitas: {', '.join(sorted(EXTENSOES_ENTRADA))}")
        print("Pressione Ctrl+C para encerrar.")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            print("\n🛑 Monitoramento encerrado.")
        observer.join()


if __name__ == "__main__":
    _watch_folder_converter()