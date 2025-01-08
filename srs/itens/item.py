import sqlite3

class Item:
    def __init__(self, nome=None, quantidade=None, serial_number=None, caixa_id=None):
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
                quantidade INTEGER NOT NULL,
                serial_number TEXT NOT NULL,
                caixa_id INTEGER NOT NULL,
                FOREIGN KEY (caixa_id) REFERENCES caixas (id)
            )
        ''')
        self.conexao.commit()

    def excluir_tabela(self):
        self.cursor.execute('DROP TABLE IF EXISTS itens')
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

    @staticmethod
    def pesquisar_itens(query):
        conexao = sqlite3.connect('sistema_organizacao.db')
        cursor = conexao.cursor()
        cursor.execute('''
            SELECT itens.id, itens.nome, itens.quantidade, itens.serial_number, caixas.nome, setores.nome
            FROM itens
            JOIN caixas ON itens.caixa_id = caixas.id
            JOIN setores ON caixas.setor_id = setores.id
            WHERE itens.nome LIKE ? OR itens.serial_number LIKE ?
        ''', ('%' + query + '%', '%' + query + '%'))
        itens = cursor.fetchall()
        conexao.close()
        return itens

    def __del__(self):
        self.conexao.close()