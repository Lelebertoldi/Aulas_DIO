# classes
# self representa a instancia do objeto, padrao é self, mas pode ser usado this 
# diz uma caracteristica que o objeto tem
# def __init__ é metodo contrutor
# self. sao os atributos da classe
class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    # metodos sao funçoes dentro da classe, a diferença é que precisa chamar pelo menos argumento self
    def buzinar(self):
        print("Plim Plim...")
        
    def parar(self):
        print("Parando...")
        print("Bicicleta parada.")
        
    def correr(self):
        print("vrummm...")
    
    # funçoes tb podem ser usadas para acessar os atributos, mas tem q usar palavra diferente para nao dar erro
    # mas nao é pratica comum por atributos serem acessiveis, ex linha 52 (print(bic2.cor))
    def get_cor(self):
        return self.cor    
    
    # para poder ver os valores dentro de um objeto so chamando nome do objeto precisa definir __str__, para ficar legivel
    #def __str__(self):
        return f"Bicicleta: cor: {self.cor}, modelo: {self.modelo}, ano: {self.ano}, valor: {self.valor}"
    # ou fazer assim: (exibe nome da classe, mas se nome mudar nao preciso reescrever no return)
    # converte para dicionario os atributos da classe, sem precisar alterar caso haja alteracao na classe
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}"
        # join esta contatenando para formatar separacao dos dict com ', '
    
    
# parte para instanciar o objeto
bic1 = bicicleta('vermelha', 'caloi', 2022, 600)

bic2 = bicicleta('verde', 'monark', 2000, 500)

# chamar metodos

bic1.buzinar()
bic1.correr()
bic1.parar()
# sao equivalentes a chamar desa forma:
bicicleta.buzinar(bic2)
print(bic2.get_cor())
print(bic2.cor)


# tambem posso acessar atributos do objeto
print(bic1.cor, bic1.modelo, bic1.ano, bic1.valor)

# para exibir a instancia para ver os valores dentro de objeto precisa da configuraçao __str__ na linha 29-35
print(bic1) # output sem __str__ = <__main__.bicicleta object at 0x000001D31D6F6AB0>






