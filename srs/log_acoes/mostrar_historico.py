from tkinter import messagebox
from log_acoes.log_acoes import LogAcoes
from log_acoes.log_acoes import LogAcoes

def mostrar_historico(app):
    try:
        log = LogAcoes()
        acoes = log.listar_todas_acoes()
        if not acoes:
            messagebox.showinfo("Histórico de Ações", "Nenhuma ação registrada.")
        else:
            historico_texto = "\n".join([f"Usuário {usuario_id}: {acao} ({descricao}) em {data_hora}" for usuario_id, acao, descricao, data_hora in acoes])
            messagebox.showinfo("Histórico de Ações", historico_texto)
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao carregar histórico: {str(e)}")