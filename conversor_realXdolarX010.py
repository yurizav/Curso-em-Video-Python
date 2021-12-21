import time

print("CURSO EM VIDEO - PYTHON")
print("Conversor Real X Dólar\n")
time.sleep(3)
print("Cotação do dia: USD 1$ = BRL 5,74R$")
print("Atualizado em: 21 de dez. 2021 00:30 UTC\n")
time.sleep(1)
valor = int(input("Digite um valor inteiro à ser convertido em dólares: \n"))
nvalor = valor/5.74
print(f"Com {valor:.2f}, poderá comprar {nvalor:.2f} Dólares!")
time.sleep(20)