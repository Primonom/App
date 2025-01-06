from tkinter import simpledialog, messagebox
from itens.item import Item
from itens.visualizar_itens import visualizar_itens

def adicionar_item(app):
    nome = simpledialog.askstring("Adicionar Item", "Nome do item:")
    quantidade = simpledialog.askinteger("Quantidade do Item", "Quantidade do item:")
    serial_number = simpledialog.askstring("Serial Number", "Número serial:")
    caixa_id = simpledialog.askinteger("Caixa", "ID da caixa:")
    
    if nome and quantidade and serial_number:
        item = Item()
        item.adicionar_item(nome, quantidade, serial_number, caixa_id)
        messagebox.showinfo("Sucesso", "Item adicionado com sucesso!")
        visualizar_itens(app, caixa_id)
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")