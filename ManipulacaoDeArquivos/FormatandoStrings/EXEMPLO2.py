from datetime import datetime

frutas = ['Jabuticaba', 'Laranja', 'Uvas', 'Morango']
for fruta in frutas:
    minha_fruta = f"Nome: {fruta:12} - Número de Letras: {len(fruta): 3}"
    print(minha_fruta)

pi = 3.1415
meu_numero = f'\nO número PI é: {pi:.1f}'
meu_numero_deslocado = f'O PI deslocado é: {pi:6.1f}'
meu_numero_preciso = f'O PI mais preciso é: {pi:.4f}'
print(meu_numero)
print(meu_numero_deslocado)
print(meu_numero_preciso)

data = datetime.now()
minha_data = f'A data de hoje é {data}'
minha_data_formatada = f'A data de hoje formatada é {data:%d/%m/%Y}'
print(minha_data)
print(minha_data_formatada)