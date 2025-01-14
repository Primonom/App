import sqlite3
from base_model import BaseModel

class Setor(BaseModel):
    def __init__(self, __conexao=None, __cursor=None):
        self.__conexao = sqlite3.connect('sistema_organizacao.db')
        self.__cursor = self.__conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS setores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        ''')
        self.__conexao.commit()

    def adicionar(self, nome):
        self.__cursor.execute('INSERT INTO setores (nome) VALUES (?)', (nome,))
        self.__conexao.commit()

    def listar_todos(self):
        self.__cursor.execute('SELECT * FROM setores')
        return self.__cursor.fetchall()

    def excluir(self, setor_id):
        self.__cursor.execute('DELETE FROM setores WHERE id = ?', (setor_id,))
        self.__conexao.commit()

    def __del__(self):
        self.__conexao.close()

    # Métodos públicos para acessar os atributos privados
    def get_conexao(self):
        return self.__conexao

    def get_cursor(self):
        return self.__cursor