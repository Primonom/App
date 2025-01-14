from tkinter import simpledialog, messagebox
from setores.setor import Setor

def adicionar_setor(app):
    nome = simpledialog.askstring("Adicionar Setor", "Nome do Setor:")
    if nome:
        setor = Setor()
        setor.adicionar(nome)
        messagebox.showinfo("Sucesso", "Setor adicionado com sucesso.")
        app.mostrar_setores()