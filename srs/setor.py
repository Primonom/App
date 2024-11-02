import sqlite3

class Setor:
    def __init__(self, db_path="database.db"):
        self.db_path = db_path
        self.criar_tabela_setores()
        self.criar_tabela_caixas()

    def criar_tabela_setores(self):
        """
        Cria a tabela de setores no banco de dados caso ainda não exista.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS setores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE
            )
        ''')
        conn.commit()
        conn.close()

    def criar_tabela_caixas(self):
        """
        Cria a tabela de caixas no banco de dados caso ainda não exista.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS caixas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                setor_id INTEGER,
                FOREIGN KEY(setor_id) REFERENCES setores(id)
            )
        ''')
        conn.commit()
        conn.close()

    def adicionar_setor(self, nome):
        """
        Adiciona um novo setor ao banco de dados.
        :param nome: Nome do setor a ser adicionado.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO setores (nome) VALUES (?)', (nome,))
            conn.commit()
            print(f"Setor '{nome}' adicionado com sucesso.")
        except sqlite3.IntegrityError:
            print("Erro: Setor já existe.")
        finally:
            conn.close()

    def remover_setor(self, nome):
        """
        Remove um setor do banco de dados, juntamente com as caixas associadas.
        :param nome: Nome do setor a ser removido.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM caixas WHERE setor_id = (SELECT id FROM setores WHERE nome = ?)', (nome,))
        cursor.execute('DELETE FROM setores WHERE nome = ?', (nome,))
        conn.commit()
        conn.close()
        print(f"Setor '{nome}' e suas caixas foram removidos com sucesso.")

    def listar_setores(self):
        """
        Retorna uma lista de todos os setores cadastrados no banco de dados.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM setores')
        setores = cursor.fetchall()
        conn.close()
        return setores

    def adicionar_caixa(self, nome_caixa, nome_setor):
        """
        Adiciona uma nova caixa ao setor especificado.
        :param nome_caixa: Nome da caixa a ser adicionada.
        :param nome_setor: Nome do setor ao qual a caixa pertence.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM setores WHERE nome = ?', (nome_setor,))
        setor_id = cursor.fetchone()

        if setor_id:
            cursor.execute('INSERT INTO caixas (nome, setor_id) VALUES (?, ?)', (nome_caixa, setor_id[0]))
            conn.commit()
            print(f"Caixa '{nome_caixa}' adicionada ao setor '{nome_setor}' com sucesso.")
        else:
            print(f"Erro: Setor '{nome_setor}' não encontrado.")
        conn.close()

    def listar_caixas_por_setor(self, nome_setor):
        """
        Retorna uma lista de todas as caixas pertencentes a um setor específico.
        :param nome_setor: Nome do setor cujas caixas serão listadas.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM setores WHERE nome = ?', (nome_setor,))
        setor_id = cursor.fetchone()

        if setor_id:
            cursor.execute('SELECT * FROM caixas WHERE setor_id = ?', (setor_id[0],))
            caixas = cursor.fetchall()
            conn.close()
            return caixas
        else:
            conn.close()
            print(f"Erro: Setor '{nome_setor}' não encontrado.")
            return []

# Exemplo de uso para criar um setor e adicionar uma caixa, apenas para testes.
if __name__ == "__main__":
    setor = Setor()
    setor.adicionar_setor("Mecânica")
    setor.adicionar_caixa("Ferramentas", "Mecânica")
    print("Setor e caixa adicionados com sucesso.")
