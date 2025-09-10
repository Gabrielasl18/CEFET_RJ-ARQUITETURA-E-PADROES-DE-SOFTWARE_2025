from abc import ABC, abstractmethod

class Botao(ABC):
    @abstractmethod
    def renderizar(self):
        pass

class Janela(ABC):
    @abstractmethod
    def exibir(self):
        pass

class BotaoWindows(Botao):
    def renderizar(self):
        return "Botão Windows - Estilo retangular com bordas quadradas"

class JanelaWindows(Janela):
    def exibir(self):
        return "Janela Windows - Barra de título azul com botões quadrados"

class BotaoMacOS(Botao):
    def renderizar(self):
        return "Botão MacOS - Estilo arredondado com gradiente suave"

class JanelaMacOS(Janela):
    def exibir(self):
        return "Janela MacOS - Barra de título cinza com botões coloridos redondos"

class BotaoUbuntu(Botao):
    def renderizar(self):
        return "Botão Ubuntu - Estilo laranja com bordas suaves"

class JanelaUbuntu(Janela):
    def exibir(self):
        return "Janela Ubuntu - Barra de título laranja com tema Ambiance"