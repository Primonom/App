from tkinter import simpledialog, messagebox
from ttkbootstrap import ttk
from itens.item import Item
from caixas.caixa import Caixa

def adicionar_item(app):
    # Criar um novo frame para adicionar item
    app.adicionar_item_frame = ttk.Frame(app.root)
    app.adicionar_item_frame.grid(row=0, column=0, sticky="nsew")

    # Adicionar widgets ao frame de adicionar item
    ttk.Label(app.adicionar_item_frame, text="Adicionar Item", font=("Arial", 24, "bold")).grid(row=0, column=0, columnspan=2, pady=20)
    ttk.Label(app.adicionar_item_frame, text="Nome do Item", font=("Arial", 14)).grid(row=1, column=0, pady=5, padx=5, sticky="e")
    nome_entry = ttk.Entry(app.adicionar_item_frame, font=("Arial", 14), width=30)
    nome_entry.grid(row=1, column=1, pady=5, padx=5)

    ttk.Label(app.adicionar_item_frame, text="Quantidade", font=("Arial", 14)).grid(row=2, column=0, pady=5, padx=5, sticky="e")
    quantidade_entry = ttk.Entry(app.adicionar_item_frame, font=("Arial", 14), width=30)
    quantidade_entry.grid(row=2, column=1, pady=5, padx=5)

    ttk.Label(app.adicionar_item_frame, text="Número de Série", font=("Arial", 14)).grid(row=3, column=0, pady=5, padx=5, sticky="e")
    serial_number_entry = ttk.Entry(app.adicionar_item_frame, font=("Arial", 14), width=30)
    serial_number_entry.grid(row=3, column=1, pady=5, padx=5)

    # Obter a lista de caixas
    caixas = Caixa().listar_todos()
    caixas_str = "\n".join([f"ID: {caixa[0]}, Nome: {caixa[1]}" for caixa in caixas])
    ttk.Label(app.adicionar_item_frame, text="ID da Caixa (Escolha entre os IDs existentes):", font=("Arial", 14)).grid(row=4, column=0, pady=5, padx=5, sticky="e")
    caixa_id_entry = ttk.Entry(app.adicionar_item_frame, font=("Arial", 14), width=30)
    caixa_id_entry.grid(row=4, column=1, pady=5, padx=5)
    ttk.Label(app.adicionar_item_frame, text=caixas_str, font=("Arial", 12)).grid(row=5, column=0, columnspan=2, pady=5, padx=5)

    def salvar_item():
        nome = nome_entry.get()
        quantidade = quantidade_entry.get()
        serial_number = serial_number_entry.get()
        caixa_id = caixa_id_entry.get()
        if nome and quantidade and serial_number and caixa_id:
            item = Item()
            item.adicionar(nome, int(quantidade), serial_number, int(caixa_id))
            messagebox.showinfo("Sucesso", "Item adicionado com sucesso.")
            app.mostrar_menu_principal()
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")

    ttk.Button(app.adicionar_item_frame, text="Salvar", command=salvar_item, style="primary.TButton").grid(row=6, column=0, columnspan=2, pady=20, ipadx=10, ipady=5)
    ttk.Button(app.adicionar_item_frame, text="Voltar", command=app.mostrar_menu_principal, style="secondary.TButton").grid(row=7, column=0, columnspan=2, pady=10, ipadx=10, ipady=5)