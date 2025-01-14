from tkinter import simpledialog, messagebox
from itens.item import Item

def adicionar_item(app):
    nome = simpledialog.askstring("Adicionar Item", "Nome do Item:")
    quantidade = simpledialog.askinteger("Adicionar Item", "Quantidade:")
    serial_number = simpledialog.askstring("Adicionar Item", "Serial Number:")
    caixa_id = simpledialog.askinteger("Adicionar Item", "ID da Caixa:")
    if nome and quantidade is not None and caixa_id is not None:
        item = Item()
        item.adicionar(nome, quantidade, serial_number, caixa_id)
        messagebox.showinfo("Sucesso", "Item adicionado com sucesso.")
        app.mostrar_setores()