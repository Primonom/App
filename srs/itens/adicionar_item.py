import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from itens.item import Item

def adicionar_item(app):
    nome = simpledialog.askstring("Adicionar Item", "Nome do item:")
    quantidade = simpledialog.askinteger("Quantidade do Item", "Quantidade do item:")
    serial_number = simpledialog.askstring("Serial Number", "Número serial:")
    caixa_id = simpledialog.askinteger("Caixa", "ID da caixa:")
    
    if nome and quantidade and serial_number and caixa_id:
        item = Item(nome, quantidade, serial_number, caixa_id)
        item.salvar()
        mostrar_quadro_item(app, nome, quantidade, serial_number, caixa_id)
        messagebox.showinfo("Sucesso", "Item adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")

def mostrar_quadro_item(app, nome_item, quantidade_item, serial_number, caixa_id):
    quadro_item = tk.Toplevel(app.root)
    quadro_item.title("Novo Item Adicionado")
    quadro_item.geometry("300x150")

    ttk.Label(quadro_item, text="Item criado com sucesso!", font=("Arial", 14, "bold")).pack(pady=10)
    ttk.Label(quadro_item, text=f"Nome do Item: {nome_item}", font=("Arial", 12)).pack(pady=5)
    ttk.Label(quadro_item, text=f"Quantidade: {quantidade_item}", font=("Arial", 12)).pack(pady=5)
    ttk.Label(quadro_item, text=f"Serial Number: {serial_number}", font=("Arial", 12)).pack(pady=5)
    ttk.Label(quadro_item, text=f"Caixa ID: {caixa_id}", font=("Arial", 12)).pack(pady=5)