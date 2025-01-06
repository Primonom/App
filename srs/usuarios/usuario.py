import logging
from database import DatabaseModel

# Configuração do logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Usuario(DatabaseModel):
    def __init__(self):
        super().__init__()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            )
        ''')
        self.conexao.commit()

    def adicionar_usuario(self, username, senha):
        try:
            self.cursor.execute('INSERT INTO usuarios (username, senha) VALUES (?, ?)', (username, senha))
            self.conexao.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def verificar_login(self, username, senha):
        logging.debug(f"Verificando login para username: {username}, senha: {senha}")
        self.cursor.execute('SELECT id FROM usuarios WHERE username = ? AND senha = ?', (username, senha))
        usuario = self.cursor.fetchone()
        logging.debug(f"Resultado da consulta: {usuario}")
        return usuario[0] if usuario else None