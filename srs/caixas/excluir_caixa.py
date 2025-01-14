from tkinter import ttk, messagebox
import tkinter as tk
from caixas.caixa import Caixa

def excluir_caixa(app):
    caixa = Caixa()
    caixas = caixa.listar_todos()
    if not caixas:
        messagebox.showinfo("Caixas", "Nenhuma caixa encontrada.")
        return

    quadro_excluir_caixa = tk.Toplevel(app.root)
    quadro_excluir_caixa.title("Excluir Caixa")
    quadro_excluir_caixa.geometry("500x400")

    ttk.Label(quadro_excluir_caixa, text="Selecione uma Caixa para Excluir", font=("Arial", 18, "bold")).pack(pady=10)

    colunas = ("ID", "Nome", "Setor ID")
    tree = ttk.Treeview(quadro_excluir_caixa, columns=colunas, show="headings", height=10)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Setor ID", text="Setor ID")
    tree.column("ID", width=50, anchor="center")
    tree.column("Nome", width=150, anchor="center")
    tree.column("Setor ID", width=100, anchor="center")

    for caixa_data in caixas:
        tree.insert("", "end", values=(caixa_data[0], caixa_data[1], caixa_data[2]))

    def confirmar_exclusao():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Seleção", "Nenhuma caixa selecionada.")
            return
        caixa_id = tree.item(selected_item[0])["values"][0]
        resposta = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir esta caixa?")
        if resposta:
            caixa.excluir(caixa_id)
            messagebox.showinfo("Sucesso", "Caixa excluída com sucesso.")
            quadro_excluir_caixa.destroy()

    ttk.Button(quadro_excluir_caixa, text="Excluir", command=confirmar_exclusao).pack(pady=10)
    ttk.Button(quadro_excluir_caixa, text="Fechar", command=quadro_excluir_caixa.destroy).pack(pady=10)