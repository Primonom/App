from tkinter import messagebox
from itens.item import Item

def remover_item(app):
    item_id = simpledialog.askinteger("Remover Item", "ID do item a ser removido:")
    if item_id:
        item = Item()
        try:
            item.cursor.execute("DELETE FROM itens WHERE id = ?", (item_id,))
            item.conexao.commit()
            messagebox.showinfo("Sucesso", "Item removido com sucesso.")
            app.log_acoes.registrar_acao(app.usuario_atual, "remover item", f"Item ID '{item_id}' removido")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao remover item: {e}")