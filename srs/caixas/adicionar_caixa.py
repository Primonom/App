from tkinter import simpledialog, messagebox, ttk
import tkinter as tk
from caixas.caixa import Caixa

def adicionar_caixa(app):
    nome = simpledialog.askstring("Adicionar Caixa", "Nome da caixa:")
    setor_id = simpledialog.askinteger("Adicionar Caixa", "ID do Setor ao qual a caixa pertence:")            
    
    if nome and setor_id:
        caixa = Caixa()
        caixa.adicionar_caixa(nome, setor_id)
        app.log_acoes.registrar_acao(app.usuario_atual, "adicionar caixa", f"Caixa '{nome}' adicionada no setor '{setor_id}'")
        mostrar_quadro_caixa(app, nome, setor_id)

def mostrar_quadro_caixa(app, nome_caixa, setor_id):
    quadro_caixa = tk.Toplevel(app.root)
    quadro_caixa.title("Nova Caixa Adicionada")
    quadro_caixa.geometry("300x150")

    ttk.Label(quadro_caixa, text="Caixa criada com sucesso!", font=("Arial", 14, "bold")).pack(pady=10)
    ttk.Label(quadro_caixa, text=f"Nome da Caixa: {nome_caixa}", font=("Arial", 12)).pack(pady=5)

    ttk.Button(quadro_caixa, text="Fechar", command=quadro_caixa.destroy).pack(pady=10)