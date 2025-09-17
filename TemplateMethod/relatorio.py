from abc import ABC, abstractmethod

class Relatorio(ABC):
    def gerar_relatorio(self):
        """Template method definindo o esqueleto da geração de um relatorio."""
        dados = self.carregar_dados()
        dados_processados = self.processar_dados(dados)
        return self.formatar_relatorio(dados_processados)

        @abstractmethod
        def carregar_dados(self):
            """Método para carregar os dados necessários para o relatório."""
            pass

        @abstractmethod
        def processar_dados(self, dados):
            """Método para processar os dados carregados."""
            pass

        @abstractmethod
        def formatar_relatorio(self, dados_processados):
            """Método para formatar o relatório final."""
            pass
