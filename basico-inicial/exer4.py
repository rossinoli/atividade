# 4 - FAÇA UM PROGRAMA ONDE O USUÁRIO CHAME UMA FUNÇÃO PARA CALCULAR O AUMENTO DE SALÁRIO. NA CHAMADA DA FUNÇÃO, DEVEM SER ENVIADOS OS PARÂMETROS DE SALÁRIO E A PORCENTAGEM DE AUMENTO. VERIFIQUE SE O SALÁRIO É MAIOR QUE ZERO, BEM COMO A PORCENTAGEM.

def calcular_aumento(salario_atual, percentual_aumento):

    valor_do_aumento = salario_atual * (percentual_aumento /100)
    
    novo_salario =salario_atual + valor_do_aumento

    return novo_salario


print("--- Calculadora de Aumento Salarial ---")
salario_do_usuario = float(input("Digite o salario atual: R$ "))
porcentagem_usuario =float(input("Digite a porcetagem de aumento (apenas o numero): "))



if salario_do_usuario > 0 and porcentagem_usuario > 0:
    salario_reajustado = calcular_aumento(salario_do_usuario, porcentagem_usuario)
    print("\n--- Resultado ---")
    print(f"O salario de R$ {salario_do_usuario:.2f} com um aumento de {porcentagem_usuario}%")
    print(f"Passara a ser: R$ {salario_reajustado:.2f}")

else:
    print("\n[ERRO] O salario e a porcentagem de aumento devem ser valores maiores que zero!")


