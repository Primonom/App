from tkinter import ttk, messagebox
from usuarios.usuario import Usuario

def criar_conta(app):
    app.login_frame.pack_forget()

    app.criar_conta_frame = ttk.Frame(app.root)
    app.criar_conta_frame.pack(expand=True, fill="both")

    app.inner_frame_criar_conta = ttk.Frame(app.criar_conta_frame)
    app.inner_frame_criar_conta.place(relx=0.5, rely=0.5, anchor="center")

    ttk.Label(app.inner_frame_criar_conta, text="Novo Usuário", font=("Arial", 14)).pack(pady=10)

    app.novo_username_entry = ttk.Entry(app.inner_frame_criar_conta, font=("Arial", 14), width=30)
    app.novo_username_entry.pack(pady=10)

    ttk.Label(app.inner_frame_criar_conta, text="Nova Senha", font=("Arial", 14)).pack(pady=10)
    app.nova_senha_entry = ttk.Entry(app.inner_frame_criar_conta, show="*", font=("Arial", 14), width=30)
    app.nova_senha_entry.pack(pady=10)

    ttk.Button(app.inner_frame_criar_conta, text="Criar Conta", command=lambda: salvar_novo_usuario(app)).pack(pady=10)
    ttk.Button(app.inner_frame_criar_conta, text="Voltar", command=lambda: voltar_para_login(app)).pack(pady=10)

def salvar_novo_usuario(app):
    novo_username = app.novo_username_entry.get()
    nova_senha = app.nova_senha_entry.get()

    if novo_username and nova_senha:
        usuario = Usuario()
        if usuario.adicionar_usuario(novo_username, nova_senha):
            messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
            app.login_frame.pack(expand=True)
            app.criar_conta_frame.pack_forget()
        else:
            messagebox.showerror("Erro", "O nome de usuário já existe.")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos.")

def voltar_para_login(app):
    app.criar_conta_frame.pack_forget()
    app.login_frame.pack(expand=True)