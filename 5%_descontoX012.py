import time

print('Ajude-me a calcular o Desconto!\n')
time.sleep(2)
valor = float(input("Digite o valor do produto desejado: \n"))
time.sleep(3)
desconto = (valor/100)*95 # <-- Porcentagem de desconto!
print(f"O valor do produto BAIXOU!!! De R${valor} para R${desconto}, aproveite!\n")
print("Fim do algoritmo!")
time.sleep(10)