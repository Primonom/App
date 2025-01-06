from tkinter import messagebox, simpledialog
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from usuarios.login import login
from usuarios.criar_conta import criar_conta
from usuarios.editar_conta import editar_conta
from usuarios.excluir_conta import excluir_conta
from setores.visualizar_setores import visualizar_setores
from caixas.visualizar_caixas import visualizar_caixas
from itens.visualizar_itens import visualizar_itens
from log_acoes.mostrar_historico import mostrar_historico
from log_acoes.log_acoes import LogAcoes
from setores.adicionar_setor import adicionar_setor
from caixas.adicionar_caixa import adicionar_caixa
from itens.adicionar_item import adicionar_item

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Organização de Materiais - Milhagem")
        self.usuario_atual = None  # Armazena o usuário logado
        self.history = []  # Histórico de navegação

        # Aplicar tema
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Você pode escolher outros temas como 'alt', 'default', 'classic'

        # Interface de Login
        self.login_frame = ttk.Frame(self.root)
        self.login_frame.pack(expand=True, fill="both")

        self.inner_frame = ttk.Frame(self.login_frame)
        self.inner_frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(self.inner_frame, text="Username", font=("Arial", 14)).pack(pady=10, padx=10)
        self.username_entry = ttk.Entry(self.inner_frame, font=("Arial", 14), width=30)
        self.username_entry.pack(pady=10, padx=10)

        ttk.Label(self.inner_frame, text="Senha", font=("Arial", 14)).pack(pady=10, padx=10)
        self.senha_entry = ttk.Entry(self.inner_frame, show="*", font=("Arial", 14), width=30)
        self.senha_entry.pack(pady=10, padx=10)

        ttk.Button(self.inner_frame, text="Entrar", command=lambda: self.login()).pack(pady=20)
        ttk.Button(self.inner_frame, text="Criar nova conta", command=lambda: criar_conta(self)).pack(pady=10)

        # Frame do Menu Principal (oculto até o login)
        self.main_content_frame = ttk.Frame(self.root)

        # Carregar imagem de fundo
        self.bg_image = Image.open(r"C:\Users\gabri\App\srs\premiacao.jpg")  # Substitua pelo caminho correto da sua imagem
        self.bg_image = self.bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Canvas para exibir a imagem de fundo
        self.canvas = tk.Canvas(self.main_content_frame, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Frame principal sobre o Canvas
        self.main_frame = ttk.Frame(self.canvas)
        self.canvas.create_window(0, 0, anchor="nw", window=self.main_frame)

        # Barra lateral fixa à direita
        self.sidebar_frame = ttk.Frame(self.main_frame)
        self.sidebar_frame.pack(side="right", fill="y", padx=10, pady=10)

        # Adicionar divisória
        self.divisoria = ttk.Separator(self.main_frame, orient='vertical')
        self.divisoria.pack(side="right", fill="y")

        button_options = {'width': 20}
        ttk.Button(self.sidebar_frame, text="Adicionar Setor", command=lambda: adicionar_setor(self), **button_options).pack(pady=10)
        ttk.Button(self.sidebar_frame, text="Visualizar Setores", command=lambda: visualizar_setores(self), **button_options).pack(pady=10)
        ttk.Button(self.sidebar_frame, text="Adicionar Caixa", command=lambda: adicionar_caixa(self), **button_options).pack(pady=10)
        ttk.Button(self.sidebar_frame, text="Visualizar Caixas", command=lambda: visualizar_caixas(self), **button_options).pack(pady=10)
        ttk.Button(self.sidebar_frame, text="Adicionar Item", command=lambda: adicionar_item(self), **button_options).pack(pady=10)
        ttk.Button(self.sidebar_frame, text="Visualizar Itens", command=lambda: visualizar_itens(self), **button_options).pack(pady=10)
        ttk.Button(self.sidebar_frame, text="Mostrar Histórico", command=lambda: mostrar_historico(self), **button_options).pack(pady=10)
        ttk.Button(self.sidebar_frame, text="Editar Conta", command=lambda: editar_conta(self), **button_options).pack(pady=10)
        ttk.Button(self.sidebar_frame, text="Excluir Conta", command=lambda: excluir_conta(self), **button_options).pack(pady=10)
        ttk.Button(self.sidebar_frame, text="Sair", command=lambda: self.sair(), **button_options).pack(pady=10)

        # Área central que muda conforme a seleção dos botões
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Botão Voltar
        self.back_button = ttk.Button(self.sidebar_frame, text="Voltar", command=self.voltar, **button_options)
        self.back_button.pack(pady=10)

    def login(self):
        login(self)

    def mostrar_menu_principal(self):
        self.login_frame.pack_forget()
        self.main_content_frame.pack(expand=True, fill="both")
        self.history.append(visualizar_setores)  # Adicionar ao histórico
        visualizar_setores(self)  # Exibir setores após o login

    def sair(self):
        self.main_content_frame.pack_forget()
        self.login_frame.pack(expand=True, fill="both")
        self.usuario_atual = None

    def voltar(self):
        if len(self.history) > 1:
            self.history.pop()  # Remover a página atual do histórico
            previous_page = self.history[-1]  # Obter a página anterior
            previous_page(self)  # Navegar para a página anterior

if __name__ == "__main__":
    root = tk.Tk()
    root.state('zoomed')
    app = App(root)
    root.mainloop()