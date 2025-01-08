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
    quadro_itens.geometry("600x500")

    ttk.Label(quadro_itens, text="Itens Cadastrados", font=("Arial", 14, "bold")).pack(pady=10)

    search_frame = ttk.Frame(quadro_itens)
    search_frame.pack(pady=10)

    search_label = ttk.Label(search_frame, text="Buscar:")
    search_label.pack(side="left", padx=5)

    search_entry = ttk.Entry(search_frame)
    search_entry.pack(side="left", padx=5)

    def buscar_itens():
        query = search_entry.get()
        resultados = [item for item in itens if query.lower() in item[1].lower()]
        atualizar_treeview(resultados)

    search_button = ttk.Button(search_frame, text="Buscar", command=buscar_itens)
    search_button.pack(side="left", padx=5)

    colunas = ("ID", "Nome", "Quantidade", "Serial Number", "Caixa ID")
    tree = ttk.Treeview(quadro_itens, columns=colunas, show="headings", height=15)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    def atualizar_treeview(itens):
        for row in tree.get_children():
            tree.delete(row)
        for item in itens:
            tree.insert("", "end", values=item)

    atualizar_treeview(itens)