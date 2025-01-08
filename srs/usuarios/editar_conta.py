from tkinter import simpledialog, messagebox, ttk
import tkinter as tk
from usuarios.usuario import Usuario

def editar_conta(app):
    novo_username = simpledialog.askstring("Editar Conta", "Novo nome de usuário:")
    nova_senha = simpledialog.askstring("Editar Conta", "Nova senha:", show="*")

    if novo_username and nova_senha:
        usuario = Usuario()
        try:
            usuario.cursor.execute("UPDATE usuarios SET username = ?, senha = ? WHERE id = ?", (novo_username, nova_senha, app.usuario_atual))
            usuario.conexao.commit()
            messagebox.showinfo("Sucesso", "Conta atualizada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar conta: {e}")
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")