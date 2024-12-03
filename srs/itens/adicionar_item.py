from tkinter import simpledialog, messagebox, ttk
import tkinter as tk
from itens.item import Item

def adicionar_item(app):
    nome = simpledialog.askstring("Adicionar Item", "Nome do item:")
    quantidade = simpledialog.askstring("Tipo do Item", "Tipo do item:")
    serial_number = simpledialog.askstring("Serial Number", "Número serial:")
    caixa_id = simpledialog.askinteger("Caixa", "ID da caixa:")
    
    if nome and quantidade and serial_number and caixa_id:
        item = Item(nome, quantidade, serial_number, caixa_id)
        item.salvar()
        app.log_acoes.registrar_acao(app.usuario_atual, "adicionar item", f"Item '{nome}' adicionado à caixa {caixa_id}")
        mostrar_quadro_item(app, nome, quantidade, serial_number, caixa_id)

def mostrar_quadro_item(app, nome_item, quantidade_item, serial_number, caixa_id):
    quadro_item = tk.Toplevel(app.root)
    quadro_item.title("Novo Item Adicionado")
    quadro_item.geometry("300x200")

    ttk.Label(quadro_item, text="Item criado com sucesso!", font=("Arial", 14, "bold")).pack(pady=10)
    ttk.Label(quadro_item, text=f"Nome: {nome_item}", font=("Arial", 12)).pack(pady=5)
    ttk.Label(quadro_item, text=f"Tipo: {quantidade_item}", font=("Arial", 12)).pack(pady=5)
    ttk.Label(quadro_item, text=f"Serial: {serial_number}", font=("Arial", 12)).pack(pady=5)
    ttk.Label(quadro_item, text=f"Caixa ID: {caixa_id}", font=("Arial", 12)).pack(pady=5)

    ttk.Button(quadro_item, text="Fechar", command=quadro_item.destroy).pack(pady=10)