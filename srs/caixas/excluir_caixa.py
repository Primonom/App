from tkinter import messagebox
from caixas.caixa import Caixa

def excluir_caixa(app):
    caixa_id = simpledialog.askinteger("Excluir Caixa", "ID da caixa a ser excluída:")
    if caixa_id:
        caixa = Caixa()
        try:
            caixa.cursor.execute("DELETE FROM caixas WHERE id = ?", (caixa_id,))
            caixa.conexao.commit()
            messagebox.showinfo("Sucesso", "Caixa excluída com sucesso.")
            app.log_acoes.registrar_acao(app.usuario_atual, "excluir caixa", f"Caixa ID '{caixa_id}' excluída")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir caixa: {e}")