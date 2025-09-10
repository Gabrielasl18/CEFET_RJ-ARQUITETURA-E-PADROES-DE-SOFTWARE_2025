from concret_factory import WindowsFactory, MacOSFactory, UbuntuFactory

class Aplicacao:
    def __init__(self, factory):
        self.factory = factory
        self.botao = None
        self.janela = None
    
    def criar_interface(self):
        self.botao = self.factory.criar_botao()
        self.janela = self.factory.criar_janela()
    
    def exibir_interface(self):
        print("=== Interface Criada ===")
        print(f"Botão: {self.botao.renderizar()}")
        print(f"Janela: {self.janela.exibir()}")
        print("=" * 30)

def main():
    print("Sistema de Interface Gráfica Multiplataforma")
    print("=" * 50)
    
    print("\n1. Criando interface para Windows:")
    app_windows = Aplicacao(WindowsFactory())
    app_windows.criar_interface()
    app_windows.exibir_interface()
    
    print("\n2. Criando interface para MacOS:")
    app_macos = Aplicacao(MacOSFactory())
    app_macos.criar_interface()
    app_macos.exibir_interface()
    
    print("\n3. Criando interface para Ubuntu:")
    app_ubuntu = Aplicacao(UbuntuFactory())
    app_ubuntu.criar_interface()
    app_ubuntu.exibir_interface()
    
    print("\n4. Demonstração de troca dinâmica:")
    sistemas = [WindowsFactory(), MacOSFactory(), UbuntuFactory()]
    nomes = ["Windows", "MacOS", "Ubuntu"]
    
    for i, (factory, nome) in enumerate(zip(sistemas, nomes), 1):
        print(f"\n   {i}. Alternando para {nome}:")
        app = Aplicacao(factory)
        app.criar_interface()
        app.exibir_interface()

if __name__ == "__main__":
    main()