import sqlite3

def inicializar_banco():
    # Conectar ao banco de dados
    conexao = sqlite3.connect('sistema_organizacao.db')
    cursor = conexao.cursor()

    # Criar tabelas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        senha TEXT
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS setores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS caixas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        setor_id INTEGER,
        FOREIGN KEY (setor_id) REFERENCES setores(id)
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS itens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        tipo TEXT,
        serial_number TEXT UNIQUE,
        caixa_id INTEGER,
        FOREIGN KEY (caixa_id) REFERENCES caixas(id)
    )
    ''')

    # Inserir usuários padrão
    inserir_usuarios_padrao(cursor)

    # Salvar (commit) as mudanças e fechar a conexão
    conexao.commit()
    conexao.close()

def inserir_usuarios_padrao(cursor):
    usuarios = [
        ('pablo', '1234'),
        ('gabriel', '1234'),
        ('luis', '1234')
    ]
    for username, senha in usuarios:
        try:
            cursor.execute("INSERT INTO usuarios (username, senha) VALUES (?, ?)", (username, senha))
        except sqlite3.IntegrityError:
            # Se o usuário já existir, ignore o erro
            print(f"O usuário '{username}' já existe.")

# Chama a função para inicializar o banco de dados se este arquivo for executado diretamente
if __name__ == "__main__":
    inicializar_banco()
