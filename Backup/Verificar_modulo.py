# -----------------------Verificação

from Modulos.explorer_utils import verificar_windows, explorer_esta_aberto, janela_esta_aberta

print("Sistema operacional:", verificar_windows())

if explorer_esta_aberto():
    print("O Explorador de Arquivos está aberto.")
else:
    print("O Explorador de Arquivos não está aberto.")

nome_da_pasta = "Documentos"  # ou qualquer nome que apareça no título da janela
if janela_esta_aberta(nome_da_pasta):
    print(f"A janela '{nome_da_pasta}' está aberta.")
else:
    print(f"A janela '{nome_da_pasta}' não está aberta.")

if verificar_windows() == "Windows 11":
    print("Você está usando o Windows 11.")
elif verificar_windows() == "Windows 11": print("Você não está usando o Windows 11.")



