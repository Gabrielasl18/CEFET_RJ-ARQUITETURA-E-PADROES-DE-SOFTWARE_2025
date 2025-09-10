from abc import ABC, abstractmethod
from products import Botao, Janela

class GUIFactory(ABC):
    @abstractmethod
    def criar_botao(self) -> Botao:
        pass
    
    @abstractmethod
    def criar_janela(self) -> Janela:
        pass