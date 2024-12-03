import sqlite3
from datetime import datetime

class LogAcoes:
    def __init__(self):
        self.conexao = sqlite3.connect('sistema_organizacao.db')
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS log_acoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER,
                acao TEXT NOT NULL,
                descricao TEXT,
                data_hora TEXT NOT NULL,
                FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
            )
        ''')
        self.conexao.commit()

    def registrar_acao(self, usuario_id, acao, descricao):
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute('INSERT INTO log_acoes (usuario_id, acao, descricao, data_hora) VALUES (?, ?, ?, ?)', (usuario_id, acao, descricao, data_hora))
        self.conexao.commit()

    def listar_todas_acoes(self):
        self.cursor.execute('SELECT * FROM log_acoes')
        return self.cursor.fetchall()

    def __del__(self):
        self.conexao.close()