from tkinter import simpledialog, messagebox
from caixas.caixa import Caixa
from setores.setor import Setor

def adicionar_caixa(app):
    nome = simpledialog.askstring("Adicionar Caixa", "Nome da Caixa:")
    setores = Setor().listar_todos()
    if setores:
        setor_id = simpledialog.askinteger("Adicionar Caixa", "ID do Setor (Escolha entre os IDs existentes):\n" + "\n".join([f"{setor[0]}: {setor[1]}" for setor in setores]))
        if nome and setor_id is not None:
            caixa = Caixa()
            caixa.adicionar(nome, setor_id)
            print(f"Caixa adicionada: {nome}, Setor ID: {setor_id}")  # Adicionar mensagem de depuração
            messagebox.showinfo("Sucesso", "Caixa adicionada com sucesso.")
            app.mostrar_setores()
    else:
        messagebox.showerror("Erro", "Nenhum setor encontrado. Adicione um setor primeiro.")