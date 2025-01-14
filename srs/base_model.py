from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def criar_tabela(self):
        pass

    @abstractmethod
    def adicionar(self, *args):
        pass

    @abstractmethod
    def listar_todos(self):
        pass

    @abstractmethod
    def excluir(self, id):
        pass