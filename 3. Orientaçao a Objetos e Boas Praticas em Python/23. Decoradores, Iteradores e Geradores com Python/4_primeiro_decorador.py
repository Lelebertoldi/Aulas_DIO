def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")

    return envelope


def ola_mundo():
    print("Olá mundo!")


# ola mundo recebe meu decorador, passo a funçao ola mundo para meu decorador e chamo ola mundo
ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

"""os decoradores em Python são usados para modificar o comportamento de funções ou métodos de
    maneira declarativa, permitindo executar código antes e depois da execução da função original.

    Um decorador é uma função que aceita outra função como argumento (a função que será decorada)
    e retorna uma nova função que geralmente envolve a função original para adicionar funcionalidade
    adicional. Essa funcionalidade adicional pode incluir a execução de código antes da função original
    ser chamada (pré-processamento) e/ou depois que a função original é chamada (pós-processamento).
    """



def meu_decorador(funcao):
    def funcao_decorada():
        print("Executando código antes da função original")
        funcao()  # Chamada da função original
        print("Executando código depois da função original")
    
    return funcao_decorada

@meu_decorador
def funcao_original():
    print("Função original executada")

# Chamada da função decorada
funcao_original()

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

"""






