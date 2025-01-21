from ttkbootstrap import Style
import ttkbootstrap as ttk
from usuarios.login import login
from usuarios.criar_conta import criar_conta
from usuarios.editar_conta import editar_conta
from usuarios.excluir_conta import excluir_conta
from setores.adicionar_setor import adicionar_setor
from setores.visualizar_setores import visualizar_setores
from setores.excluir_setor import excluir_setor
from caixas.adicionar_caixa import adicionar_caixa
from caixas.visualizar_caixas import visualizar_caixas
from caixas.excluir_caixa import excluir_caixa
from itens.adicionar_item import adicionar_item
from itens.visualizar_itens import visualizar_itens
from itens.excluir_item import excluir_item
from utils.navigation import Navigation
from utils.layout import create_section
import tkinter as tk
from tkinter import messagebox


class App(Navigation):
    def __init__(self, root):
        super().__init__(root)
        self.root.title("App de Organização de Materiais - Milhagem")
        self.usuario_atual = None  # Armazena o usuário logado

        # Aplicar tema com ttkbootstrap
        self.style = Style(theme="superhero")  # Escolha um tema moderno

        # Configurações de layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Interface de Login
        self.login_frame = ttk.Frame(self.root)
        self.login_frame.grid(row=0, column=0, sticky="nsew")

        self.inner_frame = ttk.Frame(self.login_frame)
        self.inner_frame.pack(pady=20)

        ttk.Label(self.inner_frame, text="Login", font=("Arial", 24, "bold")).pack(pady=20)
        ttk.Label(self.inner_frame, text="Username", font=("Arial", 14)).pack(pady=5)
        self.username_entry = ttk.Entry(self.inner_frame, font=("Arial", 14), width=30)
        self.username_entry.pack(pady=5)

        ttk.Label(self.inner_frame, text="Senha", font=("Arial", 14)).pack(pady=5)
        self.senha_entry = ttk.Entry(self.inner_frame, show="*", font=("Arial", 14), width=30)
        self.senha_entry.pack(pady=5)

        ttk.Button(self.inner_frame, text="Entrar", command=lambda: login(self), style="primary.Outline.TButton").pack(pady=20, ipadx=10, ipady=5)
        ttk.Button(self.inner_frame, text="Criar nova conta", command=lambda: criar_conta(self), style="secondary.TButton").pack(pady=10, ipadx=10, ipady=5)

        # Frame do Menu Principal (oculto até o login)
        self.main_menu_frame = ttk.Frame(self.root)
        self.main_menu_frame.grid(row=0, column=0, sticky='nsew')

        # Ações principais
        self.actions_frame = create_section(self.main_menu_frame, "Ações Principais", [
            ("Adicionar Setor", lambda: adicionar_setor(self)),
            ("Adicionar Caixa", lambda: adicionar_caixa(self)),
            ("Adicionar Item", lambda: adicionar_item(self)),
            ("Excluir Setor", lambda: excluir_setor(self)),
            ("Excluir Caixa", lambda: excluir_caixa(self)),
            ("Excluir Item", lambda: excluir_item(self)),
        ])

        # Visualizações
        self.visual_frame = create_section(self.main_menu_frame, "Visualizações", [
            ("Visualizar Setores", lambda: self.mostrar_setores()),
        ])

        # Minha conta
        self.account_frame = create_section(self.main_menu_frame, "Minha Conta", [
            ("Editar Conta", lambda: editar_conta(self)),
            ("Excluir Conta", lambda: excluir_conta(self)),
            ("Sair", lambda: self.sair()),
        ], danger=True)

        # Layout do Menu Principal
        self.actions_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')
        self.visual_frame.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')
        self.account_frame.grid(row=0, column=2, padx=20, pady=20, sticky='nsew')

        self.main_menu_frame.grid_rowconfigure(0, weight=1)
        self.main_menu_frame.grid_columnconfigure(0, weight=1)  # Coluna esquerda
        self.main_menu_frame.grid_columnconfigure(1, weight=4)  # Coluna central
        self.main_menu_frame.grid_columnconfigure(2, weight=1)  # Coluna direita

        # Frame central para exibir setores, caixas e itens
        self.central_frame = ttk.Frame(self.main_menu_frame)
        self.central_frame.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

        # Botão Voltar
        self.back_button = ttk.Button(self.main_menu_frame, text="Voltar", command=self.voltar)
        self.back_button.grid(row=1, column=2, padx=20, pady=20, sticky='sew')

        # Começar no login
        self.mostrar_login()

        # Exibir setores automaticamente ao iniciar
        self.mostrar_setores()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x800")  # Definir um tamanho padrão
    app = App(root)
    root.mainloop()