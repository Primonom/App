def sair(app):
    app.usuario_atual = None
    app.main_menu_frame.pack_forget()
    app.login_frame.pack(expand=True)