import time

print("CURSO EM VÍDEO - EX 007")
print("Cálculo de Média do Aluno!\n")

av1 = float(input("Digite a nota da Avaliação 1...\n"))
av2 = float(input("Digite a note da Avaliação 2...\n"))
atv_comp = float(input("Digite a nota das Atividades Complementares...\n"))
media = (av1 + av2 + atv_comp)/3
# Ao escrever {media:.2f}, especificamente ":.2f", estou limitando as casas decimais a 2 casas após a vírgula!
# Eu poderia fazer {media:.3f} ou {media:.4f} e etc se quisesse.
print(f"A média entre as notas da Av1: {av1}, Av2: {av2} e atividades complementares: {atv_comp} é: {media:.2f}!\n")
print("Fim do Algoritmo!")
time.sleep(10)