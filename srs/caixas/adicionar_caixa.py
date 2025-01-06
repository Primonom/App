from tkinter import simpledialog, messagebox
from caixas.caixa import Caixa
from caixas.visualizar_caixas import visualizar_caixas

def adicionar_caixa(app):
    nome = simpledialog.askstring("Adicionar Caixa", "Nome da caixa:")
    setor_id = simpledialog.askinteger("Setor", "ID do setor:")
    if nome and setor_id:
        caixa = Caixa()
        caixa.adicionar_caixa(nome, setor_id)
        messagebox.showinfo("Sucesso", "Caixa adicionada com sucesso!")
        visualizar_caixas(app, setor_id)
    else:
        messagebox.showerror("Erro", "O nome da caixa e o ID do setor são obrigatórios.")