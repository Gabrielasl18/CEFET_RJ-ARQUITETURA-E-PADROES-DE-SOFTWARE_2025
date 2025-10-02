#Component
from abc import ABC, abstractmethod
class Tarefa(ABC):
    """Classe abstrata que define a interface para tarefas."""
    def __init__(self, nome: str):
        self.nome = nome
        self._concluida = False
    @abstractmethod
    def concluir(self):
        """Marca a tarefa como concluída."""
        pass
    @abstractmethod
    def desfazer_conclusao(self):
        """Desfaz a conclusão da tarefa."""
        pass
    @abstractmethod
    def esta_concluida(self) -> bool:
        """Retorna True se a tarefa está concluída, False caso contrário."""
        return self._concluida
    @abstractmethod
    def exibir(self, nivel: int = 0):
        """Exibe a tarefa e sua hierarquia."""
        pass
    def adicionar(self, tarefa: 'Tarefa'):
        """Adiciona uma sub-tarefa. Deve ser implementado por classes compostas."""
        raise NotImplementedError("Esta tarefa não suporta sub-tarefas.")
    def remover(self, tarefa: 'Tarefa') -> None:
        """Remove uma sub-tarefa. Deve ser implementado por classes compostas."""
        raise NotImplementedError("Esta tarefa não suporta sub-tarefas.")