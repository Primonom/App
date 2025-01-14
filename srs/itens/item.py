import sqlite3

class Item:
    def __init__(self):
        self.conexao = sqlite3.connect('sistema_organizacao.db')
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS itens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                serial_number TEXT,
                caixa_id INTEGER,
                FOREIGN KEY (caixa_id) REFERENCES caixas (id)
            )
        ''')
        self.conexao.commit()

    def adicionar_item(self, nome, quantidade, serial_number, caixa_id):
        self.cursor.execute('INSERT INTO itens (nome, quantidade, serial_number, caixa_id) VALUES (?, ?, ?, ?)', (nome, quantidade, serial_number, caixa_id))
        self.conexao.commit()

    def listar_itens_por_caixa(self, caixa_id):
        self.cursor.execute('SELECT * FROM itens WHERE caixa_id = ?', (caixa_id,))
        return self.cursor.fetchall()

    def listar_todos_itens(self):
        self.cursor.execute('SELECT * FROM itens')
        return self.cursor.fetchall()

    def excluir_item(self, item_id):
        self.cursor.execute('DELETE FROM itens WHERE id = ?', (item_id,))
        self.conexao.commit()

    def __del__(self):
        self.conexao.close()