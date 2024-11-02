import sqlite3
from datetime import datetime

class LogAcoes:
    def __init__(self, db_path="database.db"):
        self.db_path = db_path
        self.criar_tabela_log()

    def criar_tabela_log(self):
        """
        Cria a tabela de log no banco de dados caso ainda não exista.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS log_acoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER,
                acao TEXT NOT NULL,
                descricao TEXT,
                data_hora TEXT NOT NULL,
                FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
            )
        ''')
        conn.commit()
        conn.close()

    def registrar_acao(self, usuario_id, acao, descricao=""):
        """
        Registra uma ação no log.
        :param usuario_id: ID do usuário que realizou a ação.
        :param acao: Tipo de ação (ex: 'adicionar', 'remover', 'atualizar').
        :param descricao: Descrição adicional sobre a ação.
        """
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO log_acoes (usuario_id, acao, descricao, data_hora)
            VALUES (?, ?, ?, ?)
        ''', (usuario_id, acao, descricao, data_hora))
        conn.commit()
        conn.close()
        print(f"Ação '{acao}' registrada com sucesso para o usuário ID {usuario_id}.")

    def listar_acoes_por_usuario(self, usuario_id):
        """
        Lista todas as ações realizadas por um usuário específico.
        :param usuario_id: ID do usuário cujas ações serão listadas.
        :return: Lista de ações do usuário.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT acao, descricao, data_hora FROM log_acoes WHERE usuario_id = ?', (usuario_id,))
        acoes = cursor.fetchall()
        conn.close()
        return acoes

    def listar_todas_acoes(self):
        """
        Lista todas as ações registradas no log.
        :return: Lista de todas as ações.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT usuario_id, acao, descricao, data_hora FROM log_acoes')
        acoes = cursor.fetchall()
        conn.close()
        return acoes

# Exemplo de uso para testar a classe
if __name__ == "__main__":
    log = LogAcoes()
    log.registrar_acao(usuario_id=1, acao="adicionar", descricao="Adicionado item Parafuso à caixa Ferramentas")
    log.registrar_acao(usuario_id=1, acao="atualizar", descricao="Atualizada quantidade do item Parafuso para 150")
    acoes_usuario = log.listar_acoes_por_usuario(1)
    print("Ações do usuário 1:", acoes_usuario)
    todas_acoes = log.listar_todas_acoes()
    print("Todas as ações registradas:", todas_acoes)
