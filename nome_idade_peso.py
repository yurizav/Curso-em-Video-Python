import time

print("Oi , eu sou Nutry!\n")
time.sleep(1)
print("Seu assistente pessoal de nutrição.\n")
nome = input("Digite seu nome ?...\n")
time.sleep(1)
peso = input ("Qual é o seu peso ?...\n")
time.sleep(1)
idade = input("Qual a sua idade ?...\n")
time.sleep(1)
print("Olá %s!\nVocê tem %s anos, e pesa %s kilos!"%(nome, idade, peso))#interpolação de string