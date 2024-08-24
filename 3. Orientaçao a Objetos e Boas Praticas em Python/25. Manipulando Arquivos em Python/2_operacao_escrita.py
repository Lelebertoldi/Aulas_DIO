arquivo = open(
    "E:/DIO/Python AI Backend Developer/3. Orientaçao a Objetos e Boas Praticas em Python/25. Manipulando Arquivos em Python/teste.txt", "w"
)
arquivo.write("Escrevendo dados em um novo arquivo.") # escreve um unico dado
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto", "\n", "Letícia"]) # escreve linhas
arquivo.close()


'''
Para adicionar linhas a um arquivo existente sem alterar as linhas já escritas, você deve abrir o arquivo no modo de adição ('a' ou 'a+'). Aqui está um exemplo de como fazer isso:

Abrir o Arquivo no Modo de Adição:

O modo 'a' abre o arquivo para escrita e o coloca no final do arquivo. Se o arquivo não existir, ele será criado.
O modo 'a+' abre o arquivo para leitura e escrita, colocando o ponteiro no final do arquivo. Se o arquivo não existir, ele será criado.
Adicionar Linhas ao Arquivo:

Para adicionar linhas ao arquivo, você pode usar o método write ou writelines.
Exemplo de Uso
python
Copy code
from pathlib import Path

# Define o caminho para o arquivo
ROOT_PATH = Path.cwd()
caminho_arquivo = ROOT_PATH / "arquivo-utf-8.txt"

# Adiciona linhas ao arquivo sem alterar as linhas existentes
with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
    arquivo.write("\nEsta é uma nova linha adicionada ao arquivo.")
    arquivo.write("\nOutra linha adicionada ao arquivo.")

print(f'Linhas adicionadas ao arquivo {caminho_arquivo}.')
Análise do Código
Abrir no Modo de Adição:

with open(caminho_arquivo, "a", encoding="utf-8") as arquivo: abre o arquivo no modo de adição com codificação UTF-8. O ponteiro é colocado no final do arquivo para que novas linhas sejam adicionadas após as linhas existentes.
Adicionar Linhas:

arquivo.write("\nEsta é uma nova linha adicionada ao arquivo.") escreve uma nova linha no final do arquivo. Note que o \n no início da string garante que a nova linha será adicionada em uma nova linha.
Exemplo com writelines
Se você quiser adicionar múltiplas linhas de uma vez, pode usar writelines:

python
Copy code
linhas_para_adicionar = [
    "\nPrimeira linha adicionada.",
    "\nSegunda linha adicionada.",
    "\nTerceira linha adicionada."
]

# Adiciona múltiplas linhas ao arquivo
with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
    arquivo.writelines(linhas_para_adicionar)

print(f'Múltiplas linhas adicionadas ao arquivo {caminho_arquivo}.')
'''













