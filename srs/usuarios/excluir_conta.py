from tkinter import messagebox
from usuarios.usuario import Usuario

def excluir_conta(app):
    resposta = messagebox.askyesno("Excluir Conta", "Tem certeza que deseja excluir sua conta?")
    if resposta:
        usuario_id = app.usuario_atual
        usuario = Usuario()
        if usuario.excluir_usuario(usuario_id):
            messagebox.showinfo("Sucesso", "Conta excluída com sucesso!")
            app.sair()
        else:
            messagebox.showerror("Erro", "Erro ao excluir a conta.")