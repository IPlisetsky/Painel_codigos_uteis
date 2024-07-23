from tkinter.filedialog import askdirectory
import shutil
import os


def copia():
    print("COPIA FILES")
    diretorio = askdirectory()
    if os.listdir(diretorio):
        print('--------PASTA NO SEU COMPUTADOR--------')
        # Obtém o nome da pasta do caminho completo
        nome_pasta = os.path.basename(diretorio)
        print(nome_pasta)   
    
    
    diretorio_sharepoint = askdirectory() # <------------ Mudar para a função do sharepoin
    if os.listdir(diretorio_sharepoint):
        # Obtém o nome da pasta do caminho completo
        print('--------PASTA NO SHAREPOIN--------')
        nome_pasta_sharepoin = os.path.basename(diretorio_sharepoint)
        print(nome_pasta_sharepoin)
    
    for arquivo in os.listdir(diretorio):
        caminho_arquivo_origem = os.path.join(diretorio, arquivo)
        caminho_arquivo_destino = os.path.join(diretorio_sharepoint, arquivo)
        shutil.copy(caminho_arquivo_origem, caminho_arquivo_destino)