import sqlite3

class Caixa:
    def __init__(self, db_path="database.db"):
        self.db_path = db_path
        self.criar_tabela_caixas()
        self.criar_tabela_itens()

    def criar_tabela_caixas(self):
            """
            Cria a tabela de caixas no banco de dados caso ainda não exista.
            """
            # Parte alterada no código #
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS caixas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL UNIQUE
                )
            ''')
            conn.commit()
            conn.close()

    def listar_caixas_com_setores(self):
        """
        Lista todas as caixas juntamente com o nome dos setores associados.
        :return: Lista de caixas com ID, nome da caixa e nome do setor.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        query = '''
            SELECT caixas.id, caixas.nome, setores.nome 
            FROM caixas 
            JOIN setores ON caixas.setor_id = setores.id
        '''
        cursor.execute(query)
        caixas = cursor.fetchall()
        conn.close()
        return caixas

    def criar_tabela_itens(self):
        """
        Cria a tabela de itens no banco de dados caso ainda não exista.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS itens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                caixa_id INTEGER,
                FOREIGN KEY(caixa_id) REFERENCES caixas(id)
            )
        ''')
        conn.commit()
        conn.close()

    def adicionar_caixa(self, nome, setor_id):
        """
        Adiciona uma nova caixa com o nome e setor fornecidos ao banco de dados.
        :param nome_caixa: Nome da caixa.
        :param setor_id: ID do setor ao qual a caixa pertence.

        """
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO caixas (nome, setor_id) VALUES (?, ?)', (nome, setor_id))
        conn.commit()
        conn.close()
        print(f"Caixa '{nome}' adicionada no setor ID '{setor_id}'.")

    
    def adicionar_item(self, nome_item, quantidade, nome_caixa):
        """
        Adiciona um novo item a uma caixa específica.
        :param nome_item: Nome do item a ser adicionado.
        :param quantidade: Quantidade do item.
        :param nome_caixa: Nome da caixa onde o item será armazenado.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM caixas WHERE nome = ?', (nome_caixa,))
        caixa_id = cursor.fetchone()

        if caixa_id:
            cursor.execute('INSERT INTO itens (nome, quantidade, caixa_id) VALUES (?, ?, ?)', 
                           (nome_item, quantidade, caixa_id[0]))
            conn.commit()
            print(f"Item '{nome_item}' (Quantidade: {quantidade}) adicionado à caixa '{nome_caixa}' com sucesso.")
        else:
            print(f"Erro: Caixa '{nome_caixa}' não encontrada.")
        conn.close()

    def remover_item(self, nome_item, nome_caixa):
        """
        Remove um item específico de uma caixa.
        :param nome_item: Nome do item a ser removido.
        :param nome_caixa: Nome da caixa onde o item está armazenado.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM caixas WHERE nome = ?', (nome_caixa,))
        caixa_id = cursor.fetchone()

        if caixa_id:
            cursor.execute('DELETE FROM itens WHERE nome = ? AND caixa_id = ?', (nome_item, caixa_id[0]))
            conn.commit()
            print(f"Item '{nome_item}' removido da caixa '{nome_caixa}' com sucesso.")
        else:
            print(f"Erro: Caixa '{nome_caixa}' não encontrada.")
        conn.close()

    def listar_caixas(self):
        """
        Lista todas as caixas disponíveis no banco de dados.
        :return: Lista de tuplas contendo as caixas (id, nome, setor_id).
        """
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT id, nome, setor_id FROM caixas')
            caixas = cursor.fetchall()
            return caixas
        except sqlite3.Error as e:
            print(f"Erro ao listar caixas: {e}")
            return []
        finally:
            conn.close()
    
    def listar_itens_por_caixa(self, nome_caixa):
        """
        Retorna uma lista de todos os itens armazenados em uma caixa específica.
        :param nome_caixa: Nome da caixa cujos itens serão listados.
        :return: Lista de tuplas contendo os itens (id, nome, quantidade) ou lista vazia se a caixa não existir.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM caixas WHERE nome = ?', (nome_caixa,))
        caixa_id = cursor.fetchone()

        if caixa_id:
            cursor.execute('SELECT id, nome, quantidade FROM itens WHERE caixa_id = ?', (caixa_id[0],))
            itens = cursor.fetchall()
            conn.close()
            return itens
        else:
            conn.close()
            print(f"Erro: Caixa '{nome_caixa}' não encontrada.")
            return []

    def atualizar_quantidade_item(self, nome_item, nome_caixa, nova_quantidade):
        """
        Atualiza a quantidade de um item específico em uma caixa.
        :param nome_item: Nome do item cuja quantidade será atualizada.
        :param nome_caixa: Nome da caixa onde o item está armazenado.
        :param nova_quantidade: Nova quantidade do item.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM caixas WHERE nome = ?', (nome_caixa,))
        caixa_id = cursor.fetchone()

        if caixa_id:
            cursor.execute('UPDATE itens SET quantidade = ? WHERE nome = ? AND caixa_id = ?', 
                           (nova_quantidade, nome_item, caixa_id[0]))
            conn.commit()
            print(f"Quantidade do item '{nome_item}' atualizada para {nova_quantidade} na caixa '{nome_caixa}'.")
        else:
            print(f"Erro: Caixa '{nome_caixa}' não encontrada.")
        conn.close()

# Exemplo de uso para adicionar e listar caixas e itens, apenas para testes.
if __name__ == "__main__":
    caixa = Caixa()
    
    caixa.adicionar_caixa("Ferramentas")
    caixa.adicionar_caixa("Documentos")
    caixas = caixa.listar_caixas()
    print("Caixas disponíveis:", caixas)
    
    caixa.adicionar_item("Parafuso", 100, "Ferramentas")
    caixa.atualizar_quantidade_item("Parafuso", "Ferramentas", 120)
    itens = caixa.listar_itens_por_caixa("Ferramentas")
    print("Itens na caixa 'Ferramentas':", itens)
