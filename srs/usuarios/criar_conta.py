from tkinter import simpledialog, messagebox
from ttkbootstrap import ttk
from usuarios.usuario import Usuario

def criar_conta(app):
    # Criar um novo frame para a criação de conta
    app.criar_conta_frame = ttk.Frame(app.root)
    app.criar_conta_frame.grid(row=0, column=0, sticky="nsew")

    # Adicionar widgets ao frame de criação de conta
    ttk.Label(app.criar_conta_frame, text="Criar Nova Conta", font=("Arial", 24, "bold")).grid(row=0, column=0, columnspan=2, pady=20)
    ttk.Label(app.criar_conta_frame, text="Username", font=("Arial", 14)).grid(row=1, column=0, pady=5, padx=5, sticky="e")
    username_entry = ttk.Entry(app.criar_conta_frame, font=("Arial", 14), width=30)
    username_entry.grid(row=1, column=1, pady=5, padx=5)

    ttk.Label(app.criar_conta_frame, text="Senha", font=("Arial", 14)).grid(row=2, column=0, pady=5, padx=5, sticky="e")
    senha_entry = ttk.Entry(app.criar_conta_frame, show="*", font=("Arial", 14), width=30)
    senha_entry.grid(row=2, column=1, pady=5, padx=5)

    def salvar_conta():
        username = username_entry.get()
        senha = senha_entry.get()
        if username and senha:
            usuario = Usuario()
            usuario.criar(username, senha)
            messagebox.showinfo("Sucesso", "Conta criada com sucesso.")
            app.mostrar_login()  # Voltar para a tela de login após criar a conta
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")

    ttk.Button(app.criar_conta_frame, text="Salvar", command=salvar_conta, style="primary.TButton").grid(row=3, column=0, columnspan=2, pady=20, ipadx=10, ipady=5)
    ttk.Button(app.criar_conta_frame, text="Voltar", command=app.mostrar_login, style="secondary.TButton").grid(row=4, column=0, columnspan=2, pady=10, ipadx=10, ipady=5)