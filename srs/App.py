from ttkbootstrap import Style
import ttkbootstrap as ttk
from usuarios.login import login
from usuarios.criar_conta import criar_conta
from usuarios.editar_conta import editar_conta
from usuarios.excluir_conta import excluir_conta
from setores.adicionar_setor import adicionar_setor
from setores.visualizar_setores import visualizar_setores
from caixas.adicionar_caixa import adicionar_caixa
from caixas.visualizar_caixas import visualizar_caixas
from itens.adicionar_item import adicionar_item
from itens.visualizar_itens import visualizar_itens
import tkinter as tk
from tkinter import messagebox


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Organização de Materiais - Milhagem")
        self.usuario_atual = None  # Armazena o usuário logado
        self.history = []  # Histórico de navegação

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
        self.actions_frame = self.create_section(self.main_menu_frame, "Ações Principais", [
            ("Adicionar Setor", lambda: adicionar_setor(self)),
            ("Adicionar Caixa", lambda: adicionar_caixa(self)),
            ("Adicionar Item", lambda: adicionar_item(self)),
        ])

        # Visualizações
        self.visual_frame = self.create_section(self.main_menu_frame, "Visualizações", [
            ("Visualizar Setores", lambda: visualizar_setores(self)),
            ("Visualizar Caixas", lambda: visualizar_caixas(self)),
            ("Visualizar Itens", lambda: visualizar_itens(self)),
        ])

        # Minha conta
        self.account_frame = self.create_section(self.main_menu_frame, "Minha Conta", [
            ("Editar Conta", lambda: editar_conta(self)),
            ("Excluir Conta", lambda: excluir_conta(self)),
            ("Sair", lambda: self.sair()),
        ], danger=True)

        # Layout do Menu Principal
        self.actions_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')
        self.visual_frame.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')
        self.account_frame.grid(row=0, column=2, padx=20, pady=20, sticky='nsew')

        self.main_menu_frame.grid_rowconfigure(0, weight=1)
        self.main_menu_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Começar no login
        self.mostrar_login()

    def create_section(self, parent, title, buttons, danger=False):
        frame = ttk.Frame(parent, padding=20, bootstyle="secondary")
        frame.pack_propagate(False)
        frame.grid_propagate(False)

        # Título da seção
        ttk.Label(frame, text=title, font=("Arial", 16, "bold"), anchor="center").pack(pady=10)

        # Adicionar botões
        for text, command in buttons:
            style = "danger.TButton" if danger else "success.Outline.TButton"
            ttk.Button(frame, text=text, command=command, style=style).pack(pady=10, ipadx=10, ipady=5, fill='x')

        return frame

    def mostrar_login(self):
        """Exibe a tela de login e esconde o menu principal."""
        self.main_menu_frame.grid_forget()
        self.login_frame.grid(row=0, column=0, sticky="nsew")

    def mostrar_menu_principal(self):
        """Exibe o menu principal e esconde a tela de login."""
        self.login_frame.grid_forget()
        self.main_menu_frame.grid(row=0, column=0, sticky="nsew")

    def sair(self):
        if messagebox.askyesno("Sair", "Tem certeza que deseja sair?"):
            self.usuario_atual = None
            self.mostrar_login()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x800")  # Definir um tamanho padrão
    app = App(root)
    root.mainloop()
