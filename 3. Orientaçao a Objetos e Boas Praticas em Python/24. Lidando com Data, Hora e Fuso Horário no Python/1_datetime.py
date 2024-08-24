# como add data e hora. se importar apenas date tb funciona
# documentaçao modulo datetime: https://docs.python.org/pt-br/3/whatsnew/3.11.html#datetime
# date é constituido por ano, mes, dia
# https://docs.python.org/pt-br/3.6/library/datetime.html
from datetime import date, datetime, time

data = date(2023, 7, 10)
print(data)
print(date.today())


data_hora = datetime(2023, 7, 10) # mais usado, diz a data e hora exata para um registro. passar hora é opcional
print(data_hora)
print(datetime.today()) # hora e data atual

hora = time(10, 20, 0)
print(hora)


# para salvar a data em uma variavel e usar depois:

from datetime import datetime

# Obtém a data e hora atuais
data_transacao = datetime.today()

# Exemplo de uso: imprimir a data da transação
print("Data da transação:", data_transacao)

# Mais tarde, você pode acessar diferentes partes da data, se precisar
print("Ano:", data_transacao.year)
print("Mês:", data_transacao.month)
print("Dia:", data_transacao.day)
print("Hora:", data_transacao.hour)
print("Minuto:", data_transacao.minute)
print("Segundo:", data_transacao.second)






