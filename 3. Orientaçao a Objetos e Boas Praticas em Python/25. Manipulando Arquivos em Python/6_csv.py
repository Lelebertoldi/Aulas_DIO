import csv
from pathlib import Path


# arquivo csv é excel


ROOT_PATH = Path(__file__).parent

# marca coluna para forma de leitura dicionario
COLUNA_ID = 0
COLUNA_NOME = 1


# O comando try em Python é usado para definir um bloco de código onde você suspeita que possa ocorrer uma exceção (um erro). Este bloco é seguido por um ou mais blocos except que especificam como lidar com exceções que podem ser geradas durante a execução do código dentro do bloco try.
# no csv os comandos sao diferentes
'''
Sem especificar newline="", o comportamento padrão em sistemas Windows pode adicionar linhas em branco extras entre as linhas escritas. Isso ocorre porque o modo como o Python lida com novas linhas ('\n') e a forma como o sistema operacional Windows lida com novas linhas ('\r\n') podem conflitar.

Especialmente ao trabalhar com arquivos CSV, onde a formatação correta das linhas é crucial para serem interpretadas corretamente por outros softwares (como Excel), a presença de linhas em branco extras pode causar problemas de formatação.
'''
try:
    with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome"])
        escritor.writerow(["1", "Maria"])
        escritor.writerow(["2", "João"])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")


try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for idx, row in enumerate(leitor):
            if idx == 0:
                continue
            print(f"ID: {row[COLUNA_ID]}")
            print(f"Nome: {row[COLUNA_NOME]}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")


try:
    with open(ROOT_PATH / "usuarios.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile) # lê como dicionario
        print(reader.fieldnames) # printa cabeçalho
        for row in reader:
            print(f"ID: {row['id']}")
            print(f"Nome: {row['nome']}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")



'''
Funcionamento do try-except:
try: O bloco try contém o código que você quer executar. É neste bloco que você coloca operações que podem potencialmente gerar uma exceção.

except: Se uma exceção ocorrer dentro do bloco try, o fluxo do programa será interrompido e a execução passará para o primeiro bloco except que corresponde ao tipo de exceção gerada.


Uso de try-except-else-finally:
Além do bloco try e except, você pode usar outros blocos opcionais com try:

else: É executado se nenhum erro ocorrer no bloco try. É útil para código que deve ser executado apenas se não houver exceções.

finally: É sempre executado, independentemente de uma exceção ter ocorrido ou não. É usado para limpeza de recursos, como fechar arquivos ou liberar conexões de rede.
'''
