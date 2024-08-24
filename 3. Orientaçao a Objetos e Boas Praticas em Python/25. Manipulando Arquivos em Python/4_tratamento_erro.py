from pathlib import Path

ROOT_PATH = Path(__file__).parent


try:
    arquivo = open(ROOT_PATH / "novo-diretorio" / "novo.txt", "r")
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    print(exc)
except IsADirectoryError as exc: # é um diretorio e nao um arquivo
    print(f"Não foi possível abrir o arquivo: {exc}")
except IOError as exc: # falta de memoria
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc: # nao tem permissoes
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")


# try:
#     arquivo = open(ROOT_PATH / "novo-diretorio")
# except IsADirectoryError as exc:
#     print(f"Não foi possível abrir o arquivo: {exc}")


'''
Usar exceções para lidar com erros é uma prática recomendada na programação, especialmente em operações que envolvem entrada e saída (I/O), como abrir arquivos, acessar recursos de rede ou interagir com o sistema de arquivos. 
'''