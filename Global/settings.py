import pyautogui as pg
import locale

# ------------------------------------------------------------------------- Caminhos de rede
CAMINHO_EDD = r'\\192.168.1.249\redacao\diagramacao\edicao'
CAMINHO_PAGFLIP = r'\\192.168.1.249\redacao\arte\00 Pagflip'
CAMINHO_WEB = r'\\192.168.1.249\redacao\web'
CAMINHO_FOTOS = r'\\192.168.1.249\fotos'
CAMINHO_MODELO_EDD = r'\\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições'
CAMINHO_MODELO_PAGFLIP = r'\\192.168.1.249\redacao\arte\00 Pagflip\00 - Modelo'
CAMINHO_MODELO_WEB = r'\\192.168.1.249\redacao\web\00 - Modelo'

# ------------------------------------------------------------------------- Barra de tarefas
quark = 1
opera = 2 # Navegador padrão
vscode = 3
explorer = 4

# ------------------------------------------------------------------------- Configurações gerais
screen_width, screen_height = pg.size()
center_x = screen_width / 2
center_y = screen_height / 2
locale.setlocale(locale.LC_TIME, "pt_BR.utf-8")

# ------------------------------------------------------------------------- Dados de edição
quantidade_repeticoes = 1
edicao_inicial = 8001
total_edicoes = quantidade_repeticoes * 6
print(".....")
print("⚙️  Settings loaded ✔️")
print(f".. Tamanho da tela: {pg.size()}")
print(f".. Edição inicial: {edicao_inicial}")
print(f".. Quantidade de repetições: {quantidade_repeticoes}")
print(f".. Criando modelo de {total_edicoes} edições")
print(".....")

# ------------------------------------------------------------------------- Posições de clique (em porcentagem da tela)
# arrumar uma forma de fazer isso de forma dinamica. Opções: 1 calcular sempre que rodar o script, 2 criar um arquivo de configuração para cada resolução de tela de acordo com o dispositivo
# if pg.size() == (1366, 768):
#     x_data = 49.48
#     y_data = 23.06
#     x_edicao_17 = 44.17
#     y_edicao_17 = 12.41
#     x_edicao_capa = 13.91
#     y_edicao_capa = 41.30
# elif pg.size() == (1920, 1080):
#     x_data = 68.45
#     y_data = 33.20
#     x_edicao_17 = 41.14
#     y_edicao_17 = 15.40
#     x_edicao_capa = 18.74
#     y_edicao_capa = 58.07

# ------------------------------------------------------------------------- Tempos de espera
TEMPO_ABERTURA = 4
TEMPO_FECHAMENTO = 3
TIMETOCLOSE = 6

# ------------------------------------------------------------------------- Ativar isso se quiser usar posições absolutas(essas funcionam na maquina do comercial)
# x_data = 49.48
# y_data = 23.06
# x_edicao_17 = 44.17
# y_edicao_17 = 12.41
# x_edicao_capa = 13.91
# y_edicao_capa = 41.30

x_data = 850
y_data = 259
x_edicao_17 = 560
y_edicao_17 = 121
x_edicao_capa = 346
y_edicao_capa = 448

if __name__ == "__main__":
    print(f"Centro da tela: ({center_x}, {center_y})")
    print(f"Edição inicial: {edicao_inicial}")
    pg.moveTo(x_data, y_data)
