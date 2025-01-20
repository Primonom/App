import sqlite3
from base_model import BaseModel

class Usuario(BaseModel):
    def __init__(self):
        self.__conexao = sqlite3.connect('sistema_organizacao.db')
        self.__cursor = self.__conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            )
        ''')
        self.__conexao.commit()

    def criar(self, username, senha):
        try:
            self.__cursor.execute('INSERT INTO usuarios (username, senha) VALUES (?, ?)', (username, senha))
            self.__conexao.commit()
            print(f"Usuário criado: {username}")
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")

    def verificar_login(self, username, senha):
        try:
            self.__cursor.execute('SELECT id FROM usuarios WHERE username = ? AND senha = ?', (username, senha))
            usuario = self.__cursor.fetchone()
            if usuario:
                return usuario[0]
            else:
                return None
        except Exception as e:
            print(f"Erro ao verificar login: {e}")
            return None

    def listar_todos(self):
        self.__cursor.execute('SELECT * FROM usuarios')
        return self.__cursor.fetchall()

    def excluir(self, usuario_id):
        self.__cursor.execute('DELETE FROM usuarios WHERE id = ?', (usuario_id,))
        self.__conexao.commit()

    def adicionar(self, *args, **kwargs):
        pass  # Implementação vazia para satisfazer o método abstrato

    def __del__(self):
        self.__conexao.close()

    # Métodos públicos para acessar os atributos privados
    def get_conexao(self):
        return self.__conexao

    def get_cursor(self):
        return self.__cursor