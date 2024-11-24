import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from usuario import Usuario
from setor import Setor
from caixa import Caixa
from item import Item
from log_acoes import LogAcoes
from tkinter import simpledialog
import sqlite3


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Organização de Materiais - Milhagem")
        self.usuario_atual = None  # Armazena o usuário logado

        # Interface de Login
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(expand=True)
        
        self.inner_frame = tk.Frame(self.login_frame)
        self.inner_frame.pack()
        
        tk.Label(self.inner_frame, text="Username", font=("Arial", 14)).pack(pady=10, padx=10)
        self.username_entry = tk.Entry(self.inner_frame, font=("Arial", 14), width=30)
        self.username_entry.pack(pady=10, padx=10)
        
        tk.Label(self.inner_frame, text="Senha", font=("Arial", 14)).pack(pady=10, padx=10)
        self.senha_entry = tk.Entry(self.inner_frame, show="*", font=("Arial", 14), width=30)
        self.senha_entry.pack(pady=10, padx=10)
        
        tk.Button(self.login_frame, text="Entrar", font=("Arial", 14), command=self.login).pack(pady=20)
        
        tk.Button(self.login_frame, text="Criar nova conta", font=("Arial", 14), command=self.criar_conta).pack(pady=10)

        
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
        
        self.main_menu.add_separator()  # Adiciona uma linha separadora
        self.main_menu.add_command(label="Histórico", command=self.mostrar_historico)
        
        self.main_menu.entryconfig("Setores", state="disabled")
        self.main_menu.entryconfig("Caixas", state="disabled")
        self.main_menu.entryconfig("Itens", state="disabled")
        self.main_menu.entryconfig("Histórico", state="disabled")

        self.conta_menu = None
        
        # Log de Ações
        self.log_acoes = LogAcoes()
        
    def mostrar_historico(self):
        try:
            log = LogAcoes()
            acoes = log.listar_todas_acoes()
            if not acoes:
                messagebox.showinfo("Histórico de Ações", "Nenhuma ação registrada.")
            else:
                historico_texto = "\n".join([f"Usuário {usuario_id}: {acao} ({descricao}) em {data_hora}" for usuario_id, acao, descricao, data_hora in acoes])
                messagebox.showinfo("Histórico de Ações", historico_texto)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar histórico: {str(e)}")

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
        self.main_menu.entryconfig("Histórico", state="normal")


        self.conta_menu = tk.Menubutton(self.root, text="Minha conta", relief=tk.RAISED)
        self.conta_menu.place(relx=0.05, rely=0.05, anchor="nw")

        conta_opcoes = tk.Menu(self.conta_menu, tearoff=0)
        conta_opcoes.add_command(label="Editar Conta")
        conta_opcoes.add_command(label="Sair", command=self.sair)
        conta_opcoes.add_separator()
        conta_opcoes.add_command(label="Excluir Conta", command=self.confirmar_exclusao, foreground="red")
        self.conta_menu["menu"] = conta_opcoes

    def confirmar_exclusao(self):
        resposta = messagebox.askyesno("Excluir Conta", "Tem certeza que deseja excluir sua conta?")
        if resposta:
            self.excluir_conta()

    def excluir_conta(self):
        conexao = sqlite3.connect('sistema_organizacao.db')
        cursor = conexao.cursor()

        try:
            cursor.execute("DELETE FROM usuarios WHERE id = ?", (self.usuario_atual,))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Conta excluída com sucesso.")
            self.sair()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir conta: {e}")
        finally:
            conexao.close()

    def sair(self):
        self.usuario_atual = None
        self.main_menu.entryconfig("Setores", state="disabled")
        self.main_menu.entryconfig("Caixas", state="disabled")
        self.main_menu.entryconfig("Itens", state="disabled")
        if self.conta_menu:
            self.conta_menu.place_forget()
        self.login_frame.pack(expand=True)
    
    def criar_conta(self):
        self.login_frame.pack_forget()

        self.criar_conta_frame = tk.Frame(self.root)
        self.criar_conta_frame.pack(expand=True, fill="both")

        self.inner_frame_criar_conta = tk.Frame(self.criar_conta_frame)
        self.inner_frame_criar_conta.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(self.inner_frame_criar_conta, text="Novo Usuário", font=("Arial", 14)).pack(pady=10)

        self.novo_username_entry = tk.Entry(self.inner_frame_criar_conta, font=("Arial", 14), width=30)
        self.novo_username_entry.pack(pady=10)

        tk.Label(self.inner_frame_criar_conta, text="Nova Senha", font=("Arial", 14)).pack(pady=10)
        self.nova_senha_entry = tk.Entry(self.inner_frame_criar_conta, show="*", font=("Arial", 14), width=30)
        self.nova_senha_entry.pack(pady=10)

        tk.Button(self.inner_frame_criar_conta, text="Criar Conta", font=("Arial", 14), command=self.salvar_novo_usuario).pack(pady=10)

        tk.Button(self.inner_frame_criar_conta, text="Voltar", font=("Arial", 12), command=self.voltar_para_login).pack(pady=10)

    def voltar_para_login(self):
        self.criar_conta_frame.pack_forget()

        self.login_frame.pack(expand=True)
    
    def salvar_novo_usuario(self):
        novo_username = self.novo_username_entry.get()
        nova_senha = self.nova_senha_entry.get()

        if novo_username and nova_senha:
            if self.verificar_usuario_existente(novo_username):
                messagebox.showerror("Erro", "O nome de usuário já existe.")
            else:
                self.adicionar_usuario_db(novo_username, nova_senha)
                messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
                self.login_frame.pack(expand=True)
                self.criar_conta_frame.pack_forget()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos.")

    def verificar_usuario_existente(self, username):
        conexao = sqlite3.connect('sistema_organizacao.db')
        cursor = conexao.cursor()
        
        cursor.execute("SELECT 1 FROM usuarios WHERE username = ?", (username,))
        existe = cursor.fetchone() is not None
        
        conexao.close()
        
        return existe

    def adicionar_usuario_db(self, username, senha):
        conexao = sqlite3.connect('sistema_organizacao.db')
        cursor = conexao.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (username, senha) VALUES (?, ?)", (username, senha))
            conexao.commit()
        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", "O nome de usuário já existe.")
        finally:
            conexao.close()

    def adicionar_setor(self):
        nome = simpledialog.askstring("Adicionar Setor", "Nome do setor:")
        if nome:
            setor = Setor()
            setor.adicionar_setor(nome)
            self.log_acoes.registrar_acao(self.usuario_atual, "adicionar setor", f"Setor '{nome}' adicionado")
            self.mostrar_quadro_setor(nome)
            
    def mostrar_quadro_setor(self, nome_setor):
        """
        Exibe um quadro com o nome do novo setor criado.
        :param nome_setor: Nome do setor adicionado.
        """
        quadro_setor = tk.Toplevel(self.root)
        quadro_setor.title("Novo Setor Adicionado")
        quadro_setor.geometry("300x150")

        tk.Label(quadro_setor, text="Setor criado com sucesso!", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(quadro_setor, text=f"Nome do Setor: {nome_setor}", font=("Arial", 12)).pack(pady=5)

        tk.Button(quadro_setor, text="Fechar", command=quadro_setor.destroy).pack(pady=10)

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
        setor_id = simpledialog.askinteger("Adicionar Caixa", "ID do Setor ao qual a caixa pertence:")            
        
        
        if nome and setor_id:
            caixa = Caixa()
            caixa.adicionar_caixa(nome, setor_id)
            self.log_acoes.registrar_acao(self.usuario_atual, "adicionar caixa", f"Caixa '{nome}' adicionada no setor '{setor_id}'")
            self.mostrar_quadro_caixa(nome, setor_id)
            
    def mostrar_quadro_caixa(self, nome_caixa, setor_id):
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
        caixa = Caixa()
        caixas = caixa.listar_caixas_com_setores()
        if not caixas:
            messagebox.showinfo("Caixas", "Nenhuma caixa encontrada.")
            return

        quadro_caixas = tk.Toplevel(self.root)
        quadro_caixas.title("Caixas Existentes")
        quadro_caixas.geometry("500x400")

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
        quantidade = simpledialog.askstring("Tipo do Item", "Tipo do item:")
        serial_number = simpledialog.askstring("Serial Number", "Número serial:")
        caixa_id = simpledialog.askinteger("Caixa", "ID da caixa:")
        
        if nome and quantidade and serial_number and caixa_id:
            item = Item(nome, quantidade, caixa_id)
            item.salvar()
            self.log_acoes.registrar_acao(self.usuario_atual, "adicionar item", f"Item '{nome}' adicionado à caixa {caixa_id}")
            self.mostrar_quadro_item(nome, quantidade, serial_number, caixa_id)

    def mostrar_quadro_item(self, nome_item, quantidade_item, serial_number, caixa_id):
        """
        Exibe um quadro com os detalhes do novo item criado.
        :param nome_item: Nome do item adicionado.
        :param quantidade_item: Quantidade do item adicionado.
        :param serial_number: Número serial do item.
        :param caixa_id: ID da caixa onde o item foi adicionado.
        """
        quadro_item = tk.Toplevel(self.root)
        quadro_item.title("Novo Item Adicionado")
        quadro_item.geometry("300x200")

        tk.Label(quadro_item, text="Item criado com sucesso!", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(quadro_item, text=f"Nome: {nome_item}", font=("Arial", 12)).pack(pady=5)
        tk.Label(quadro_item, text=f"Tipo: {quantidade_item}", font=("Arial", 12)).pack(pady=5)
        tk.Label(quadro_item, text=f"Serial: {serial_number}", font=("Arial", 12)).pack(pady=5)
        tk.Label(quadro_item, text=f"Caixa ID: {caixa_id}", font=("Arial", 12)).pack(pady=5)

        tk.Button(quadro_item, text="Fechar", command=quadro_item.destroy).pack(pady=10)

    def visualizar_itens(self):
        item = Item
        itens = item.listar_todos_itens()
        
        if not itens:
            messagebox.showinfo("Itens", "Nenhum item encontrado.")
            return
        
        quadro_itens = tk.Toplevel(self.root)
        quadro_itens.title("Itens Existentes")
        quadro_itens.geometry("500x400")

        tk.Label(quadro_itens, text="Itens Cadastrados", font=("Arial", 14, "bold")).pack(pady=10)

        colunas = ("ID", "Nome", "Quantidade", "Caixa ID")
        tree = ttk.Treeview(quadro_itens, columns=colunas, show="headings", height=10)
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        tree.heading("ID", text="ID")
        tree.heading("Nome", text="Nome")
        tree.heading("Quantidade", text="Quantidade")
        tree.heading("Caixa ID", text="Caixa ID")

        tree.column("ID", width=50, anchor="center")
        tree.column("Nome", width=150, anchor="center")
        tree.column("Quantidade", width=100, anchor="center")
        tree.column("Caixa ID", width=100, anchor="center")

        for item in itens:
            tree.insert("", "end", values=(item[0], item[1], item[2], item[3]))

        tk.Button(quadro_itens, text="Fechar", command=quadro_itens.destroy).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.state('zoomed')
    app = App(root)
    root.mainloop()