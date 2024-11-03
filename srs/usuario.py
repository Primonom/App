import sqlite3
from hashlib import sha256

class Usuario:
    def __init__(self, db_path="database.db"):
        self.db_path = db_path
        self.criar_tabela()

    def criar_tabela(self):
        """
        Cria a tabela de usuários no banco de dados caso ainda não exista.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def verificar_login(self, username, senha):
        conexao = sqlite3.connect('sistema_organizacao.db')
        cursor = conexao.cursor()
        
        # Verifica o usuário e a senha no banco
        cursor.execute("SELECT id FROM usuarios WHERE username = ? AND senha = ?", (username, senha))
        resultado = cursor.fetchone()
        
        conexao.close()
        
        if resultado:
            return resultado[0]  # Retorna o ID do usuário
        else:
            return None
        
    def adicionar_usuario(self, username, senha):
        """
        Adiciona um novo usuário ao banco de dados com username e senha criptografada.
        :param username: O nome de usuário a ser adicionado
        :param senha: A senha do usuário (será criptografada)
        """
        senha_hash = sha256(senha.encode()).hexdigest()  # Criptografa a senha com SHA-256

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO usuarios (username, senha) VALUES (?, ?)', (username, senha_hash))
            conn.commit()
            print(f"Usuário '{username}' adicionado com sucesso.")
        except sqlite3.IntegrityError:
            print("Erro: Username já existe.")
        finally:
            conn.close()

    def listar_usuarios(self):
        """
        Lista todos os usuários cadastrados no banco de dados (para debug e auditoria).
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, username FROM usuarios')
        usuarios = cursor.fetchall()
        conn.close()
        return usuarios

# Exemplo de uso para criar um usuário, apenas para testes.
if __name__ == "__main__":
    usuario = Usuario()
    usuario.adicionar_usuario("admin", "senha123")
    print("Usuário 'admin' criado com sucesso.")
