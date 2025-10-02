#Composite
from tarefa import Tarefa
from typing import List
class TarefaComposta(Tarefa):
    """Representa uma tarefa composta que pode conter sub-tarefas."""

    def __init__(self, nome: str):
        super().__init__(nome)
        self.subtarefas: List[Tarefa] = []

    def adicionar(self, tarefa: Tarefa):
        self.subtarefas.append(tarefa)
        print(f"Sub-tarefa '{tarefa.nome}' adicionada à tarefa composta '{self.nome}'.")

    def remover(self, tarefa: Tarefa):
        self.subtarefas.remove(tarefa)
        print(f"Sub-tarefa '{tarefa.nome}' removida da tarefa composta '{self.nome}'.")
    
    def concluir(self) -> bool:
      
      if not self.subtarefas:
          self._concluida = True
          print(f"Tarefa '{self.nome}' concluída!")
          return True
      todas_concluidas = all(tarefa.esta_concluida() for tarefa in self.subtarefas)
      if todas_concluidas:
          self._concluida = True
          print(f"Tarefa composta '{self.nome}' concluída!")
          return True
      else:
          print(f"Não é possível concluir a tarefa composta '{self.nome}': há sub-tarefas não concluídas.")
          return False
      
    def desfazer_conclusao(self) -> bool:
        self._concluida = False
        print(f"Conclusão da tarefa composta '{self.nome}' desfeita.")
    
    def esta_concluida(self) -> bool:
        if not self.subtarefas:
            return self._concluida
        return self._concluida and all(tarefa.esta_concluida() for tarefa in self.subtarefas)
    
    def exibir(self, nivel: int = 0) -> None:
        prefixo = "  " * nivel
        status = "[X]" if self.esta_concluida() else "[ ]"
        print(f"{prefixo}{status} {self.nome}")
        for subtarefa in self.subtarefas:
            subtarefa.exibir(nivel + 1)