import time
import math

print("CURSO EM VIDEO - PYTHON")
print("Hipotenusa\n")
time.sleep(1)
print("A fórmula para o cálculo da hipotenusa é a² + b² = c²")
print("Logo Cateto_Oposto² + Cateto_Adjacente² = Hipotenusa²\n")
time.sleep(1)
catops = float(input("Digite o valor do cateto oposto : \n"))
catadj = float(input("Digite o valor do cateto adjacente : \n"))
time.sleep(1)
sqrco = catops**2 
sqrca = catadj**2
sqrhipo = sqrco + sqrca
hipotenusa = math.sqrt(sqrhipo)
time.sleep(3)
print("\n###########################################\n")
print(f"Portanto: {catops}² + {catadj}² = Hipotenusa²")
print(f"   Logo: {sqrco} + {sqrca} = √{sqrhipo} ")
print(f"     --> √{sqrhipo} = {hipotenusa:.3f}\n")
print(f"O comprimento da hipotenusa vale: {hipotenusa:.3f} !\n")
print("###########################################\n")
time.sleep(30)
