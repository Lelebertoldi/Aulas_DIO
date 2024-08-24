# Lembre-se de alterar o caminho do arquivo, para o caminho completo da sua máquina!
# local do arquivo + "r" para somente leitura, "w" para gravar e "a" para anexar, editar

arquivo = open(
    "E:/DIO/Python AI Backend Developer/3. Orientaçao a Objetos e Boas Praticas em Python/25. Manipulando Arquivos em Python/lorem.txt", "r"
)
print(arquivo.read()) # metodo read, ler arquivo todo de uma vez
arquivo.close()

arquivo = open(
    "E:/DIO/Python AI Backend Developer/3. Orientaçao a Objetos e Boas Praticas em Python/25. Manipulando Arquivos em Python/lorem.txt", "r"
)
print(arquivo.readline()) # lê uma linha por vez
arquivo.close()

arquivo = open(
    "E:/DIO/Python AI Backend Developer/3. Orientaçao a Objetos e Boas Praticas em Python/25. Manipulando Arquivos em Python/lorem.txt", "r"
)
print(arquivo.readlines()) # retorna uma lista onde cada elemento é uma linha do arquivo
arquivo.close()

arquivo = open(
    "E:/DIO/Python AI Backend Developer/3. Orientaçao a Objetos e Boas Praticas em Python/25. Manipulando Arquivos em Python/lorem.txt", "r"
)
# tip: percorre todas as linhas com codigo simples
while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()


