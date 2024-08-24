from abc import ABC, abstractmethod
from datetime import date

# Classe abstrata para representar uma transação
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

# Classe para representar um depósito
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor > 0:
            conta.saldo += self.valor
            conta.historico.adicionar_transacao(f"Depósito: R$ {self.valor:.2f}")
            return True
        return False

# Classe para representar um saque
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.saldo >= self.valor and conta.limite_saque() > 0:
            conta.saldo -= self.valor
            conta.numero_saques += 1
            conta.historico.adicionar_transacao(f"Saque: R$ {self.valor:.2f}")
            return True
        return False

# Classe para gerenciar o histórico de transações
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def exibir(self):
        print("\n========== EXTRATO ==========")
        if not self.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in self.transacoes:
                print(transacao)
        print("=============================\n")

# Classe para representar uma conta bancária
class Conta:
    def __init__(self, cliente, numero, agencia='0001'):
        self.cliente = cliente
        self.numero = numero
        self.agencia = agencia
        self.saldo = 0.0
        self.historico = Historico()
        self.numero_saques = 0

    def saldo(self):
        return self.saldo

    def nova_conta(cliente, numero):
        return Conta(cliente, numero)

    def sacar(self, valor):
        return Saque(valor).registrar(self)

    def depositar(self, valor):
        return Deposito(valor).registrar(self)

    def limite_saque(self):
        return 3 - self.numero_saques

# Classe para representar uma conta corrente, herda de Conta
class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia='0001', limite=500):
        super().__init__(cliente, numero, agencia)
        self.limite = limite

# Classe para representar uma pessoa física
class PessoaFisica:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf.replace(".", "").replace("-", "")
        self.nome = nome
        self.data_nascimento = data_nascimento

# Classe para representar um cliente do banco
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        if transacao.registrar(conta):
            print("Transação realizada com sucesso!")
        else:
            print("Falha na transação.")

    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Classe para gerenciar o banco
class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []
        self.numero_conta = 1

    def criar_cliente(self, nome, data_nascimento, cpf, endereco):
        cliente = Cliente(endereco)
        pessoa_fisica = PessoaFisica(cpf, nome, data_nascimento)
        cliente.pessoa_fisica = pessoa_fisica
        self.clientes.append(cliente)
        return cliente

    def criar_conta_corrente(self, cpf):
        cliente = next((c for c in self.clientes if c.pessoa_fisica.cpf == cpf), None)
        if not cliente:
            print("Cliente não encontrado!")
            return None

        conta = ContaCorrente(cliente, self.numero_conta)
        cliente.adicionar_conta(conta)
        self.contas.append(conta)
        self.numero_conta += 1
        return conta

    def verificar_dados(self, cpf):
        cliente = next((c for c in self.clientes if c.pessoa_fisica.cpf == cpf), None)
        if not cliente:
            print("Cliente não encontrado!")
            return

        pf = cliente.pessoa_fisica
        print(f"Nome: {pf.nome}")
        print(f"Data de Nascimento: {pf.data_nascimento}")
        print(f"CPF: {pf.cpf}")
        print(f"Endereço: {cliente.endereco}")
        print("Contas Correntes:")
        for conta in cliente.contas:
            print(f"Agência: {conta.agencia} | Número da Conta: {conta.numero} | Saldo: R$ {conta.saldo:.2f}")

# Loop principal para interagir com o usuário
banco = Banco()
usuario_logado = None
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta Corrente
[6] Verificar Dados
[7] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "1":
        if not usuario_logado:
            print("Operação não permitida! Crie um usuário e uma conta corrente primeiro.")
            continue
        valor = float(input("Informe o valor do depósito: "))
        conta = usuario_logado.contas[0]  # Assumindo que o usuário logado tem apenas uma conta
        usuario_logado.realizar_transacao(conta, Deposito(valor))

    elif opcao == "2":
        if not usuario_logado:
            print("Operação não permitida! Crie um usuário e uma conta corrente primeiro.")
            continue
        valor = float(input("Informe o valor que deseja sacar: "))
        conta = usuario_logado.contas[0]  # Assumindo que o usuário logado tem apenas uma conta
        usuario_logado.realizar_transacao(conta, Saque(valor))

    elif opcao == "3":
        if not usuario_logado:
            print("Operação não permitida! Crie um usuário e uma conta corrente primeiro.")
            continue
        conta = usuario_logado.contas[0]  # Assumindo que o usuário logado tem apenas uma conta
        conta.historico.exibir()

    elif opcao == "4":
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        cpf = input("CPF: ")
        endereco = input("Endereço (logradouro, número - bairro - cidade/estado): ")
        usuario_logado = banco.criar_cliente(nome, data_nascimento, cpf, endereco)

    elif opcao == "5":
        cpf = input("Informe o CPF do usuário para criar uma conta corrente: ")
        conta = banco.criar_conta_corrente(cpf)
        if conta:
            usuario_logado = next((c for c in banco.clientes if c.pessoa_fisica.cpf == cpf), None)

    elif opcao == "6":
        if not usuario_logado:
            print("Operação não permitida! Crie um usuário primeiro.")
            continue
        banco.verificar_dados(usuario_logado.pessoa_fisica.cpf)

    elif opcao == "7":
        print("Obrigado por usar nossos serviços, tenha um ótimo dia.")
        break

    else:
        print("Opção inválida, por favor selecione uma das opções.")
