from tkinter import ttk, messagebox
import tkinter as tk
from itens.item import Item

def excluir_item(app):
    item = Item()
    itens = item.listar_todos_itens()
    if not itens:
        messagebox.showinfo("Itens", "Nenhum item encontrado.")
        return

    quadro_excluir_item = tk.Toplevel(app.root)
    quadro_excluir_item.title("Excluir Item")
    quadro_excluir_item.geometry("500x400")

    ttk.Label(quadro_excluir_item, text="Selecione um Item para Excluir", font=("Arial", 18, "bold")).pack(pady=10)

    colunas = ("ID", "Nome", "Quantidade", "Serial Number", "Caixa ID")
    tree = ttk.Treeview(quadro_excluir_item, columns=colunas, show="headings", height=10)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Quantidade", text="Quantidade")
    tree.heading("Serial Number", text="Serial Number")
    tree.heading("Caixa ID", text="Caixa ID")
    tree.column("ID", width=50, anchor="center")
    tree.column("Nome", width=150, anchor="center")
    tree.column("Quantidade", width=100, anchor="center")
    tree.column("Serial Number", width=100, anchor="center")
    tree.column("Caixa ID", width=50, anchor="center")

    for item_data in itens:
        tree.insert("", "end", values=(item_data[0], item_data[1], item_data[2], item_data[3], item_data[4]))

    def confirmar_exclusao():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Seleção", "Nenhum item selecionado.")
            return
        item_id = tree.item(selected_item[0])["values"][0]
        resposta = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir este item?")
        if resposta:
            item.excluir_item(item_id)
            messagebox.showinfo("Sucesso", "Item excluído com sucesso.")
            quadro_excluir_item.destroy()

    ttk.Button(quadro_excluir_item, text="Excluir", command=confirmar_exclusao).pack(pady=10)
    ttk.Button(quadro_excluir_item, text="Fechar", command=quadro_excluir_item.destroy).pack(pady=10)