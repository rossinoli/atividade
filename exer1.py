# 1-	FAÇA UM PROGRAMA EM PYTHON QUE RECEBA DOIS VALORES, E MOSTRE TODOS OS VALORES ENTRE ESSES VALORES.

num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))

inicio = min(num1, num2)
fim = max(num1, num2)

print(f"\nos valores inteiros entre {inicio} e {fim} são: ")

if fim - inicio <= 1:
    print("Não existem valores inteiros entre os numeros fornecidos.")
else:
    for numero in range(inicio + 1, fim):
        print(numero, end =" ")
    print()

    