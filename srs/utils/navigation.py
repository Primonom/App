from setores.setor import Setor
from caixas.caixa import Caixa
from itens.item import Item
from tkinter import messagebox
from ttkbootstrap import Style
import ttkbootstrap as ttk

class Navigation:
    def __init__(self, root):
        self.root = root
        self.history = []

    def mostrar_login(self):
        """Exibe a tela de login e esconde o menu principal."""
        self.main_menu_frame.grid_forget()
        self.login_frame.grid(row=0, column=0, sticky="nsew")
        if hasattr(self, 'criar_conta_frame'):
            self.criar_conta_frame.grid_forget()
        if hasattr(self, 'adicionar_item_frame'):
            self.adicionar_item_frame.grid_forget()
        if hasattr(self, 'excluir_setor_frame'):
            self.excluir_setor_frame.grid_forget()

    def mostrar_menu_principal(self):
        """Exibe o menu principal e esconde a tela de login."""
        self.login_frame.grid_forget()
        self.main_menu_frame.grid(row=0, column=0, sticky="nsew")
        if hasattr(self, 'adicionar_item_frame'):
            self.adicionar_item_frame.grid_forget()
        if hasattr(self, 'excluir_setor_frame'):
            self.excluir_setor_frame.grid_forget()

    def mostrar_setores(self):
        """Exibe os setores na coluna central."""
        self.history.append(self.mostrar_setores)
        for widget in self.central_frame.winfo_children():
            widget.destroy()

        setores = Setor().listar_todos()
        if setores:
            for setor in setores:
                button = ttk.Button(self.central_frame, text=setor[1], command=lambda s=setor: self.mostrar_caixas(s[0]), style="TButton")
                button.pack(pady=10, ipadx=10, ipady=5, fill='x')
        else:
            ttk.Label(self.central_frame, text="Nenhum setor encontrado.", font=("Arial", 14)).pack(pady=20)

    def mostrar_caixas(self, setor_id):
        """Exibe as caixas de um setor na coluna central."""
        self.history.append(lambda: self.mostrar_caixas(setor_id))
        for widget in self.central_frame.winfo_children():
            widget.destroy()

        caixas = Caixa().listar_caixas_por_setor(setor_id)
        print(f"Caixas encontradas para o setor {setor_id}: {caixas}")  # Adicionar mensagem de depuração
        if caixas:
            for caixa in caixas:
                button = ttk.Button(self.central_frame, text=caixa[1], command=lambda c=caixa: self.mostrar_itens(c[0]), style="TButton")
                button.pack(pady=10, ipadx=10, ipady=5, fill='x')
        else:
            ttk.Label(self.central_frame, text="Nenhuma caixa encontrada.", font=("Arial", 14)).pack(pady=20)

    def mostrar_itens(self, caixa_id):
        """Exibe os itens de uma caixa na coluna central."""
        self.history.append(lambda: self.mostrar_itens(caixa_id))
        for widget in self.central_frame.winfo_children():
            widget.destroy()

        itens = Item().listar_itens_por_caixa(caixa_id)
        print(f"Itens encontrados para a caixa {caixa_id}: {itens}")  # Adicionar mensagem de depuração
        if itens:
            for item in itens:
                ttk.Label(self.central_frame, text=f"{item[1]} (Quantidade: {item[2]}, Número de Série: {item[3]})").pack(pady=5)
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