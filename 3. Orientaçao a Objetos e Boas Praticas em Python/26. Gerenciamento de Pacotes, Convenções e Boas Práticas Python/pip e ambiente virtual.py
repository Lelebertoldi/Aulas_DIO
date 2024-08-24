# pip - ferramenta muito pobre

# site para ver os pacotes pip: https://pypi.org/ ou https://pypi.org/search/
# pip instal + pacote
# pip uninstall + pacote
# pip list - lista todos os pacotes instalados
# pip - traz todos os comandos dentro do pip
# pip instal --upgrade + pacote - atualiza pacote
# ls - lista os arquivos


# ambiente virtual

# criar ambiente virtual sem os pacotes da maquina para arquivo especifico:
# python3 -m venv myenv (nome do ambiente virtual)
# source myenv/bin/activate (ativa ambiente virtual)
# deactivate - desativa ambiente virtual



# pipenv - mais simplista

# https://pipenv.pypa.io/en/latest/
# pipenv cria um ambiente virtual e instala pacotes nele
# cria o ambiente dentro da pasta onde esta executando, adicionando nome aleatorio ao ambiente virtual criado
# pipenv - lista de comandos pipenv
# pip install pipenv 
# pipenv install + pacote
# pipenv uninstall + pacote
# pipenv lock 
# pipenv graph - lista as dependencias dos pacotes, pacotes secundarios que esses pacotes precisam
# bat pipfile.lock - mostra arquivo criado por pipenv lock 
# pipenv clean - remove pacotes nao listados em pipfile.lock, como por exemplo, qdo vc remove um pacote e ficam seus pacotes filhos, os filhos sao removidos
# ls - lista os arquivos

'''
Quando você executa pipenv lock, ele cria um arquivo chamado Pipfile.lock. Esse arquivo é formatado em JSON e contém informações detalhadas sobre os pacotes Python utilizados no ambiente virtual específico do projeto. Aqui estão algumas das informações que o Pipfile.lock geralmente inclui:

Versões dos Pacotes: Lista as versões específicas de cada pacote Python instalado no ambiente virtual.

Informações de Dependências: Informa quais pacotes dependem de quais outros pacotes e suas versões específicas.

Integridade do Ambiente: Inclui hashes SHA-256 para garantir a integridade dos pacotes instalados, ajudando a garantir que todas as instalações sejam consistentes.

Informações do Ambiente Virtual: Pode conter informações sobre a versão do Python utilizada, informações do sistema operacional, entre outros detalhes relevantes para a replicação do ambiente.
'''



# poetry - **** mais poderoso q os concorrentes e mais facil de aprender

# https://python-poetry.org/docs/   -   https://python-poetry.org/docs/basic-usage/
# similar ao pipenv
# pip install poetry
# poetry new myproject - cria projeto do zero qdo vc nao tem pasta
# cd myproject - entra na pasta do projeto
# poetry add xxx - add dependencia
# poetry remove xxx - remove arquivo e dependencias, filhas
# ls - lista os arquivos
# poetry init - cria arquivo pyproject.toml, que é similar ao pipfile.lock
# bat pyproject.toml - abre arquivo pyproject.toml
# poetry show - mostra pacotes instalados
# poetry show -t - mostra pacotes instalados e suas dependencias, filhas, detalhadas
# poetry show --help - mostra ajuda


'''
O comando poetry init no Poetry é usado para iniciar um novo projeto Poetry. Ele interativamente solicita informações básicas sobre o projeto, como o nome, a versão, a descrição e as dependências iniciais. Este comando cria o arquivo pyproject.toml, que é onde o Poetry gerencia as informações do projeto, incluindo as dependências e outras configurações.
'''



# PEP - propostas de melhoria do python

# PEP 8 - mais conhecida, cobre estilo de codificaçao
# guia de estilo para codificaçoes em python. inclui nomes de variaveis, uso de espaço em branco, comprimento da linha e outros.
# https://peps.python.org/pep-0008/

# principais recomendaçoes:
# 4 espaços para identaçao
# limitar as linhas a 79 caracteres
# usar nomes de variaveis em snake_case para funçoes e variaveis e CamelCase para classes

# flake8 é uma ferramenta de checagem de estilo que verifica e nos informa onde desviamos do guia do estilo

# pip install flake8
# flake8 meu_script.py 
# flake8 --help - comandos
# flake8 --max_line_length =120 meu_script.py - aumenta o numero padrao de caracteres por linha para 120 ( ou colocar numero desejado)

# black é uma ferramenta de formataçao automatica de codigo com a PEP 8

# pip install black
# black meu_script.py

# isort é uma ferramenta para classificar importaçoes alfabeticamente e separa-las automaticamente em seçoes

# https://peps.python.org/pep-0008/#imports

# pip install isort
# isort meu_script.py 
















