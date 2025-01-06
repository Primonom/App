from tkinter import simpledialog, messagebox
from usuarios.usuario import Usuario

def editar_conta(app):
    usuario_id = app.usuario_atual
    novo_username = simpledialog.askstring("Editar Conta", "Novo nome de usuário:")
    nova_senha = simpledialog.askstring("Editar Conta", "Nova senha:")
    if novo_username and nova_senha:
        usuario = Usuario()
        if usuario.editar_usuario(usuario_id, novo_username, nova_senha):
            messagebox.showinfo("Sucesso", "Conta editada com sucesso!")
        else:
            messagebox.showerror("Erro", "Erro ao editar a conta.")
    else:
        messagebox.showerror("Erro", "Nome de usuário e senha são obrigatórios.")