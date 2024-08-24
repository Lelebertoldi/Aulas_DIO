class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0 # para iniciar em zero

    def __iter__(self): # itera os numeros mensionados acima
        return self

    def __next__(self):
        try: # controle de excessao
            numero = self.numeros[self.contador]# variavel
            self.contador += 1 # contador +1, pula pro prox numero
            return numero * 2
        except IndexError: # excessao: quando termina a lista o contador fica maior q o numero e isso da erro, pq tenta entrar em looping infinito mas acabou os numeros ditados, esse index corta isso
            raise StopIteration # finaliza para nao ter looping infinito
            # se encontra index error é hora de parar

for i in MeuIterador(numeros=[38, 13, 11]):
    print(i)

"""
Iteradores e geradores permitem trabalhar com sequencias
de maneira eficiente. muito uteis pra casos de muitos dados 
a serem processados, para nao ter problemas de uso intensivo de memoria,
tempo de execussao, e ter um overflow.

iterador possui um numero contavel de valores q podem ser iterados
possui 2 metodos especiais: __iter__() e __next__()

economiza memoria evitando carregar todas as linhas do arquivo
tb itera linha a linha

"""






