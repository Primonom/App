import sqlite3

class Setor:
    def __init__(self):
        self.conexao = sqlite3.connect('sistema_organizacao.db')
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS setores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        ''')
        self.conexao.commit()

    def adicionar_setor(self, nome):
        self.cursor.execute('INSERT INTO setores (nome) VALUES (?)', (nome,))
        self.conexao.commit()

    def listar_setores(self):
        self.cursor.execute('SELECT * FROM setores')
        setores = self.cursor.fetchall()
        return setores

    def __del__(self):
        self.conexao.close()