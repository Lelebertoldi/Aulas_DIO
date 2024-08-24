# escrever no terminal - pip install pytz
# https://mljar.com/blog/list-pytz-timezones/
# se der erro digitar comando no terminal: python -m venv .env
# depois: source .env/bin/activate
# instalar pip novamente
# esse erro é pq o ambiente virtual usado nao é o msm inslado do pip
# se na aba do fim do vscode nao der para mudar o ambiente virtual apertar ctrl+shift+p e digitar interpretador > python: selecionar interpretador> buscar opçao com env:venv

from datetime import datetime

import pytz 

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)
