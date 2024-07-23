
import os
from tkinter.filedialog import askdirectory

def move():    
    print("MOVE FILES")
    origem = askdirectory()
    caminho = askdirectory()
    #origem = r"C:\Users\igor.gabriel\OneDrive - JSL SA\Área de Trabalho\CRLV_eu\PDFS"
    #caminho = r"C:\Users\igor.gabriel\OneDrive - JSL SA\Área de Trabalho\CRLV_eu\PDF2"
    lista_arquivos = os.listdir(origem)
    for arquivo in lista_arquivos:
        print(f"\nLENDO {arquivo}...\n")
        os.replace(f"{origem}/{arquivo}", f"{caminho}/{arquivo}")
        print(f"MOVIDO") 
        