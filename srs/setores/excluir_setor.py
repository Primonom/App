from tkinter import messagebox
from setores.setor import Setor

def excluir_setor(app):
    setor_id = simpledialog.askinteger("Excluir Setor", "ID do setor a ser excluído:")
    if setor_id:
        setor = Setor()
        try:
            setor.cursor.execute("DELETE FROM setores WHERE id = ?", (setor_id,))
            setor.conexao.commit()
            messagebox.showinfo("Sucesso", "Setor excluído com sucesso.")
            app.log_acoes.registrar_acao(app.usuario_atual, "excluir setor", f"Setor ID '{setor_id}' excluído")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir setor: {e}")