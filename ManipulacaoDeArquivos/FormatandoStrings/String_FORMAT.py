from datetime import datetime

nome = "Arthur"
idade = 20
mensagem = "Olá, {}. Você tem {} anos".format(nome, idade)
mensagem2 = f"Olá, {nome}. Você tem {idade} anos" # MELHOR MÉTODO

print(mensagem)
print(mensagem2)

#PRECISÃO NUMÉRICA
valor = 3.14159
print(f"Pi com 2 casas decimais => {valor:.2f}")

#format()
print("PI COM 2 CASA DECIMAIS: {:.2f}".format(valor))

#FORMATANDO DATAS:
hoje = datetime.now()
data_formatada = hoje.strftime("Data : %d/%m/%Y")
print(data_formatada)

#F-TRING DATE
data_formatada = f"DATA: {hoje:%d/%m/%Y}" # MAIS SIMPLES E ELEGANTE
print(data_formatada)
