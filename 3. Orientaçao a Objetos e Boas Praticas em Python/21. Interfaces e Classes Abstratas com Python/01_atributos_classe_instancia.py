class Estudante: # classe
    escola = "DIO"
    # nome do atributo = atribuiçao

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

# instanciando 2 alunos
# variaveis que armazenam as instancias dos estudantes
aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

# troca da variavel da classe: classe.atributo = troca
# poderia ser aluno_1.escola para alterar apenas o estudante 1, ou estudante.escola para mudar em todos os estudantes
Estudante.escola = "Python"
aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)
