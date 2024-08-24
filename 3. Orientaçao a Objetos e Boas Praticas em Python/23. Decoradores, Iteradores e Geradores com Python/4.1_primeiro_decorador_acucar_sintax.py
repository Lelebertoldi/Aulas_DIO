def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")

    return envelope


@meu_decorador
def ola_mundo():
    print("Olá mundo!")


ola_mundo()

"""Em Python, o símbolo @ é usado como uma forma conveniente de aplicar um
decorador a uma função. Quando você escreve @meu_decorador imediatamente antes
de uma função, como no exemplo:

@meu_decorador
def funcao_original():
    print("Função original executada")

Isso é equivalente a fazer:


def funcao_original():
    print("Função original executada")

funcao_original = meu_decorador(funcao_original)

isso é o açucar sintatico
"""



