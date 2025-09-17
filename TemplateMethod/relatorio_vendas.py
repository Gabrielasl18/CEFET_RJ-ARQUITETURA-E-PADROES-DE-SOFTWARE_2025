from relatorio import Relatorio

class RelatorioVendas(Relatorio):
    def carregar_dados(self):
        """Carrega os dados de vendas."""
        # Simulação de carregamento de dados
        return [
            {"produto": "Produto A", "quantidade": 10, "preco_unitario": 15.0},
            {"produto": "Produto B", "quantidade": 5, "preco_unitario": 25.0},
            {"produto": "Produto C", "quantidade": 8, "preco_unitario": 12.5},
        ]
    def processar_dados(self, dados):
        total_vendas = sum(item["quantidade"] * item["preco_unitario"] for item in dados)
        return {"total de vendas": total_vendas, "itens_vendidos": dados}
    
    def formatar_relatorio(self, dados_processados):
        relatorio = f"Relatório de Vendas\nTotal de Vendas: R$ {dados_processados['total de vendas']:.2f}\nItens Vendidos:\n"
        for item in dados_processados["itens_vendidos"]:
            relatorio += f"- {item['produto']}: {item['quantidade']} unidades a R$ {item['preco_unitario']:.2f} cada\n"
        return relatorio
