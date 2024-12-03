import tkinter as tk
from tkinter import ttk, messagebox
from itens.item import Item

def visualizar_itens(app):
    itens = Item.listar_todos_itens()
    
    if not itens:
        messagebox.showinfo("Itens", "Nenhum item cadastrado.")
        return
    
    quadro_itens = tk.Toplevel(app.root)
    quadro_itens.title("Itens Existentes")
    quadro_itens.geometry("500x400")

    ttk.Label(quadro_itens, text="Itens Cadastrados", font=("Arial", 14, "bold")).pack(pady=10)

    colunas = ("ID", "Nome", "Quantidade", "Serial Number", "Caixa ID")
    tree = ttk.Treeview(quadro_itens, columns=colunas, show="headings", height=10)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for item in itens:
        tree.insert("", "end", values=item)