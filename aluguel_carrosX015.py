import time

print("CURSO EM VIDEO - PYTHON")
print("Aluguel de Carros\n")
time.sleep(1)
print("Valor por dia alugado: R$ 60,00")
print("Valor por Km rodado: R$ 0,15\n")
time.sleep(0.5)
valorA = int(input("Quantos dias o carro ficou alugado ?\n"))
valorB = int(input("Quantos kilômetros o carro rodou nesse período ?\n"))
nvalorA = (valorA*60)
nvalorB = (valorB*0.15)
cet = nvalorA + nvalorB
print(f"O custo de aluguel por {valorA} dias é de R${nvalorA} !")
print(f"O custo da quilômetragem, de {valorB} km rodados, é de R${nvalorB} !\n")
print(f"O custo efetivo total do aluguel é R${cet} !\n")
time.sleep(20)

