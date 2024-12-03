from tkinter import ttk, messagebox
import tkinter as tk
from caixas.caixa import Caixa

def visualizar_caixas(app):
    caixa = Caixa()
    caixas = caixa.listar_caixas_com_setores()
    if not caixas:
        messagebox.showinfo("Caixas", "Nenhuma caixa encontrada.")
        return

    quadro_caixas = tk.Toplevel(app.root)
    quadro_caixas.title("Caixas Existentes")
    quadro_caixas.geometry("500x400")

    ttk.Label(quadro_caixas, text="Caixas Criadas", font=("Arial", 14, "bold")).pack(pady=10)

    colunas = ("ID", "Nome", "Setor")
    tree = ttk.Treeview(quadro_caixas, columns=colunas, show="headings", height=10)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Setor", text="Setor")
    tree.column("ID", width=50, anchor="center")
    tree.column("Nome", width=150, anchor="center")
    tree.column("Setor", width=150, anchor="center")

    for caixa in caixas:
        tree.insert("", "end", values=(caixa[0], caixa[1], caixa[2]))

    ttk.Button(quadro_caixas, text="Fechar", command=quadro_caixas.destroy).pack(pady=10)