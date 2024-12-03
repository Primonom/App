import sqlite3

class Usuario:
    def __init__(self):
        self.conexao = sqlite3.connect('sistema_organizacao.db')
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            )
        ''')
        self.conexao.commit()

    def verificar_login(self, username, senha):
        self.cursor.execute('SELECT id FROM usuarios WHERE username = ? AND senha = ?', (username, senha))
        usuario = self.cursor.fetchone()
        return usuario[0] if usuario else None

    def adicionar_usuario(self, username, senha):
        try:
            self.cursor.execute('INSERT INTO usuarios (username, senha) VALUES (?, ?)', (username, senha))
            self.conexao.commit()
        except sqlite3.IntegrityError:
            return False
        return True

    def __del__(self):
        self.conexao.close()