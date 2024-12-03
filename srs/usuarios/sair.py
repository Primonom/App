def sair(app):
    app.usuario_atual = None
    app.main_menu.entryconfig("Setores", state="disabled")
    app.main_menu.entryconfig("Caixas", state="disabled")
    app.main_menu.entryconfig("Itens", state="disabled")
    app.main_menu.entryconfig("Histórico", state="disabled")
    if app.conta_menu:
        app.conta_menu.place_forget()
    app.login_frame.pack(expand=True)