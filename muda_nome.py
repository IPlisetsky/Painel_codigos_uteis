import os
from tkinter.filedialog import askdirectory
import tkinter as tk
from tkinter import Button, Frame



def muda():
    print("MUDA NOME")
    pasta = askdirectory()

    def user():
        tela = tk.Tk()
        tela.title("TEXTO A SER EXCLUIDO")
        label = tk.Label(tela, text="Insira o texto:")
        label.pack()
        entry = tk.Entry(tela)
        entry.pack()
        def get_input():
            global value
            value = entry.get()
            print(f"Valor: {value}")
            tela.destroy()

            ctx = tk.Tk()
            ctx.title("CERTEZA?")
            label = tk.Label(ctx, text=f"Quer seguir com a alteração: {value} ?")
            label.pack()
            frame = Frame(ctx, background="white")
            frame.pack(pady=10)
            def nao():
                print("\nNÃO\n")
                ctx.destroy()
                user()
            def sim():
                print("\nSIM\n")
                ctx.destroy()
                contador = 1
                excluidos = 0
                alterados = 0
                for arquivo in os.listdir(pasta):
                    try:    
                        # RENOMEIA
                        if arquivo.endswith(".pdf"):
                            nome_atual = os.path.join(pasta, arquivo)
                            nome_novo = arquivo.replace(value, "")
                            nome_novo = os.path.join(pasta, nome_novo)
                            os.rename(nome_atual, nome_novo)
                            print(f"Arquivo renomeado: {arquivo} -> {nome_novo}")
                            alterados += 1
                            contador += 1 
                        else:
                            pass
                        
                        #REMOVE
                        if "(1)" in arquivo or "(2)" in arquivo or "(3)" in arquivo or "(4)" in arquivo or "(5)" in arquivo or "(6)" in arquivo or "(7)" in arquivo:
                            arquivo_remove = os.remove(nome_novo)
                            print(f"removeu arquivo: {arquivo}")
                            excluidos +=1
                        else:
                            pass
                    except:
                        print(f"ERRO NO ARQUIVO: {arquivo}")
                        pass
                print(f"\n{excluidos} ARQUIVOS EXCLUÍDOS\n")
                print(f"\n{alterados} ARQUIVOS ALTERADOS\n")

            botao1 = Button(frame, text="SIM", command=sim)
            botao2 = Button(frame, text="NÃO", command=nao)
            botao1.grid(row = 0, column=0)
            botao2.grid(row = 0, column=1)
            ctx.mainloop()
            pass

        button = tk.Button(tela, text="Enter", command=get_input)
        button.pack()
        tela.mainloop()


    user()

    
    

    
