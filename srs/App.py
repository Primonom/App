from tkinter import messagebox, simpledialog
from tkinter import ttk
import tkinter as tk
from usuarios.login import login
from usuarios.criar_conta import criar_conta
from usuarios.editar_conta import editar_conta
from usuarios.excluir_conta import excluir_conta
from setores.visualizar_setores import visualizar_setores
from caixas.visualizar_caixas import visualizar_caixas
from itens.visualizar_itens import visualizar_itens
from log_acoes.mostrar_historico import mostrar_historico
from log_acoes.log_acoes import LogAcoes

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Organização de Materiais - Milhagem")
        self.usuario_atual = None  # Armazena o usuário logado

        # Aplicar tema
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Você pode escolher outros temas como 'alt', 'default', 'classic'

        # Interface de Login
        self.login_frame = ttk.Frame(self.root)
        self.login_frame.pack(expand=True)

        self.inner_frame = ttk.Frame(self.login_frame)
        self.inner_frame.pack()

        ttk.Label(self.inner_frame, text="Username", font=("Arial", 14)).pack(pady=10, padx=10)
        self.username_entry = ttk.Entry(self.inner_frame, font=("Arial", 14), width=30)
        self.username_entry.pack(pady=10, padx=10)

        ttk.Label(self.inner_frame, text="Senha", font=("Arial", 14)).pack(pady=10, padx=10)
        self.senha_entry = ttk.Entry(self.inner_frame, show="*", font=("Arial", 14), width=30)
        self.senha_entry.pack(pady=10, padx=10)

        ttk.Button(self.inner_frame, text="Entrar", command=lambda: login(self)).pack(pady=20)
        ttk.Button(self.inner_frame, text="Criar nova conta", command=lambda: criar_conta(self)).pack(pady=10)

        # Frame do Menu Principal (oculto até o login)
        self.main_frame = ttk.Frame(self.root)
        
        # Barra lateral fixa à direita
        self.sidebar_frame = ttk.Frame(self.main_frame)
        self.sidebar_frame.pack(side="right", fill="y")

        ttk.Button(self.sidebar_frame, text="Visualizar Setores", command=lambda: visualizar_setores(self)).pack(pady=10)
        ttk.Button(self.sidebar_frame, text="Visualizar Caixas", command=lambda: visualizar_caixas(self)).pack(pady=10)
        ttk.Button(self.sidebar_frame, text="Visualizar Itens", command=lambda: visualizar_itens(self)).pack(pady=10)
        ttk.Button(self.sidebar_frame, text="Mostrar Histórico", command=lambda: mostrar_historico(self)).pack(pady=10)
        ttk.Button(self.sidebar_frame, text="Sair", command=lambda: self.sair()).pack(pady=10)

        # Área central que muda conforme a seleção dos botões
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.pack(side="left", fill="both", expand=True)

    def mostrar_menu_principal(self):
        self.login_frame.pack_forget()
        self.main_frame.pack(expand=True, fill="both")
        visualizar_setores(self)  # Exibir setores após o login

    def sair(self):
        self.main_frame.pack_forget()
        self.login_frame.pack(expand=True)
        self.usuario_atual = None

if __name__ == "__main__":
    root = tk.Tk()
    root.state('zoomed')
    app = App(root)
    root.mainloop()