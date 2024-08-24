def principal():
    print("executando a funcao principal") # executa primeiro por ser pai

    def funcao_interna():
        print("executando a funcao interna")

    def funcao_2():
        print("executando a funcao 2")

    funcao_interna() # executa funçao interna dentro da funçao
    funcao_2() # executa funçao interna dentro da funçao


principal() # chama a funçao e executa as funçoes internas

# define uma funcao dentro de outra funçao
# inner functions
# funçoes podem ser cascateadas dentro de funçoes, tendo netas, bisnetas, etc, mas deixa o codigo complicado






