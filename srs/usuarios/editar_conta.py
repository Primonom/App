from tkinter import simpledialog, messagebox, ttk
import tkinter as tk
from usuarios.usuario import Usuario

def editar_conta(app):
    def alterar_usuario_senha():
        novo_username = simpledialog.askstring("Editar Conta", "Novo nome de usuário:")
        nova_senha = simpledialog.askstring("Editar Conta", "Nova senha:", show="*")

        if novo_username and nova_senha:
            usuario = Usuario()
            
            # Verificar se o nome de usuário já existe
            usuario.cursor.execute("SELECT COUNT(*) FROM usuarios WHERE username = ?", (novo_username,))
            count = usuario.cursor.fetchone()[0]
            
            if count > 0:
                messagebox.showerror("Erro", "Nome de usuário já existe. Tente outro.")
            else:
                try:
                    usuario.cursor.execute("UPDATE usuarios SET username = ?, senha = ? WHERE id = ?", (novo_username, nova_senha, app.usuario_atual))
                    usuario.conexao.commit()
                    messagebox.showinfo("Sucesso", "Conta atualizada com sucesso!")
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao atualizar conta: {e}")
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            
    # Exibir opções para alterar nome de usuário ou senha
    def exibir_opcoes():
        alterar_usuario_senha()

    exibir_opcoes()