import sqlite3

class Item:
    def __init__(self, nome, quantidade, serial_number, caixa_id):
        self.nome = nome
        self.quantidade = quantidade
        self.serial_number = serial_number
        self.caixa_id = caixa_id
        self.conexao = sqlite3.connect('sistema_organizacao.db')
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS itens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                quantidade TEXT NOT NULL,
                serial_number TEXT NOT NULL,
                caixa_id INTEGER,
                FOREIGN KEY (caixa_id) REFERENCES caixas (id)
            )
        ''')
        self.conexao.commit()

    def salvar(self):
        self.cursor.execute('INSERT INTO itens (nome, quantidade, serial_number, caixa_id) VALUES (?, ?, ?, ?)', (self.nome, self.quantidade, self.serial_number, self.caixa_id))
        self.conexao.commit()

    @staticmethod
    def listar_todos_itens():
        conexao = sqlite3.connect('sistema_organizacao.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM itens')
        itens = cursor.fetchall()
        conexao.close()
        return itens

    def __del__(self):
        self.conexao.close()