from PIL import Image, ImageTk
import tkinter as tk
from tkinter import PhotoImage, Label, Frame, Button, ttk
import os
from le_arquivos import le_files
from move_files import move
from muda_nome import muda
from copy_files import copia


def tela_ajudinha():
    try:
        root = tk.Tk()
        root.title("Little Help")
        root.geometry("200x250")
        root.configure(bg="white")

        content = ttk.Frame(root)

        img = Image.open(r'Images\a.jpg')
        img_ajust = img.resize((100, 100), Image.LANCZOS)
        img_ajust = ImageTk.PhotoImage(image=img_ajust)

        label = Label(root, image=img_ajust)
        label.pack()

        frame = Frame(root, background="white")
        frame.pack(pady=10)
        
        botao1 = Button(frame, text="LER/PLANILHAS", command=le_files)
        botao2 = Button(frame, text="MOVE", command=move)
        botao3 = Button(frame, text="COPIA", command=copia)
        botao4 = Button(frame, text="MUDA NOME", command=muda)

        botao1.grid(row=0, columnspan=4, padx=10, pady=5)
        botao2.grid(row=1, column=0, padx=3, pady=5)
        botao3.grid(row=1, column=1, padx=3, pady=5)
        botao4.grid(row=2, columnspan=4, padx=10, pady=5)

        root.mainloop()
    except Exception as e:
        print(f"AJUDINHA {e}")
tela_ajudinha()