from tkinter import messagebox
from usuarios.usuario import Usuario

def login(app):
    username = app.username_entry.get()
    senha = app.senha_entry.get()
    if username and senha:
        usuario = Usuario()
        usuario_id = usuario.verificar_login(username, senha)
        if usuario_id:
            app.usuario_atual = usuario_id
            messagebox.showinfo("Sucesso", f"Login bem-sucedido, usuário ID: {usuario_id}")
            app.mostrar_menu_principal()
        else:
            messagebox.showerror("Erro", "Username ou senha incorretos.")
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")