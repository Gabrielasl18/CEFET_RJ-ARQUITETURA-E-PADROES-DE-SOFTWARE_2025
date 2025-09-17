from relatorio import Relatorio
class RelatorioDespesas(Relatorio):
    def carregar_dados(self):
        """Carrega os dados de despesas."""
        # Simulação de carregamento de dados
        return [
            {"categoria": "Aluguel", "valor": 1200.0},
            {"categoria": "Salários", "valor": 3000.0},
            {"categoria": "Marketing", "valor": 800.0},
        ]

    def processar_dados(self, dados):
        total_despesas = sum(item["valor"] for item in dados)
        return {"total de despesas": total_despesas, "itens_despesa": dados}

    def formatar_relatorio(self, dados_processados):
        relatorio = f"Relatório de Despesas\nTotal de Despesas: R$ {dados_processados['total de despesas']:.2f}\nItens de Despesa:\n"
        for item in dados_processados["itens_despesa"]:
            relatorio += f"- {item['categoria']}: R$ {item['valor']:.2f}\n"
        return relatorio