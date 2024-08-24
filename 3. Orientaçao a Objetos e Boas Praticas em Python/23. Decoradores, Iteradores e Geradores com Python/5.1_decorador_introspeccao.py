import functools # modulo de funçoes


def meu_decorador(funcao):
    @functools.wraps(funcao) # passa argumento pra ela pra manter nome da funçao e parametros para nao perder a capacidade de introspecçao
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)
    # @functools é um decorador dentro de um decorador
    return envelope


@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")


print(ola_mundo.__name__)
