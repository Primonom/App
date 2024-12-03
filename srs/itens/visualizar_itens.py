from tkinter import ttk, messagebox
import tkinter as tk
from itens.item import Item

def visualizar_itens(app):
    itens = Item.listar_todos_itens()
    
    if not itens:
        messagebox.showinfo("Itens", "Nenhum item encontrado.")
        return
    
    quadro_itens = tk.Toplevel(app.root)
    quadro_itens.title("Itens Existentes")
    quadro_itens.geometry("500x400")

    ttk.Label(quadro_itens, text="Itens Cadastrados", font=("Arial", 14, "bold")).pack(pady=10)

    colunas = ("ID", "Nome", "Quantidade", "Serial Number", "Caixa ID")
    tree = ttk.Treeview(quadro_itens, columns=colunas, show="headings", height=10)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Quantidade", text="Quantidade")
    tree.heading("Serial Number", text="Serial Number")
    tree.heading("Caixa ID", text="Caixa ID")

    tree.column("ID", width=50, anchor="center")
    tree.column("Nome", width=150, anchor="center")
    tree.column("Quantidade", width=100, anchor="center")
    tree.column("Serial Number", width=150, anchor="center")
    tree.column("Caixa ID", width=100, anchor="center")

    for item in itens:
        tree.insert("", "end", values=(item[0], item[1], item[2], item[3], item[4]))

    ttk.Button(quadro_itens, text="Fechar", command=quadro_itens.destroy).pack(pady=10)