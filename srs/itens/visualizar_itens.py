import tkinter as tk
from tkinter import ttk, messagebox
from itens.item import Item

def visualizar_itens(app, caixa_id=None):
    for widget in app.content_frame.winfo_children():
        widget.destroy()

    item = Item()
    itens = item.listar_itens(caixa_id)
    
    if not itens:
        messagebox.showinfo("Itens", "Nenhum item cadastrado.")
        return
    
    ttk.Label(app.content_frame, text="Itens", font=("Arial", 16, "bold")).pack(pady=20)

    colunas = ("ID", "Nome", "Quantidade", "Serial Number", "Caixa ID")
    tree = ttk.Treeview(app.content_frame, columns=colunas, show="headings", height=10)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for item in itens:
        tree.insert("", "end", values=item)

    app.history.append(lambda: visualizar_itens(app, caixa_id))  # Adicionar ao histórico