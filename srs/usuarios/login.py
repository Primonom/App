from tkinter import messagebox
from usuarios.usuario import Usuario
from log_acoes.log_acoes import LogAcoes
import logging

# Configuração do logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def login(app):
    username = app.username_entry.get()
    senha = app.senha_entry.get()
    logging.debug(f"Tentando login com username: {username}, senha: {senha}")
    usuario = Usuario()

    usuario_id = usuario.verificar_login(username, senha)
    if usuario_id:
        logging.debug(f"Login bem-sucedido, usuário ID: {usuario_id}")
        app.usuario_atual = usuario_id
        log_acoes = LogAcoes()
        log_acoes.registrar_acao(usuario_id, "login", "Login realizado")
        app.mostrar_menu_principal()
    else:
        logging.debug("Login falhou")
        messagebox.showerror("Erro", "Usuário ou senha inválidos")