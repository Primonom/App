import sqlite3
from abc import ABC, abstractmethod

class DatabaseModel(ABC):
    def __init__(self):
        self.conexao = sqlite3.connect('sistema_organizacao.db')
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    @abstractmethod
    def criar_tabela(self):
        pass

    def excluir_tabela(self):
        self.cursor.execute(f'DROP TABLE IF EXISTS {self.table_name}')
        self.conexao.commit()

    def salvar(self, query, params):
        self.cursor.execute(query, params)
        self.conexao.commit()

    def listar_todos(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def __del__(self):
        self.conexao.close()