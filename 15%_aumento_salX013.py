import time

print("\nSeja bem vindo ao seu assistente de RH!\n")
time.sleep(2)
nome = str(input("Digite seu nome...\n"))
time.sleep(2)
salario = float(input("Digite o valor de seu salário atual, com ponto entre as casas decimais!\n"))
time.sleep(2)
print(f"Olá, {nome}! Tenho boas notícias!\n")
time.sleep(2)
print(f"Parabéns {nome}, você acaba de receber um aumento salarial!\n")
time.sleep(2)
aumento = (salario/100)*115
print(f"Sua remuneração, de R${salario:.2f} passará para {aumento:.2f}! Aproveite!\n")
print("Fim do algoritmo!")
time.sleep(10)