#sintaxe da herança:
# a classe filha herda as caranteristicas da classe mae
# a classe neta herda as caracteristicas da classe mae e vó e assim por diante
# estrutura de herança em que C é uma subclasse de B, que, por sua vez, é uma subclasse de A.

# herança simples: 

# classe mae/pai (base)
class A:
    pass

# classe filha
class B(A):
    pass

# classe neta
class C(B):
    pass


# tambem podem ter multiplas filhas:

# classe mae/pai (base)
class A:
    pass

# classe filha 1
class B(A):
    pass

# classe filha 2
class C(A):
    pass


    """
    Agora tanto a classe B quanto a classe C 
    são subtipos de A, herdando seus atributos
    e métodos. Essa estrutura permite que você
    tenha hierarquias de herança mais complexas,
    com múltiplas classes derivadas de uma única
    classe base.
    
    """

# herança multipla:
# quando uma filha herda de varias classes pai

# classe mae/pai (base)
class A:
    pass

# classe mae/pai (base)
class B:
    pass

# classe filha 
class C(A, B):
    pass

















     