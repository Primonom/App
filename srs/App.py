import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
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

        # Menu principal (oculto até o login)
        self.main_menu = tk.Menu(self.root)
        self.root.config(menu=self.main_menu)
        self.setor_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Setores", menu=self.setor_menu)
        self.setor_menu.add_command(label="Adicionar Setor", command=lambda: adicionar_setor(self))
        self.setor_menu.add_command(label="Visualizar Setores", command=lambda: visualizar_setores(self))

        self.caixa_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Caixas", menu=self.caixa_menu)
        self.caixa_menu.add_command(label="Adicionar Caixa", command=lambda: adicionar_caixa(self))
        self.caixa_menu.add_command(label="Visualizar Caixas", command=lambda: visualizar_caixas(self))

        self.item_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Itens", menu=self.item_menu)
        self.item_menu.add_command(label="Adicionar Item", command=lambda: adicionar_item(self))
        self.item_menu.add_command(label="Visualizar Itens", command=lambda: visualizar_itens(self))

        self.main_menu.add_separator()  # Adiciona uma linha separadora
        self.main_menu.add_command(label="Histórico", command=lambda: mostrar_historico(self))

        self.main_menu.entryconfig("Setores", state="disabled")
        self.main_menu.entryconfig("Caixas", state="disabled")
        self.main_menu.entryconfig("Itens", state="disabled")
        self.main_menu.entryconfig("Histórico", state="disabled")

        self.conta_menu = None

        # Log de Ações
        self.log_acoes = LogAcoes()

    def configurar_interface_principal(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(expand=True, fill="both")

        # Centralizar os botões
        button_frame = ttk.Frame(self.main_frame)
        button_frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Button(button_frame, text="Adicionar Setor", command=lambda: adicionar_setor(self)).pack(pady=10)
        ttk.Button(button_frame, text="Visualizar Setores", command=lambda: visualizar_setores(self)).pack(pady=10)

    def mostrar_menu_principal(self):
        self.login_frame.pack_forget()  # Esconde a tela de login
        self.main_menu.entryconfig("Setores", state="normal")
        self.main_menu.entryconfig("Caixas", state="normal")
        self.main_menu.entryconfig("Itens", state="normal")
        self.main_menu.entryconfig("Histórico", state="normal")

        self.conta_menu = ttk.Menubutton(self.root, text="Minha conta", relief=tk.RAISED)
        self.conta_menu.place(relx=0.05, rely=0.05, anchor="nw")

        conta_opcoes = tk.Menu(self.conta_menu, tearoff=0)
        conta_opcoes.add_command(label="Editar Conta", command=lambda: editar_conta(self))
        conta_opcoes.add_command(label="Sair", command=self.sair)
        conta_opcoes.add_separator()
        conta_opcoes.add_command(label="Excluir Conta", command=lambda: excluir_conta(self), foreground="red")
        self.conta_menu.config(menu=conta_opcoes)

        # Configurar interface principal
        self.configurar_interface_principal()

    def sair(self):
        self.usuario_atual = None
        self.main_menu.entryconfig("Setores", state="disabled")
        self.main_menu.entryconfig("Caixas", state="disabled")
        self.main_menu.entryconfig("Itens", state="disabled")
        self.main_menu.entryconfig("Histórico", state="disabled")
        if self.conta_menu:
            self.conta_menu.place_forget()
        self.main_frame.pack_forget()  # Esconde a interface principal
        self.login_frame.pack(expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    root.state('zoomed')
    app = App(root)
    root.mainloop()