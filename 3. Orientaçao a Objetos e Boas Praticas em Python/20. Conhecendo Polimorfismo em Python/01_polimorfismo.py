# polimorfismo é onde vc pode passar varios tipos de objetos e para cada objeto ele se comporta de uma maneira, ex: len


class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

# polimorfismo em herança
# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")
# objeto se comporta de formas diferentes chamando o mesmo nome, isso é polimorfismo


# chama metodo voar dentro de cada classe
def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
