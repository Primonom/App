import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from usuario import Usuario
from setor import Setor
from caixa import Caixa
from item import Item
from log_acoes import LogAcoes
from tkinter import simpledialog

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Organização de Materiais - Milhagem")
        self.usuario_atual = None  # Armazena o usuário logado

        # Interface de Login
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()
        
        tk.Label(self.login_frame, text="Username").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1)
        
        tk.Label(self.login_frame, text="Senha").grid(row=1, column=0)
        self.senha_entry = tk.Entry(self.login_frame, show="*")
        self.senha_entry.grid(row=1, column=1)
        
        tk.Button(self.login_frame, text="Entrar", command=self.login).grid(row=2, column=0, columnspan=2)
        
        # Menu principal (oculto até o login)
        self.main_menu = tk.Menu(self.root)
        self.root.config(menu=self.main_menu)
        self.setor_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Setores", menu=self.setor_menu)
        self.setor_menu.add_command(label="Adicionar Setor", command=self.adicionar_setor)
        self.setor_menu.add_command(label="Visualizar Setores", command=self.visualizar_setores)
        
        self.caixa_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Caixas", menu=self.caixa_menu)
        self.caixa_menu.add_command(label="Adicionar Caixa", command=self.adicionar_caixa)
        self.caixa_menu.add_command(label="Visualizar Caixas", command=self.visualizar_caixas)
        
        self.item_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Itens", menu=self.item_menu)
        self.item_menu.add_command(label="Adicionar Item", command=self.adicionar_item)
        self.item_menu.add_command(label="Visualizar Itens", command=self.visualizar_itens)
        
        # Log de Ações
        self.log_acoes = LogAcoes()

    def login(self):
        username = self.username_entry.get()
        senha = self.senha_entry.get()
        usuario = Usuario()

        usuario_id = usuario.verificar_login(username, senha)
        if usuario_id:
            self.usuario_atual = usuario_id
            # Corrigido: usar `registrar_acao` em vez de `logar_acao`
            self.log_acoes.registrar_acao(usuario_id, "login", "Login realizado")
            self.mostrar_menu_principal()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos")

    def mostrar_menu_principal(self):
        self.login_frame.pack_forget()  # Esconde a tela de login
        self.main_menu.entryconfig("Setores", state="normal")
        self.main_menu.entryconfig("Caixas", state="normal")
        self.main_menu.entryconfig("Itens", state="normal")

    def adicionar_setor(self):
        nome = simpledialog.askstring("Adicionar Setor", "Nome do setor:")
        if nome:
            setor = Setor()
            setor.adicionar_setor(nome)
            # Corrigido: usar `registrar_acao` em vez de `logar_acao`
            self.log_acoes.registrar_acao(self.usuario_atual, "adicionar setor", f"Setor '{nome}' adicionado")

    def visualizar_setores(self):
        setor = Setor()
        setores = setor.listar_setores()
        if not setores:
            messagebox.showinfo("Setores", "Nenhum setor encontrado.")
            return
        
        quadro_setores = tk.Toplevel(self.root)
        quadro_setores.title("Setores Existentes")
        quadro_setores.geometry("400x300")

        tk.Label(quadro_setores, text="Setores Cadastrados", font=("Arial", 14, "bold")).pack(pady=10)

        colunas = ("ID", "Nome")
        tree = ttk.Treeview(quadro_setores, columns=colunas, show="headings", height=10)
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        tree.heading("ID", text="ID")
        tree.heading("Nome", text="Nome")
        tree.column("ID", width=50, anchor="center")
        tree.column("Nome", width=150, anchor="center")

        for setor in setores:
            tree.insert("", "end", values=(setor[0], setor[1]))

        tk.Button(quadro_setores, text="Fechar", command=quadro_setores.destroy).pack(pady=10)

    def adicionar_caixa(self):
        nome = simpledialog.askstring("Adicionar Caixa", "Nome da caixa:")
        if nome:
            caixa = Caixa()
            caixa.adicionar_caixa(nome)
            self.log_acoes.registrar_acao(self.usuario_atual, f"Caixa '{nome}' adicionada.")
            self.mostrar_quadro_caixa(nome)
            
    def mostrar_quadro_caixa(self, nome_caixa):
        """
        Exibe um quadro com o nome da nova caixa criada.
        :param nome_caixa: Nome da caixa adicionada.
        """
        quadro_caixa = tk.Toplevel(self.root)
        quadro_caixa.title("Nova Caixa Adicionada")
        quadro_caixa.geometry("300x150")

        tk.Label(quadro_caixa, text="Caixa criada com sucesso!", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(quadro_caixa, text=f"Nome da Caixa: {nome_caixa}", font=("Arial", 12)).pack(pady=5)

        tk.Button(quadro_caixa, text="Fechar", command=quadro_caixa.destroy).pack(pady=10)

    def visualizar_caixas(self):
        caixa = Caixa() # Criação de instância da classe Caixa
        caixas = caixa.listar_caixas()
        if not caixas:
            messagebox.showinfo("Caixas", "Nenhuma caixa encontrada.")
            return

        quadro_caixas = tk.Toplevel(self.root)
        quadro_caixas.title("Caixas Existentes")
        quadro_caixas.geometry("400x300")

        tk.Label(quadro_caixas, text="Caixas Criadas", font=("Arial", 14, "bold")).pack(pady=10)

        colunas = ("ID", "Nome", "Setor")
        tree = ttk.Treeview(quadro_caixas, columns=colunas, show="headings", height=10)
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        tree.heading("ID", text="ID")
        tree.heading("Nome", text="Nome")
        tree.heading("Setor", text="Setor")
        tree.column("ID", width=50, anchor="center")
        tree.column("Nome", width=150, anchor="center")
        tree.column("Setor", width=150, anchor="center")

        for caixa in caixas:
            tree.insert("", "end", values=(caixa[0], caixa[1], caixa[2]))

        tk.Button(quadro_caixas, text="Fechar", command=quadro_caixas.destroy).pack(pady=10)

    def adicionar_item(self):
        nome = simpledialog.askstring("Adicionar Item", "Nome do item:")
        tipo = simpledialog.askstring("Tipo do Item", "Tipo do item:")
        serial_number = simpledialog.askstring("Serial Number", "Número serial:")
        caixa_id = simpledialog.askinteger("Caixa", "ID da caixa:")
        if nome and tipo and serial_number and caixa_id:
            item = Item()
            item.adicionar_item(nome, tipo, serial_number, caixa_id)
            self.log_acoes.logar_acao(self.usuario_atual, f"Item '{nome}' adicionado à caixa {caixa_id}")

    def visualizar_itens(self):
        itens = Item.consultar_itens()
        messagebox.showinfo("Itens", "\n".join([item.nome for item in itens]))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
