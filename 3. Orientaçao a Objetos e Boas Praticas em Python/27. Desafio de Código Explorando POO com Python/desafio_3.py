import sys

class Plano:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    @property
    def saldo(self):
        return self.__saldo

    def custo_chamada(self, duracao):
        return duracao * 0.10

    def deduzir_saldo(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        return False

class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    @property
    def nome(self):
        return self.__nome

    @property
    def numero(self):
        return self.__numero

    @property
    def plano(self):
        return self.__plano

    def fazer_chamada(self, destinatario, duracao):
        custo = self.plano.custo_chamada(duracao)
        if self.plano.deduzir_saldo(custo):
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self.plano.saldo:.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))

# Recebendo as informações do usuário:
nome = sys.stdin.readline().strip()
numero = sys.stdin.readline().strip()
saldo_inicial = float(sys.stdin.readline().strip())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = sys.stdin.readline().strip()
duracao = int(sys.stdin.readline().strip())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
