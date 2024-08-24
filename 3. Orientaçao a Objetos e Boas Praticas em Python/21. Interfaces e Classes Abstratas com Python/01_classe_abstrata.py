# interface define o q uma classe deve fazer, e nao como
# interface é criada com classes abstratas
# em python nao fornece classe abstrata (ABC - abstract method class)
# modulo ABC em python decora metodos da classe base como abstratos e registra classes concretascomo implementaçao da base abstrata
# um metodo se torna abstrato com @abstractmethod

# importa do modulo a classe abc
from abc import ABC, abstractmethod, abstractproperty

# todas as classes filhas sao obrigadas a implementar os metodos da classe
# classe abstrata nao pode ser instanciada diretamente
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self): # metodo passa a ser obrigatorio da classe pai pra filha
        pass

    @abstractmethod
    def desligar(self): # metodo passa a ser obrigatorio da classe pai pra filha
        pass

    @property # tambem pode forçar a propriedade para as filhas
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self): # metodo passa a ser obrigatorio da classe pai pra filha
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self): # metodo passa a ser obrigatorio da classe pai pra filha
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
