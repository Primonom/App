from tkinter import simpledialog, messagebox
from usuarios.usuario import Usuario
import logging

# Configuração do logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def criar_conta(app):
    username = simpledialog.askstring("Criar Conta", "Nome de usuário:")
    senha = simpledialog.askstring("Criar Conta", "Senha:")
    if username and senha:
        usuario = Usuario()
        if usuario.adicionar_usuario(username, senha):
            logging.debug(f"Conta criada com sucesso para username: {username}")
            messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
        else:
            logging.debug(f"Falha ao criar conta, nome de usuário já existe: {username}")
            messagebox.showerror("Erro", "Nome de usuário já existe.")
    else:
        logging.debug("Nome de usuário e senha são obrigatórios.")
        messagebox.showerror("Erro", "Nome de usuário e senha são obrigatórios.")