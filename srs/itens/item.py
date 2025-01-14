import sqlite3
from base_model import BaseModel

class Item(BaseModel):
    def __init__(self):
        self.__conexao = sqlite3.connect('sistema_organizacao.db')
        self.__cursor = self.__conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS itens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                serial_number TEXT,
                caixa_id INTEGER,
                FOREIGN KEY (caixa_id) REFERENCES caixas (id)
            )
        ''')
        self.__conexao.commit()

    def adicionar(self, nome, quantidade, serial_number, caixa_id):
        self.__cursor.execute('INSERT INTO itens (nome, quantidade, serial_number, caixa_id) VALUES (?, ?, ?, ?)', (nome, quantidade, serial_number, caixa_id))
        self.__conexao.commit()

    def listar_todos(self):
        self.__cursor.execute('SELECT * FROM itens')
        return self.__cursor.fetchall()

    def listar_itens_por_caixa(self, caixa_id):
        self.__cursor.execute('SELECT * FROM itens WHERE caixa_id = ?', (caixa_id,))
        return self.__cursor.fetchall()

    def excluir(self, item_id):
        self.__cursor.execute('DELETE FROM itens WHERE id = ?', (item_id,))
        self.__conexao.commit()

    def __del__(self):
        self.__conexao.close()

    # Métodos públicos para acessar os atributos privados
    def get_conexao(self):
        return self.__conexao

    def get_cursor(self):
        return self.__cursor