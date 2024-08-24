class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod # transforma em metodo de classe, usa cls por convençao
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    # para caso em q precise ter acesso ao metodo da classe

    @staticmethod # funçao estatica, pode mudar
    def e_maior_idade(idade):
        return idade >= 18
    # para caso nao precise de contexto, nem classe, nem instancia do objeto


p = Pessoa.criar_de_data_nascimento(1988, 10, 14, "Letícia")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
