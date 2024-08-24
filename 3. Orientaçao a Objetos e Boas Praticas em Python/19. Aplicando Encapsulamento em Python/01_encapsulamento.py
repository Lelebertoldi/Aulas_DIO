# em python tudo é publico, usar encapsulamento, _ para subentender que é privado
class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo # _ antes do nome deixa subentendido que é privado, usar apenas no escopo da classe
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self): # metodo, usado para nao acessar o privado acima diretamente
        # ... para proteger, aqui coloca restriçoes para apenas dono da conta ter acesso a saldo
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
