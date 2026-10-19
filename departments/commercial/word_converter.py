import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ==================== CONFIGURAÇÃO ====================
PASTA_PARA_MONITORAR = r"C:\Users\terravista.JORNALOHOJE\Downloads\daily_requests"

# Caminho padrão do LibreOffice no Windows
CAMINHO_LIBREOFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"
# ======================================================

class WordOldConverterHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        # Inicializa o contador de arquivos processados
        self.contador = 1

    def on_created(self, event):
        if event.is_directory:
            return

        caminho_arquivo = os.path.abspath(event.src_path)
        nome_arquivo, extensao = os.path.splitext(caminho_arquivo)
        extensao = extensao.lower()

        # Ignora se for .doc (evita loops) ou se for arquivo temporário do Office
        if extensao == '.doc' or os.path.basename(caminho_arquivo).startswith('~$'):
            return

        # Monitora novos arquivos .docx
        if extensao == '.docx':
            print(f"✨ Novo arquivo .docx detectado: {os.path.basename(caminho_arquivo)}")
            
            # Pausa para garantir que a gravação/download do arquivo terminou
            time.sleep(2)
            self.converter_para_word_97_2003(caminho_arquivo)

    def converter_para_word_97_2003(self, caminho_origem):
        try:
            # 1. Executa a conversão para .doc na mesma pasta
            comando = [
                CAMINHO_LIBREOFFICE,
                "--headless",
                "--convert-to", "doc:MS Word 97",
                "--outdir", PASTA_PARA_MONITORAR,
                caminho_origem
            ]
            subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            
            # 2. Define os caminhos para renomear o arquivo gerado
            nome_base, _ = os.path.splitext(os.path.basename(caminho_origem))
            caminho_doc_gerado = os.path.join(PASTA_PARA_MONITORAR, f"{nome_base}.doc")
            
            nome_final_com_prefixo = f"M{self.contador} - {nome_base}.doc"
            caminho_doc_final = os.path.join(PASTA_PARA_MONITORAR, nome_final_com_prefixo)
            
            # Renomeia para o padrão M1, M2, etc.
            if os.path.exists(caminho_doc_gerado):
                os.rename(caminho_doc_gerado, caminho_doc_final)
                print(f"✅ Exportado e renomeado: {nome_final_com_prefixo}")
                
                # Incrementa o contador para o próximo arquivo
                self.contador += 1
            
            # 3. DELETA o arquivo .docx original
            if os.path.exists(caminho_origem):
                os.remove(caminho_origem)
                print(f"🗑️ Arquivo original deletado: {os.path.basename(caminho_origem)}\n")

        except Exception as e:
            print(f"❌ Erro no processamento do arquivo {os.path.basename(caminho_origem)}: {e}\n")

if __name__ == "__main__":
    if not os.path.exists(PASTA_PARA_MONITORAR):
        os.makedirs(PASTA_PARA_MONITORAR)

    if not os.path.exists(CAMINHO_LIBREOFFICE):
        print(f"⚠️ AVISO: Não encontrei o LibreOffice em '{CAMINHO_LIBREOFFICE}'.")
        print("Por favor, certifique-se de que o caminho está correto.")
    
    event_handler = WordOldConverterHandler()
    observer = Observer()
    observer.schedule(event_handler, path=PASTA_PARA_MONITORAR, recursive=False)
    
    print(f"🚀 Monitoramento iniciado na pasta: {PASTA_PARA_MONITORAR}")
    print("Modo: Word 97-2003 (.doc) com numeração automática M1, M2, M3...")
    print("Pressione Ctrl+C para encerrar.")
    
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Monitoramento encerrado.")
    observer.join()
