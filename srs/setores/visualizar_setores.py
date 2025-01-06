import tkinter as tk
from tkinter import ttk, messagebox
from setores.setor import Setor
from caixas.visualizar_caixas import visualizar_caixas

def visualizar_setores(app):
    for widget in app.content_frame.winfo_children():
        widget.destroy()

    setor = Setor()
    setores = setor.listar_setores()
    if not setores:
        messagebox.showinfo("Setores", "Nenhum setor cadastrado.")
        return

    ttk.Label(app.content_frame, text="Setores", font=("Arial", 16, "bold")).pack(pady=20)

    frame = ttk.Frame(app.content_frame)
    frame.pack(pady=10)

    for i, setor in enumerate(setores):
        button = ttk.Button(frame, text=setor[1], command=lambda s=setor: visualizar_caixas(app, s[0]))
        button.grid(row=i // 2, column=i % 2, padx=10, pady=10)

    app.history.append(visualizar_setores)  # Adicionar ao histórico