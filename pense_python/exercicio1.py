"""Exercícios da página 35 do livro Pense em Python
"""
"""No Programa "Hello World!" o que acontece se omitir uma das aspas? E se omitir ambas?
"""
from cmath import pi

print ('Hello World')
x = +2
print(x)
b = 2 ++ 2
print(b)
m = '0' + '2'
print(m)
"""
Qantos segundos há em 42 minutos e 42 segundos?_
"""
'\n'
fator = 60
minutos = int(input('Quantos minutos deseja converter em segundos (entre apenas com números inteiros)?\n'))
segundos = int(input('Existe alguns segundos inferiores a um minuto? Se sim digites quantos, se não digite 0\n'))
total = (minutos * fator) + segundos
print(f'{minutos} minutos tem {total} segundos')

#Exercício 2.1

x = y = 1
print(f'x = {x}')
print(f'y = {y}')

#Cálculo do volume de uma esfera:

raio = float(input('Digite o raio:\n'))
if raio < 0:
    print('O raio deve ser maior que zero! O programa será encerrado!')
else:
    volume = (4/3) * pi * (raio**3)
    print('O volume da esfera de raio %5.2f é %5.2f' % (raio, volume))

"""Suponha que o preço de capa de um livro seja R$24,95, mas as livrarias recebem com desconto de 40%
O transporte custa R$ 3,00 o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo
total de atacado para 60 cópias?    
"""

preco = float(input('Digite o preço de capa do livro:\n'))
desconto = float(input('Digite o desconto de capa em porcentagem:\n'))
transporte_1 = 3.00
transporte_demais = 0.75
quantidade = float(input('Digite a quantidade de exemplares a serem compradas:\n'))

preco_com_desconto = preco - (preco * desconto/100)
transporte = transporte_1 + (0.75 * (quantidade - 1))
preco_total = (preco_com_desconto * quantidade) + transporte
print('\nA compra de %5.2f exemplares custa R$%5.2f' % (quantidade, preco_total))

#primeiro quilometro

saida_hora = float(input('Digite a hora da saída:\n'))
saida_min = float(input('Digite os minutos da saída:\n'))
min_passo1 = float(input('Digite os minutos do passo do primeiro km:\n'))
seg_passo1 = float(input('Digite os segundos do passo do primeiro km:\n'))
min_passo3 = float(input('Digite os minutos do passo dos proximos 3 km:\n'))
seg_passo3 = float(input('Digite os segundos do passo dos próximos 3 km:\n'))
min_passo11 = float(input('Digite os minutos do passo do km final:\n'))
seg_passo11 = float(input('Digite os segundos do passo do km final:\n'))
seg_total_1 = min_passo1 * 60 + seg_passo1
seg_total_3 = min_passo3 * 60 + seg_passo3
seg_total_11 = min_passo11 * 60 + seg_passo11
tempo = (1 * seg_total_1) + (3 * seg_total_3) + (1 * seg_total_11)
tempo_min = int(tempo/60)
segundos = tempo % 60
print('O tempo total da corrida foi de %5.0f minutos e %.0f segundos.' % (tempo_min, segundos))
    