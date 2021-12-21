import time
import math

print('Olá, sou Bob, o Construtor!\n')
time.sleep(2)
print('Diga-me as medidas da parede...\n')
time.sleep(2)
h = int(input('Qual a altura da parede?\n'))
time.sleep(2)
b = int(input('Qual o tamanho da base da parede?\n'))
time.sleep(2)
a = h*b
tinta = a/2
print(f"No caso, Área = base*altura, logo, {b}*{h} = {a} metros quadrados!\n")
time.sleep(2)
print(f'Serão necessários {tinta} latas de tinta para concluir a pintura!\n')
print('Fim do Algoritmo!')
time.sleep(10)