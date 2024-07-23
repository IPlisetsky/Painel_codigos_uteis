import tkinter as tk

def mostrar_selecao(opcao):
  print(f"Você selecionou: {opcao}")

root = tk.Tk()
root.title("Menu Suspenso")

var = tk.StringVar()
var.set("Opção 1")

options = ["Opção 1", "Opção 2", "Opção 3"]

dropdown = tk.OptionMenu(root, var, *options, command=mostrar_selecao)
dropdown.pack()

root.mainloop()