from pathlib import Path

ROOT_PATH = Path(__file__).parent

# with garante fechamento do arquivo mesmo com erro, de forma automatica
try:
    with open(ROOT_PATH / "1lorem.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")


# try:
#     with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
#         arquivo.write("Aprendendo a manipular arquivos utilizando Python.")
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo {exc}")


# Usar encoding="utf-8" garante que o Python interpretará corretamente o conteúdo do arquivo como texto codificado em UTF-8. Isso é especialmente importante para arquivos que contêm caracteres não ASCII, como acentos ou caracteres de outros alfabetos.
# Quando você especifica encoding="utf-8", você está dizendo ao Python para ler ou escrever o arquivo usando a codificação UTF-8. Isso é necessário para evitar erros de leitura ou escrita, especialmente se o arquivo contém caracteres especiais.
# em utf-8 existem acentos e em ascii nao existem
try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")
except UnicodeDecodeError as exc:
    print(exc)
