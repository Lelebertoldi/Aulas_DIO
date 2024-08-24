def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2


for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)



"""
Iteradores e geradores permitem trabalhar com sequencias
de maneira eficiente. muito uteis pra casos de muitos dados 
a serem processados, para nao ter problemas de uso intensivo de memoria,
tempo de execussao, e ter um overflow.

geradores sao iteradores especiais que nao armazenam todos os 
seus valores na memoria.

economiza mt a memoria da maquina

ao invez de return utiliza yield

ex, em um banco de dados ele chama um unico usuario da lista
trabalhando de um em um usuario, e nao a lista toda de uma vez

o item é gerado, consumido e esquecido, nao pode mais ser acessado

a execussao de um gerador é pausada em yield e retomada dai na 
prox vez q ele for chamado

util para tarefas simples

"""