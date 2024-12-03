from tkinter import messagebox
from usuarios.usuario import Usuario

def login(app):
    username = app.username_entry.get()
    senha = app.senha_entry.get()
    usuario = Usuario()

    usuario_id = usuario.verificar_login(username, senha)
    if usuario_id:
        app.usuario_atual = usuario_id
        app.log_acoes.registrar_acao(usuario_id, "login", "Login realizado")
        app.mostrar_menu_principal()
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos")