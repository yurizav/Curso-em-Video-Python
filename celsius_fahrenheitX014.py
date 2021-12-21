import time

print("CURSO EM VIDEO - PYTHON")
print("Conversor Celcius X Fahrenheit\n")
valor = int(input("Digite um valor inteiro em Celcius à ser convertido em Fahrenheit : \n"))
nvalor = (valor * 1.8 + 32)
print(f"{valor:.2f}°C equivale à {nvalor:.2f}°F!")
time.sleep(20)