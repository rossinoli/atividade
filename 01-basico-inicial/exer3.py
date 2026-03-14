# 3-	Faça um programa que receba dois números e execute as operações listadas a seguir de acordo com a escolha do usuário:
 
num1 = float(input("Digite o primeiro numero: "))
num2 = float (input("Digite o segundo numero: "))

print("\n--- Escolha a Operacao ---")
print("1: Media entre os numeros digitados")
print("2: Diferenca entre os numeros")
print("3: produto entre os numeros digitados")
print("4: Divisao do primeiro pelo segundo")
print("----------------------------")


escolha = int(input("Digite o numero da sua escolha: "))

if escolha == 1:
    resultado = (num1 + num2) /2
    print(f"\nA media entre {num1} e {num2} é: {resultado}")

elif escolha == 2:
    resultado = abs(num1 - num2)
    print(f"\nA diferenca entre {num1} e {num2} é: {resultado}")

elif escolha == 3:
    resultado = num1 * num2
    print(f"\nO produto entre {num1} e {num2} é: {resultado}")

elif escolha == 4:
    if num2 ==0:
        print("\nErro: nao é possivel dividir por zero")
    else:
        resultado = num1 / num2
        print(f"\nA divisao de {num1} por {num2} é: {resultado:.2f}")

else:
    print("\nOpcao invalida! por favor, escolha um numero de 1 a 4")
