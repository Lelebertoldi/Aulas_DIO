def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        resultado = funcao(*args, **kwargs) # assim guarda o resultado
        print("faz algo depois de executar")
        return resultado
        # ou return funcao(*args, **kwargs)

    return envelope


@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")
    return nome.upper()


resultado = ola_mundo("João", 1000)
print(resultado)
print(ola_mundo)

"""
*args é usado para passar uma lista de argumentos
posicionais variáveis para uma função.

**kwargs é usado para passar um dicionário de 
argumentos nomeados variáveis para uma função.

voce pode colocar os argumentos da funçao como nome, idade, etc,
mas se quiser que fique mais generico pra caso aumente depois se usa args e kwargs.

o decorador pode decidir se retorna o valor da funçao decorada
ou nao. pro valor ser retornado a funçao 'envelope' deve retornar
o valor da funçao decorada


"""







