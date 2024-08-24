# strftime = string format time - formata data/hora para padrao desejado, como pt-BR, por exemplo 
# strptime = string parse time - converte de um formato para outro, como de uma string para data, por exemplo
# https://docs.python.org/pt-br/3.6/library/datetime.html

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %a" # dia, mes, ano, dia da semana
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr)) # strftime pode cortar as informaçoes e mostrar so o pedido

# strptime precisa da data em string e do formato entre ()
data_convertida = datetime.strptime(data_hora_str, mascara_en) # strptime precisa passar todas as informaçoes da string. 
print(data_convertida)
print(type(data_convertida)) # como foi convertido pra datetime agora pode ser editado como data, com timedelta, por exemplo
