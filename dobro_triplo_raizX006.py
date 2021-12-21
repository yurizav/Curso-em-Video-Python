import time

print("CURSO EM VÍDEO - EX006")
print("Cálculo de Dobro, Triplo e Raiz!\n")
time.sleep(3)
num = int(input("Por favor, digite um número...\n"))
#num_dobro, num_triplo, num_raiz = num
num_dobro = num*2
num_triplo = num*3
num_raiz = float(num)**0.5 #Dessa forma, calculo a raiz sem a necessidade de importar a biblioteca MATH
print(f"O dobro de {num} é {num_dobro}, seu triplo é {num_triplo}, e sua raíz quadrada é {num_raiz}!\n")
print("Fim do Algoritmo!")
time.sleep(10)

# Também posso calcular a raíz dessas formas, usando a biblioteca math:

#   import math
#   num = float(input("Entre com um número:\n"))
#   raiz = math.sqrt(num)
#   print(f'\nA raiz quadrada de {num} é {raiz}\n')

# Ou:

#   import math
#   num = float(input("Entre com um número:\n"))
#   raiz = math.pow(num, 1/2)
#   print(f'\nA raiz quadrada de {num} é {raiz}\n')