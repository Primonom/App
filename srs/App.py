from ttkbootstrap import Style
import ttkbootstrap as ttk
from usuarios.login import login
from usuarios.criar_conta import criar_conta
from usuarios.editar_conta import editar_conta
from usuarios.excluir_conta import excluir_conta
from setores.adicionar_setor import adicionar_setor
from setores.visualizar_setores import visualizar_setores
from setores.excluir_setor import excluir_setor  # Importar a nova função
from caixas.adicionar_caixa import adicionar_caixa
from caixas.visualizar_caixas import visualizar_caixas
from caixas.excluir_caixa import excluir_caixa  # Importar a nova função
from itens.adicionar_item import adicionar_item
from itens.visualizar_itens import visualizar_itens
from itens.excluir_item import excluir_item  # Importar a nova função
from setores.setor import Setor
from caixas.caixa import Caixa
from itens.item import Item
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
            ("Excluir Setor", lambda: excluir_setor(self)),  # Adicionar botão para excluir setor
            ("Excluir Caixa", lambda: excluir_caixa(self)),  # Adicionar botão para excluir caixa
            ("Excluir Item", lambda: excluir_item(self)),  # Adicionar botão para excluir item
        ])

        # Visualizações
        self.visual_frame = self.create_section(self.main_menu_frame, "Visualizações", [
            ("Visualizar Setores", lambda: self.mostrar_setores()),
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

    def mostrar_setores(self):
        """Exibe os setores na coluna central."""
        self.history.append(self.mostrar_setores)
        for widget in self.central_frame.winfo_children():
            widget.destroy()

        setores = Setor().listar_todos()
        if setores:
            for setor in setores:
                button = ttk.Button(self.central_frame, text=setor[1], command=lambda s=setor: self.mostrar_caixas(s[0]))
                button.pack(pady=10, ipadx=10, ipady=5, fill='x')
                button.configure(style="TButton")
        else:
            ttk.Label(self.central_frame, text="Nenhum setor encontrado.", font=("Arial", 14)).pack(pady=20)

    def mostrar_caixas(self, setor_id):
        """Exibe as caixas de um setor na coluna central."""
        self.history.append(lambda: self.mostrar_caixas(setor_id))
        for widget in self.central_frame.winfo_children():
            widget.destroy()

        caixas = Caixa().listar_caixas_por_setor(setor_id)
        if caixas:
            for caixa in caixas:
                button = ttk.Button(self.central_frame, text=caixa[1], command=lambda c=caixa: self.mostrar_itens(c[0]))
                button.pack(pady=10, ipadx=10, ipady=5, fill='x')
                button.configure(style="TButton", font=("Arial", 14))
        else:
            ttk.Label(self.central_frame, text="Nenhuma caixa encontrada.", font=("Arial", 14)).pack(pady=20)

    def mostrar_itens(self, caixa_id):
        """Exibe os itens de uma caixa na coluna central."""
        self.history.append(lambda: self.mostrar_itens(caixa_id))
        for widget in self.central_frame.winfo_children():
            widget.destroy()

        itens = Item().listar_itens_por_caixa(caixa_id)
        if itens:
            for item in itens:
                ttk.Label(self.central_frame, text=f"{item[1]} (Quantidade: {item[2]})", font=("Arial", 12)).pack(pady=5)
        else:
            ttk.Label(self.central_frame, text="Nenhum item encontrado.", font=("Arial", 14)).pack(pady=20)

    def voltar(self):
        """Volta para a página anterior na pilha de navegação."""
        if len(self.history) > 1:
            self.history.pop()  # Remove a página atual
            self.history.pop()()  # Remove e chama a página anterior

    def sair(self):
        if messagebox.askyesno("Sair", "Tem certeza que deseja sair?"):
            self.usuario_atual = None
            self.mostrar_login()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x800")  # Definir um tamanho padrão
    app = App(root)
    root.mainloop()