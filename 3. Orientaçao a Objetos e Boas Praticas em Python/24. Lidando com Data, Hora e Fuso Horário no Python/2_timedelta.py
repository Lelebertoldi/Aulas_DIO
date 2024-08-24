# timedelta é a duraçao da diferença entre 2 datas/horas
# ele serve para fazer calculos com data/hora, dizendo que algo vai acontecer daqui a 3 horas, por exemplo

from datetime import date, datetime, timedelta

tipo_carro = "M"  # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now() # ou utcnow para fuso horario

if tipo_carro == "P":
    data_estimada = data_atual - timedelta(days=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual - timedelta(days=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual - timedelta(days=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")


print(date.today() - timedelta(days=1))

# timedelta nao trabalha apenas com time, entao para manipular apenas a hora se usa datetime e chama apenas time no resultado
resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())
