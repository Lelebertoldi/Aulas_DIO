def calculadora(operacao):
    def soma(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    match operacao: # similar a if
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div


op = calculadora("+") # dessa forma guarda em uma variavel
print(op(2, 2))
op = calculadora("-")
print(op(2, 2))
op = calculadora("*")
print(op(2, 2))
op = calculadora("/")
print(op(2, 2))

# tambem poderia ser:
print(calculadora("+")(3, 3))

# tambem podemos retornar funçoes de funçoes






