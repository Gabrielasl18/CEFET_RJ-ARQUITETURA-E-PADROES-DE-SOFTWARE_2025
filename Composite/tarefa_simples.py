#Folha
from tarefa import Tarefa
class TarefaSimples(Tarefa):
    def concluir(self) -> bool:
        """Marca a tarefa como concluída."""
        self._concluida = True
        print(f"Tarefa '{self.nome}' concluída.")
        return True
    def desfazer_conclusao(self) -> bool:
        """Desfaz a conclusão da tarefa."""
        self._concluida = False
        print(f"Conclusão da tarefa '{self.nome}' desfeita.")
        return True
    def esta_concluida(self) -> bool:
        """Retorna True se a tarefa está concluída, False caso contrário."""
        return self._concluida
    def exibir(self, nivel: int = 0):
        """Exibe a tarefa e sua hierarquia."""
        prefixo = "  " * nivel
        status = "[X]" if self._concluida else "[ ]"
        print(f"{prefixo}{status} {self.nome}")