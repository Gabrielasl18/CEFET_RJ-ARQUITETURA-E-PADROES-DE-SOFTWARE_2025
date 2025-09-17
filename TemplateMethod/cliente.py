from relatorio_vendas import RelatorioVendas
from relatorio_despesas import RelatorioDespesas

class Cliente:
    def __init__(self, relatorios):
        self.relatorios = relatorios

    def gerar_relatorios(self):
        for relatorio in self.relatorios:
            print(f'---{relatorio.__class__.__name__}---')
            print(relatorio.gerar_relatorio())
            print("=" * 40)

def main():
    cliente = Cliente([RelatorioVendas(), RelatorioDespesas()])
    cliente.gerar_relatorios()

if __name__ == "__main__":
    main()