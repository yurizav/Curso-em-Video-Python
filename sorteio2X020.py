import time
import random

# Sortear nomes aleatoriamente dentro de uma lista.

print("CURSO EM VIDEO - PYTHON")
print("Sortear Alunos\n")
time.sleep(1)
a = (input("Digite o nome da primeira pessoa...\n"))
b = (input("Digite o nome da segunda pessoa...\n"))
c = (input("Digite o nome da terceira pessoa...\n"))
d = (input("Digite o nome da última pessoa...\n"))
nomes = [ a, b, c, d ]
time.sleep(1)
random.shuffle(nomes)
print(f"O ordem sorteada foi:{nomes}")
time.sleep(20)