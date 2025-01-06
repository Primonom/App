from database import DatabaseModel

class Caixa(DatabaseModel):
    table_name = 'caixas'

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS caixas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                setor_id INTEGER NOT NULL,
                FOREIGN KEY (setor_id) REFERENCES setores (id)
            )
        ''')
        self.conexao.commit()

    def adicionar_caixa(self, nome, setor_id):
        self.salvar('INSERT INTO caixas (nome, setor_id) VALUES (?, ?)', (nome, setor_id))

    def listar_caixas_com_setores(self, setor_id=None):
        if setor_id:
            return self.listar_todos('SELECT * FROM caixas WHERE setor_id = ?', (setor_id,))
        else:
            return self.listar_todos('SELECT * FROM caixas')