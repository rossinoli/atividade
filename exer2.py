# 2-	FAÇA UM PROGRAMA QUE REALIZE SORTEIOS DE 0 ATÉ 100, PARE O PROGRAMA APENAS QUANDO O NÚMERO 55 FOR ENCONTRADO, E MOSTRE A QUANTIDADE DE TENTATIVAS.

import random

tentativas = 0
numero_soreteado = 0


print("Iniciando o sorteio! O programa irá parar quando o numero 55 for encontrado.")
print("--------------------------------------------------------------------")

while numero_soreteado != 55:
    numero_soreteado = random.randint(0,100)
    tentativas += 1
    print(f"tentativa nº {tentativas}: o numero sorteado foi {numero_soreteado}")


print("--------------------------------------------------------------------")
print(f"FIM DO SORTEIO! O número 55 foi encontrado!")
print(f"Foram necessárias {tentativas} tentativas.")