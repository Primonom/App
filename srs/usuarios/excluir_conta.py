from tkinter import messagebox
import sqlite3

def excluir_conta(app):
    resposta = messagebox.askyesno("Excluir Conta", "Tem certeza que deseja excluir sua conta?")
    if resposta:
        conexao = sqlite3.connect('sistema_organizacao.db')
        cursor = conexao.cursor()

        try:
            cursor.execute("DELETE FROM usuarios WHERE id = ?", (app.usuario_atual,))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Conta excluída com sucesso.")
            app.sair()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir conta: {e}")
        finally:
            conexao.close()