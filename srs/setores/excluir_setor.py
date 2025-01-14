from tkinter import ttk, messagebox
import tkinter as tk
from setores.setor import Setor

def excluir_setor(app):
    setor = Setor()
    setores = setor.listar_setores()
    if not setores:
        messagebox.showinfo("Setores", "Nenhum setor encontrado.")
        return

    quadro_excluir_setor = tk.Toplevel(app.root)
    quadro_excluir_setor.title("Excluir Setor")
    quadro_excluir_setor.geometry("500x400")

    ttk.Label(quadro_excluir_setor, text="Selecione um Setor para Excluir", font=("Arial", 18, "bold")).pack(pady=10)

    colunas = ("ID", "Nome")
    tree = ttk.Treeview(quadro_excluir_setor, columns=colunas, show="headings", height=10)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.column("ID", width=50, anchor="center")
    tree.column("Nome", width=150, anchor="center")

    for setor_data in setores:
        tree.insert("", "end", values=(setor_data[0], setor_data[1]))

    def confirmar_exclusao():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Seleção", "Nenhum setor selecionado.")
            return
        setor_id = tree.item(selected_item[0])["values"][0]
        resposta = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir este setor?")
        if resposta:
            setor.excluir_setor(setor_id)
            messagebox.showinfo("Sucesso", "Setor excluído com sucesso.")
            quadro_excluir_setor.destroy()

    ttk.Button(quadro_excluir_setor, text="Excluir", command=confirmar_exclusao).pack(pady=10)
    ttk.Button(quadro_excluir_setor, text="Fechar", command=quadro_excluir_setor.destroy).pack(pady=10)