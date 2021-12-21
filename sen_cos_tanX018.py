import time
import math

print("CURSO EM VIDEO - PYTHON")
print("Seno, Cosseno e Tangente\n")
time.sleep(1)
ang = float(input("Digite o valor de um ângulo qualquer !\n"))
time.sleep(1)
seno = math.sin(ang)
cosseno = math.cos(ang)
tangente = math.tan(ang)
print("\n####################################################\n")
print(f"O valor do Seno de {ang} graus é {seno:.6f} !")
print(f"O valor do Cosseno de {ang} graus é {cosseno:.6f} !" )
print(f"O valor da Tangente de {ang} graus é {tangente:.6f} !" )
print("\n####################################################\n")
time.sleep(30)


