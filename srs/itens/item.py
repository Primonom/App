from database import DatabaseModel

class Item(DatabaseModel):
    table_name = 'itens'

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

    def adicionar_item(self, nome, quantidade, serial_number, caixa_id):
        self.salvar('INSERT INTO itens (nome, quantidade, serial_number, caixa_id) VALUES (?, ?, ?, ?)', (nome, quantidade, serial_number, caixa_id))

    def listar_itens(self, caixa_id=None):
        if caixa_id:
            return self.listar_todos('SELECT * FROM itens WHERE caixa_id = ?', (caixa_id,))
        else:
            return self.listar_todos('SELECT * FROM itens')