from tkinter import simpledialog, messagebox
from setores.setor import Setor
from setores.visualizar_setores import visualizar_setores

def adicionar_setor(app):
    nome = simpledialog.askstring("Adicionar Setor", "Nome do setor:")
    if nome:
        setor = Setor()
        setor.adicionar_setor(nome)
        messagebox.showinfo("Sucesso", "Setor adicionado com sucesso!")
        visualizar_setores(app)
    else:
        messagebox.showerror("Erro", "O nome do setor é obrigatório.")