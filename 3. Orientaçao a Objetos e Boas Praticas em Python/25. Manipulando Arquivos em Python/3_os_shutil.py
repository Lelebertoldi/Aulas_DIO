

import os
import shutil
from pathlib import Path


# Se você deseja obter o diretório onde o próprio script está localizado (que pode ser diferente do diretório atual, especialmente se o script foi chamado de outro lugar), você pode usar __file__ em combinação com Path:
ROOT_PATH = Path(__file__).parent

# Cria o novo diretório na pasta designada como raiz
os.mkdir(ROOT_PATH / "novo-diretorio")

#Se o diretório já existir, os.mkdir lançará um erro. Para evitar isso, você pode usar os.makedirs com exist_ok=True:
# os.makedirs(novo_diretorio, exist_ok=True)
# Isso garantirá que o diretório será criado sem lançar um erro se ele já existir e criará todos os diretórios intermediários necessários.


# se você não especificar um diretório no nome do arquivo, ele será criado na mesma pasta onde o script Python está sendo executado
# criar arquivo
arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

# renomear arquivo
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

# remover arquivo
os.remove(ROOT_PATH / "alterado.txt")

# mover arquivo
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")



"""
A parte ROOT_PATH no código define o caminho raiz ou base a partir do qual outros diretórios ou arquivos serão criados ou acessados. Utilizando o módulo pathlib para definir ROOT_PATH como uma instância de Path, você pode construir caminhos de maneira mais intuitiva e segura, especialmente quando está lidando com diferentes sistemas operacionais (Windows, Linux, macOS).

Aqui está uma explicação detalhada sobre cada componente:

Definição do Caminho Raiz:

python
Copy code
from pathlib import Path

# Define o caminho raiz usando pathlib
ROOT_PATH = Path('caminho/para/o/diretorio')
Aqui, ROOT_PATH é um objeto Path que representa o diretório "caminho/para/o/diretorio". Esse caminho pode ser relativo ou absoluto, dependendo da sua necessidade.

Construção de Novos Caminhos:

python
Copy code
# Define o novo diretório a ser criado
novo_diretorio = ROOT_PATH / 'novo-diretorio'
Usando o operador /, você pode concatenar caminhos de maneira simples e segura. novo_diretorio agora é um objeto Path que representa o caminho completo para o novo diretório dentro de ROOT_PATH.

Criação do Diretório:

python
Copy code
# Cria o novo diretório
os.mkdir(novo_diretorio)
Aqui, os.mkdir cria o novo diretório especificado por novo_diretorio.

Para evitar erros se o diretório já existir ou se você precisar criar diretórios intermediários, você pode usar os.makedirs:

python
Copy code
import os
from pathlib import Path

# Define o caminho raiz usando pathlib
ROOT_PATH = Path('caminho/para/o/diretorio')

# Define o novo diretório a ser criado
novo_diretorio = ROOT_PATH / 'novo-diretorio'

# Cria o novo diretório, incluindo todos os intermediários, se necessário
os.makedirs(novo_diretorio, exist_ok=True)

print(f'O diretório {novo_diretorio} foi criado com sucesso.')
Neste código, ROOT_PATH serve como a base para construir outros caminhos, facilitando a organização e manipulação de diretórios e arquivos no seu projeto.

"""

'''
Obter o Diretório Atual:
Você pode usar Path.cwd() para obter o diretório de trabalho atual (o diretório de onde o script está sendo executado):

python
Copy code
from pathlib import Path

# Obtém o diretório atual
ROOT_PATH = Path.cwd()

print(f'Diretório atual: {ROOT_PATH}')
Usar o Diretório do Script:
Se você deseja obter o diretório onde o próprio script está localizado (que pode ser diferente do diretório atual, especialmente se o script foi chamado de outro lugar), você pode usar __file__ em combinação com Path:

python
Copy code
from pathlib import Path

# Obtém o diretório onde o script está localizado
ROOT_PATH = Path(__file__).parent

print(f'Diretório do script: {ROOT_PATH}')
Criar e Manipular Caminhos:
Depois de definir ROOT_PATH, você pode construir caminhos relativos a partir dele e criar novos diretórios ou arquivos:

python
Copy code
from pathlib import Path
import os

# Obtém o diretório onde o script está localizado
ROOT_PATH = Path(__file__).parent

# Define o novo diretório a ser criado
novo_diretorio = ROOT_PATH / 'novo-diretorio'

# Cria o novo diretório, incluindo todos os intermediários, se necessário
os.makedirs(novo_diretorio, exist_ok=True)

print(f'O diretório {novo_diretorio} foi criado com sucesso.')
Neste exemplo, ROOT_PATH será o diretório onde o script está localizado. A partir daí, você pode construir caminhos adicionais e criar diretórios conforme necessário.

'''



