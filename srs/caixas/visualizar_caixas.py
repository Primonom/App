import tkinter as tk
from tkinter import ttk, messagebox
from caixas.caixa import Caixa

def visualizar_caixas(app, setor_id=None):
    for widget in app.content_frame.winfo_children():
        widget.destroy()

    caixa = Caixa()
    caixas = caixa.listar_caixas_com_setores(setor_id)
    if not caixas:
        messagebox.showinfo("Caixas", "Nenhuma caixa cadastrada.")
        return

    ttk.Label(app.content_frame, text="Caixas", font=("Arial", 14, "bold")).pack(pady=10)

    frame = ttk.Frame(app.content_frame)
    frame.pack(pady=10)

    for i, caixa in enumerate(caixas):
        button = ttk.Button(frame, text=caixa[1], command=lambda c=caixa: visualizar_itens(app, c[0]))
        button.grid(row=i // 2, column=i % 2, padx=10, pady=10)