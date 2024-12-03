import sqlite3

class Caixa:
    def __init__(self):
        self.conexao = sqlite3.connect('sistema_organizacao.db')
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS caixas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                setor_id INTEGER NOT NULL,
                FOREIGN KEY (setor_id) REFERENCES setores (id)
            )
        ''')
        self.conexao.commit()

    def adicionar_caixa(self, nome, setor_id):
        self.cursor.execute('INSERT INTO caixas (nome, setor_id) VALUES (?, ?)', (nome, setor_id))
        self.conexao.commit()

    def listar_caixas_com_setores(self, setor_id=None):
        if setor_id:
            self.cursor.execute('SELECT * FROM caixas WHERE setor_id = ?', (setor_id,))
        else:
            self.cursor.execute('SELECT * FROM caixas')
        caixas = self.cursor.fetchall()
        return caixas

    def __del__(self):
        self.conexao.close()