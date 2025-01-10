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
from setores.setor import Setor
from caixas.caixa import Caixa
from itens.item import Item
import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Organização de Materiais - Milhagem")
        self.usuario_atual = None  # Armazena o usuário logado
        self.history = []  # Histórico de navegação

        # Aplicar tema
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', font=('Arial', 12), padding=10, background='#4CAF50', foreground='white')
        self.style.configure('TLabel', font=('Arial', 12), background='lightgrey', foreground='black')

        # Configurações de layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
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
        self.main_menu_frame = tk.Frame(self.root)
        
        self.main_menu_frame.grid_rowconfigure(0, weight=1)
        self.main_menu_frame.grid_columnconfigure(0, weight=1)
        self.main_menu_frame.grid_columnconfigure(1, weight=1)
        self.main_menu_frame.grid_columnconfigure(2, weight=1)

        # Ações principais (lado esquerdo)
        self.actions_frame = ttk.Frame(self.main_menu_frame)
        self.actions_frame.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)

        ttk.Label(self.actions_frame, text="Ações Principais", font=("Arial", 14)).pack(pady=10)
        ttk.Button(self.actions_frame, text="Adicionar Setor", command=lambda: adicionar_setor(self)).pack(pady=10)
        ttk.Button(self.actions_frame, text="Adicionar Caixa", command=lambda: adicionar_caixa(self)).pack(pady=10)
        ttk.Button(self.actions_frame, text="Adicionar Item", command=lambda: adicionar_item(self)).pack(pady=10)

        # Visualizações (centro)
        self.visual_frame = ttk.Frame(self.main_menu_frame)
        self.visual_frame.grid(row=0, column=1, sticky='nsew', padx=20, pady=20)

        ttk.Label(self.visual_frame, text="Visualizações", font=("Arial", 14)).pack(pady=10)
        ttk.Button(self.visual_frame, text="Visualizar Setores", command=lambda: visualizar_setores(self)).pack(pady=10)
        ttk.Button(self.visual_frame, text="Visualizar Caixas", command=lambda: visualizar_caixas(self)).pack(pady=10)
        ttk.Button(self.visual_frame, text="Visualizar Itens", command=lambda: visualizar_itens(self)).pack(pady=10)
        ttk.Button(self.visual_frame, text="Mostrar Histórico", command=lambda: mostrar_historico(self)).pack(pady=10)

        # Minha conta (lado direito)
        self.account_frame = ttk.Frame(self.main_menu_frame)
        self.account_frame.grid(row=0, column=2, sticky='nsew', padx=20, pady=20)

        ttk.Label(self.account_frame, text="Minha Conta", font=("Arial", 14)).pack(pady=10)
        ttk.Button(self.account_frame, text="Editar Conta", command=lambda: editar_conta(self)).pack(pady=10)
        ttk.Button(self.account_frame, text="Excluir Conta", command=lambda: excluir_conta(self)).pack(pady=10)
        ttk.Button(self.account_frame, text="Sair", command=lambda: self.sair()).pack(pady=10)
        ttk.Button(self.account_frame, text="Voltar", command=lambda: self.voltar()).pack(pady=10)

    def mostrar_menu_principal(self):
        self.login_frame.pack_forget()
        self.main_menu_frame.grid(row=0, column=0, sticky='nsew')
        self.carregar_setores()

    def carregar_setores(self):
        self.history.append(self.carregar_setores)
        for widget in self.inner_left_bar.winfo_children():
            widget.destroy()
        for widget in self.central_frame.winfo_children():
            widget.destroy()

        setor = Setor()
        setores = setor.listar_setores()
        for setor in setores:
            button = ttk.Button(self.inner_left_bar, text=setor[1], command=lambda s=setor[0]: self.carregar_caixas(s))
            button.pack(pady=5)

    def carregar_caixas(self, setor_id):
        self.history.append(lambda: self.carregar_caixas(setor_id))
        for widget in self.central_frame.winfo_children():
            widget.destroy()

        caixa = Caixa()
        caixas = caixa.listar_caixas_com_setores()
        for caixa in caixas:
            if caixa[2] == setor_id:
                button = ttk.Button(self.central_frame, text=caixa[1], command=lambda c=caixa[0]: self.carregar_itens(c))
                button.pack(pady=5)

    def carregar_itens(self, caixa_id):
        self.history.append(lambda: self.carregar_itens(caixa_id))
        for widget in self.central_frame.winfo_children():
            widget.destroy()

        item_tree = ttk.Treeview(self.central_frame, columns=("ID", "Nome", "Quantidade", "Serial Number"), show="headings")
        item_tree.heading("ID", text="ID")
        item_tree.heading("Nome", text="Nome")
        item_tree.heading("Quantidade", text="Quantidade")
        item_tree.heading("Serial Number", text="Serial Number")
        item_tree.pack(fill='both', expand=True)

        itens = Item.listar_todos_itens()
        for item in itens:
            if item[4] == caixa_id:
                item_tree.insert("", "end", values=item)

    def pesquisar_item(self):
        query = self.search_entry.get()
        if not query:
            messagebox.showwarning("Pesquisa", "Por favor, insira um termo de pesquisa.")
            return

        for widget in self.central_frame.winfo_children():
            widget.destroy()

        item_tree = ttk.Treeview(self.central_frame, columns=("ID", "Nome", "Quantidade", "Serial Number", "Caixa", "Setor"), show="headings")
        item_tree.heading("ID", text="ID")
        item_tree.heading("Nome", text="Nome")
        item_tree.heading("Quantidade", text="Quantidade")
        item_tree.heading("Serial Number", text="Serial Number")
        item_tree.heading("Caixa", text="Caixa")
        item_tree.heading("Setor", text="Setor")
        item_tree.pack(fill='both', expand=True)

        itens = Item.pesquisar_itens(query)
        for item in itens:
            item_tree.insert("", "end", values=item)

    def voltar(self):
        if len(self.history) > 1:
            self.history.pop()  # Remove the current view
            previous_view = self.history.pop()  # Get the previous view
            previous_view()  # Load the previous view

    def sair(self):
        if messagebox.askyesno("Sair", "Tem certeza que deseja sair?"):
            self.usuario_atual = None
            self.main_menu_frame.grid_forget()
            self.login_frame.grid(row=0, column=0, sticky='nsew')

if __name__ == "__main__":
    root = tk.Tk()
    root.state('zoomed')
    app = App(root)
    root.mainloop()
    