from tkinter import ttk, messagebox
import tkinter as tk
from setores.setor import Setor

def visualizar_setores(app):
    setor = Setor()
    setores = setor.listar_setores()
    if not setores:
        messagebox.showinfo("Setores", "Nenhum setor encontrado.")
        return
    
    quadro_setores = tk.Toplevel(app.root)
    quadro_setores.title("Setores Existentes")
    quadro_setores.geometry("400x300")

    ttk.Label(quadro_setores, text="Setores Cadastrados", font=("Arial", 14, "bold")).pack(pady=10)

    colunas = ("ID", "Nome")
    tree = ttk.Treeview(quadro_setores, columns=colunas, show="headings", height=10)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.column("ID", width=50, anchor="center")
    tree.column("Nome", width=150, anchor="center")

    for setor in setores:
        tree.insert("", "end", values=(setor[0], setor[1]))

    ttk.Button(quadro_setores, text="Fechar", command=quadro_setores.destroy).pack(pady=10)