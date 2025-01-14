import sqlite3
from base_model import BaseModel

class Caixa(BaseModel):
    def __init__(self):
        self.__conexao = sqlite3.connect('sistema_organizacao.db')
        self.__cursor = self.__conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS caixas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                setor_id INTEGER,
                FOREIGN KEY (setor_id) REFERENCES setores (id)
            )
        ''')
        self.__conexao.commit()

    def adicionar(self, nome, setor_id):
        self.__cursor.execute('INSERT INTO caixas (nome, setor_id) VALUES (?, ?)', (nome, setor_id))
        self.__conexao.commit()

    def listar_todos(self):
        self.__cursor.execute('SELECT * FROM caixas')
        return self.__cursor.fetchall()

    def listar_caixas_por_setor(self, setor_id):
        self.__cursor.execute('SELECT * FROM caixas WHERE setor_id = ?', (setor_id,))
        return self.__cursor.fetchall()

    def excluir(self, caixa_id):
        self.__cursor.execute('DELETE FROM caixas WHERE id = ?', (caixa_id,))
        self.__conexao.commit()

    def __del__(self):
        self.__conexao.close()

    # Métodos públicos para acessar os atributos privados
    def get_conexao(self):
        return self.__conexao

    def get_cursor(self):
        return self.__cursor