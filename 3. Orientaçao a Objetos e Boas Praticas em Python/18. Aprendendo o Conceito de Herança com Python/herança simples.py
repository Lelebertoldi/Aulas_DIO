

class veiculo:
    def __init__(self, cor, placa, rodas):
        self.cor = cor 
        self.placa = placa 
        self.rodas = rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__ (self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}"


class motocicleta(veiculo):
    pass



class carro(veiculo):
    pass



# init na filha sobrescreve init da classe pai
# nesse caso para chamar a caracteristica da classe pai usar super() + caracteristica
class caminhao(veiculo):
    def __init__(self, cor, placa, rodas, carregado):
        super().__init__(cor, placa, rodas) # chama da classe pai
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{"Sim" if self.carregado else "Não"} estou carregado!")



moto = motocicleta("preta", "abc-1234", 2)
moto.ligar_motor()

carro = carro('branco', 'xde-3456', 4)
carro.ligar_motor()

caminhao = caminhao('roxo', 'gfd-6787', 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()


print(caminhao)
print(carro)
print(moto)










