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
        setores = Setor.consultar_setores()
        messagebox.showinfo("Setores", "\n".join([setor.nome for setor in setores]))

    def adicionar_caixa(self):
        nome = simpledialog.askstring("Adicionar Caixa", "Nome da caixa:")
        if nome:
            caixa = Caixa()
            caixa.adicionar_caixa(nome)
            self.log_acoes.logar_acao(self.usuario_atual, f"Caixa '{nome}' adicionada.")

    def visualizar_caixas(self):
        caixas = Caixa.consultar_caixas()
        messagebox.showinfo("Caixas", "\n".join([caixa.nome for caixa in caixas]))

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
