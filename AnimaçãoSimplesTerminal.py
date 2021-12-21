import time, sys

animação = " Carregando... "

while True:   
    for i in list(animação):
        print(i, end='')
        # O stdout só é atualizado a cada nova linha, portanto, como a animação é uma frase na mesma linha, vamos atualizar à força!
        sys.stdout.flush()
        time.sleep(0.3)
        