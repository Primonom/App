import sqlite3

class Item:
    def __init__(self, nome, quantidade, caixa_id, db_path="database.db"):
        self.nome = nome
        self.quantidade = quantidade
        self.caixa_id = caixa_id
        self.db_path = db_path
        self.criar_tabela_itens()

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

    def salvar(self):
        """
        Salva o item no banco de dados.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO itens (nome, quantidade, caixa_id) VALUES (?, ?, ?)',
                       (self.nome, self.quantidade, self.caixa_id))
        conn.commit()
        conn.close()
        print(f"Item '{self.nome}' adicionado à caixa com ID '{self.caixa_id}'.")

    def atualizar_quantidade(self, nova_quantidade):
        """
        Atualiza a quantidade do item no banco de dados.
        :param nova_quantidade: Nova quantidade do item.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('UPDATE itens SET quantidade = ? WHERE nome = ? AND caixa_id = ?',
                       (nova_quantidade, self.nome, self.caixa_id))
        conn.commit()
        conn.close()
        print(f"Quantidade do item '{self.nome}' atualizada para {nova_quantidade}.")

    def remover(self):
        """
        Remove o item do banco de dados.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM itens WHERE nome = ? AND caixa_id = ?', (self.nome, self.caixa_id))
        conn.commit()
        conn.close()
        print(f"Item '{self.nome}' removido da caixa com ID '{self.caixa_id}'.")

    @staticmethod
    def listar_todos_itens(db_path="database.db"):
        """
        Lista todos os itens armazenados no banco de dados.
        :param db_path: Caminho para o banco de dados (default: "database.db")
        :return: Lista de itens com suas respectivas informações.
        """
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome, quantidade, caixa_id FROM itens')
        itens = cursor.fetchall()
        conn.close()
        return itens

    @staticmethod
    def listar_itens_por_caixa(caixa_id, db_path="database.db"):
        """
        Lista todos os itens de uma caixa específica.
        :param caixa_id: ID da caixa cujos itens serão listados.
        :return: Lista de itens e suas quantidades na caixa.
        """
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT nome, quantidade FROM itens WHERE caixa_id = ?', (caixa_id,))
        itens = cursor.fetchall()
        conn.close()
        return itens

# Exemplo de uso para testar a classe
if __name__ == "__main__":
    item1 = Item("Parafuso", 100, 1)
    item1.salvar()
    item1.atualizar_quantidade(150)
    print("Itens na caixa 1:", Item.listar_itens_por_caixa(1))
    item1.remover()
