# deixa codigo complexo e de dificil manutençao

class animal:
    def __init__(self, patas):
        self.patas = patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}"


# ao definir def __init__(self, patas, bico): da erro, por patas estar em ambos os pais (herdado de avo) ele entende como 2 argumentos
# nesse caso trocar argumento herdado por **kwargs e jogar pro final da lista e passar chave = valor na chamada do print
class mamifero(animal):
    def __init__(self, pelo, **patas):
        self.pelo = pelo
        super().__init__(**patas)



class cachorro(mamifero):
    pass

class gato(mamifero):
    pass

class leao(mamifero):
    pass


# ao definir def __init__(self, patas, bico): da erro, por patas estar em ambos os pais (herdado de avo) ele entende como 2 argumentos
# nesse caso trocar argumento herdado por **kwargs e jogar pro final da lista e passar chave = valor na chamada do print
class oviparo(animal):
    def __init__(self, bico, **patas):
        super().__init__(**patas)
        self.bico = bico



class ornitorrinco(mamifero, oviparo):
    pass


# por haver utilizaçao de **kwargs por conta da herança multipla, precisa definir chave = valor
gato = gato(patas=4, pelo="preto")
print(gato)


# por ser herança multipla passar chave = valor pro python saber de onde tirar cada caracteristica
ornitorrinco = ornitorrinco(patas=4, pelo="marrom", bico="laranja")
print(ornitorrinco)



# print(ornitorrinco.__mro__)
# print(ornitorrinco.mro())
# mro retorna a ordem que o python executa aquele comando, ordem que ele busca no codigo











