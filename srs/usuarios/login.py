from tkinter import messagebox
from usuarios.usuario import Usuario
from log_acoes.log_acoes import LogAcoes  # Adicione esta linha para importar LogAcoes

def login(app):
    username = app.username_entry.get()
    senha = app.senha_entry.get()
    usuario = Usuario()

    usuario_id = usuario.verificar_login(username, senha)
    if usuario_id:
        print("Login bem-sucedido, usuário ID:", usuario_id)  # Print de depuração
        app.usuario_atual = usuario_id
        log_acoes = LogAcoes()
        log_acoes.registrar_acao(usuario_id, "login", "Login realizado")
        app.mostrar_menu_principal()
    else:
        print("Login falhou")  # Print de depuração
        messagebox.showerror("Erro", "Usuário ou senha inválidos")