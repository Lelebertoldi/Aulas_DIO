def mensagem(nome):
    print("executando mensagem")
    return f"Oi {nome}"


def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Olá tudo bem com você {nome}?"


def executar(funcao, nome):
    print("executando executar")
    return funcao(nome)


print(executar(mensagem, "Joao"))
print(executar(mensagem_longa, "Joao"))

# funçoes sao objetos de primeira classe qdo faz uma "salada" desses objetos
# posso passar uma funçao para outras funçoes e usar essa funçao como retorno de valor
# posso passar uma funçao com argumento de outra funçao, e inclusive usar so como referencia para outra funçao






