import os
import pandas as pd
from tkinter.filedialog import askdirectory
import time
import tkinter as tk
from tkinter import ttk

def le_files():
    def atualizar_progresso(progresso):
        try:
            progresso_var.set(str(progresso))
            progress_bar["value"] = porcento
            print(porcento)
            if porcento == 100:
                porcentagem_str = f"{porcento:.2f}%" 
                porcentagem_label.config(text=porcentagem_str)
                arquivo_label.config(text="Planilha Gerada!")
            else:
                porcentagem_str = f"{porcento:.2f}%" 
                porcentagem_label.config(text=porcentagem_str)
                arquivo_label.config(text=arquivo)
            root.update()
        except Exception as e:
            print(f"aaaaaaaaa{e}")

    def simular_atualizacao():
        global porcento
        global arquivo
        lista = os.listdir(arq)
        total = len(lista)
        progresso = 0
        for arquivo in lista:
            if arquivo.endswith(".pdf"):
                nomes_arquivos.append(arquivo)
                print(nomes_arquivos)
                print(progresso)
                porcento = ((progresso+1) * 100) / total
                progresso +=1
                atualizar_progresso(progresso)
                time.sleep(0.1)
            else:
                pass
        try:
            diretorio = r"C:\Backup - OneDrive\novo dnv\Área de Trabalho\IGOR\Python\little help\RETORNOS"
            df = pd.DataFrame(nomes_arquivos, columns=["Nome do Arquivo"])
            df.to_excel(f"{diretorio}\ARQUIVOS_LIDOS.xlsx", index=False)
            print("Planilha gerada com sucesso!")
        except Exception as e:
            print(f"ERRO PLANILHAMENTO {e}")

    arq = askdirectory()
    print("LE FILES")
    nomes_arquivos = []
    root = tk.Tk()
    root.title("Exemplo de Barra de Progresso")
    root.geometry("250x100")

    progresso_var = tk.StringVar(value="0")

    progress_bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
    arquivo_label = tk.Label(root, text="")
    arquivo_label.pack(pady=3)
    porcentagem_label = tk.Label(root, text="")
    porcentagem_label.pack(pady=3)
    progress_bar.pack(pady=5)
    simular_atualizacao()

    root.mainloop()
