class Foo:
    def __init__(self, x=None): # se nao for passado valor é none
        self._x = x

    @property # decorador, funçao q executa antes da sua funçao, acessa x com sintaxe de atributo
    def x(self):
        return self._x or 0

    @x.setter # para poder setar atributo x, nao é metodo
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0 # da o valor de zero sem excluir
        # para excluir : del self._x , mas nesse caso pode dar mau funcionamento


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)

# para reornar valor de atributo (nao objeto) precisa do @property
# para alterar esse valor precisa do @x.setter, fazer atribuiçao para a propriedade
# para poder deletar um atributo precisa do @x.deleter


