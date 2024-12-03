from tkinter import simpledialog, messagebox, ttk
import tkinter as tk
from setores.setor import Setor

def adicionar_setor(app):
    nome = simpledialog.askstring("Adicionar Setor", "Nome do setor:")
    if nome:
        setor = Setor()
        setor.adicionar_setor(nome)
        app.log_acoes.registrar_acao(app.usuario_atual, "adicionar setor", f"Setor '{nome}' adicionado")
        mostrar_quadro_setor(app, nome)

def mostrar_quadro_setor(app, nome_setor):
    quadro_setor = tk.Toplevel(app.root)
    quadro_setor.title("Novo Setor Adicionado")
    quadro_setor.geometry("300x150")

    ttk.Label(quadro_setor, text="Setor criado com sucesso!", font=("Arial", 14, "bold")).pack(pady=10)
    ttk.Label(quadro_setor, text=f"Nome do Setor: {nome_setor}", font=("Arial", 12)).pack(pady=5)

    ttk.Button(quadro_setor, text="Fechar", command=quadro_setor.destroy).pack(pady=10)