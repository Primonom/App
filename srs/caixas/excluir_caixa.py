from tkinter import ttk, messagebox, simpledialog
import tkinter as tk
from caixas.caixa import Caixa

def excluir_caixa(app):
    caixa = Caixa()
    caixas = caixa.listar_caixas_com_setores()
    if not caixas:
        messagebox.showinfo("Caixas", "Nenhuma caixa encontrada.")
        return

    quadro_excluir_caixa = tk.Toplevel(app.root)
    quadro_excluir_caixa.title("Excluir Caixa")
    quadro_excluir_caixa.geometry("500x400")

    ttk.Label(quadro_excluir_caixa, text="Selecione uma Caixa para Excluir", font=("Arial", 18, "bold")).pack(pady=10)

    colunas = ("ID", "Nome", "Setor")
    tree = ttk.Treeview(quadro_excluir_caixa, columns=colunas, show="headings", height=10)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Setor", text="Setor")
    tree.column("ID", width=50, anchor="center")
    tree.column("Nome", width=150, anchor="center")
    tree.column("Setor", width=150, anchor="center")

    for caixa in caixas:
        tree.insert("", "end", values=(caixa[0], caixa[1], caixa[2]))

    def confirmar_exclusao():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Seleção", "Nenhuma caixa selecionada.")
            return
        caixa_id = tree.item(selected_item[0])["values"][0]
        resposta = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir esta caixa?")
        if resposta:
            caixa.excluir_caixa(caixa_id)
            messagebox.showinfo("Sucesso", "Caixa excluída com sucesso.")
            quadro_excluir_caixa.destroy()

    ttk.Button(quadro_excluir_caixa, text="Excluir", command=confirmar_exclusao).pack(pady=10)
    ttk.Button(quadro_excluir_caixa, text="Fechar", command=quadro_excluir_caixa.destroy).pack(pady=10)