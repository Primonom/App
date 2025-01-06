from database import DatabaseModel

class Setor(DatabaseModel):
    table_name = 'setores'

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS setores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        ''')
        self.conexao.commit()

    def adicionar_setor(self, nome):
        self.salvar('INSERT INTO setores (nome) VALUES (?)', (nome,))

    def listar_setores(self):
        return self.listar_todos('SELECT * FROM setores')