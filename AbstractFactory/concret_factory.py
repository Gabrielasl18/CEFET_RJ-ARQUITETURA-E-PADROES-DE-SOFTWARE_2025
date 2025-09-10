from abstract_factory import GUIFactory
from products import BotaoWindows, JanelaWindows, BotaoMacOS, JanelaMacOS, BotaoUbuntu, JanelaUbuntu

class WindowsFactory(GUIFactory):
    def criar_botao(self) -> BotaoWindows:
        return BotaoWindows()
    
    def criar_janela(self) -> JanelaWindows:
        return JanelaWindows()

class MacOSFactory(GUIFactory):
    def criar_botao(self) -> BotaoMacOS:
        return BotaoMacOS()
    
    def criar_janela(self) -> JanelaMacOS:
        return JanelaMacOS()

class UbuntuFactory(GUIFactory):
    def criar_botao(self) -> BotaoUbuntu:
        return BotaoUbuntu()
    
    def criar_janela(self) -> JanelaUbuntu:
        return JanelaUbuntu()