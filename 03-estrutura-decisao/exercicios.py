import math

def exibir_cabecalho(titulo):
    print(f"\n{'-'*50}")
    print(f"{titulo.center(50)}")
    print(f"{'-'*50}\n")

# --- EXERCÍCIOS ---

def exe_01():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print(f"O maior número é: {max(n1, n2)}")

def exe_02():
    valor = float(input("Digite um valor: "))
    if valor > 0: print("O valor é POSITIVO")
    elif valor < 0: print("O valor é NEGATIVO")
    else: print("O valor é NEUTRO (Zero)")

def exe_03():
    sexo = input("Digite F ou M: ").upper()
    if sexo == 'F': print("F - Feminino")
    elif sexo == 'M': print("M - Masculino")
    else: print("Sexo Inválido")

def exe_04():
    letra = input("Digite uma letra: ").lower()
    if letra in 'aeiou': print("É uma VOGAL")
    else: print("É uma CONSOANTE")

def exe_05():
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2
    if media == 10: print("Aprovado com Distinção")
    elif media >= 7: print("Aprovado")
    else: print("Reprovado")

def exe_06():
    n1 = float(input("Digite o 1º número: "))
    n2 = float(input("Digite o 2º número: "))
    n3 = float(input("Digite o 3º número: "))
    maior = max(n1, n2, n3)
    print(f"O MAIOR número é: {maior}")

def exe_07():
    n1 = float(input("Digite o 1º número: "))
    n2 = float(input("Digite o 2º número: "))
    n3 = float(input("Digite o 3º número: "))
    maior = max(n1, n2, n3)
    menor = min(n1, n2, n3)
    print(f"O MAIOR número é: {maior}")
    print(f"O MENOR número é: {menor}")

def exe_08():
    exibir_cabecalho("QUAL PRODUTO COMPRAR?")
    precos = []
    for i in range(1, 4):
        entrada = input(f"Digite o preço do {i}º produto (ex: 10.50): ").replace(',', '.')
        preco = float(entrada)
        precos.append(preco)
    mais_barato = min(precos)
    print(f"\nO preço mais barato é R$ {mais_barato:g}")
    print("Você deve comprar o produto de menor preço!")

def exe_09():
    nums = [float(input(f"Número {i+1}: ")) for i in range(3)]
    nums.sort(reverse=True)
    print(f"Ordem decrescente: {nums}")

def exe_10():
    turno = input("Turno (M-Matutino, V-Vespertino, N-Noturno): ").upper()
    if turno == 'M': print("Bom Dia!")
    elif turno == 'V': print("Boa Tarde!")
    elif turno == 'N': print("Boa Noite!")
    else: print("Valor Inválido!")

def exe_11():
    salario = float(input("Salário atual: R$ "))
    if salario <= 280: perc = 20
    elif salario <= 700: perc = 15
    elif salario <= 1500: perc = 10
    else: perc = 5
    aumento = salario * (perc/100)
    print(f"Antes: R$ {salario:.2f} | Percentual: {perc}% | Aumento: R$ {aumento:.2f} | Novo: R$ {salario + aumento:.2f}")

def exe_12():
    valor_hora = float(input("Valor da hora: "))
    horas = float(input("Horas trabalhadas: "))
    bruto = valor_hora * horas
    if bruto <= 900: ir_perc = 0
    elif bruto <= 1500: ir_perc = 5
    elif bruto <= 2500: ir_perc = 10
    else: ir_perc = 20
    
    ir = bruto * (ir_perc/100)
    inss = bruto * 0.10
    fgts = bruto * 0.11
    total_desc = ir + inss
    print(f"Salário Bruto: R$ {bruto:.2f}\n(-) IR ({ir_perc}%): R$ {ir:.2f}\n(-) INSS (10%): R$ {inss:.2f}\nFGTS (11%): R$ {fgts:.2f}\nTotal descontos: R$ {total_desc:.2f}\nLíquido: R$ {bruto - total_desc:.2f}")

def exe_13():
    dia = input("Dia (1-7): ")
    dias = {"1":"Domingo", "2":"Segunda", "3":"Terça", "4":"Quarta", "5":"Quinta", "6":"Sexta", "7":"Sábado"}
    print(dias.get(dia, "Valor inválido"))

def exe_14():
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2
    if media >= 9: conceito = "A"
    elif media >= 7.5: conceito = "B"
    elif media >= 6: conceito = "C"
    elif media >= 4: conceito = "D"
    else: conceito = "E"
    status = "APROVADO" if conceito in "ABC" else "REPROVADO"
    print(f"Média: {media} | Conceito: {conceito} | Status: {status}")

def exe_15():
    l1 = float(input("Lado 1: "))
    l2 = float(input("Lado 2: "))
    l3 = float(input("Lado 3: "))
    if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
        if l1 == l2 == l3: tipo = "Equilátero"
        elif l1 == l2 or l1 == l3 or l2 == l3: tipo = "Isósceles"
        else: tipo = "Escaleno"
        print(f"É um triângulo {tipo}")
    else: print("Não formam um triângulo")

def exe_16():
    a = float(input("Valor de A: "))
    if a == 0:
        print("Equação não é do 2º grau. Encerrando.")
        return
    b = float(input("Valor de B: "))
    c = float(input("Valor de C: "))
    delta = b**2 - 4*a*c
    if delta < 0: print("Delta negativo. Sem raízes reais.")
    elif delta == 0: print(f"Uma raiz real: {-b / (2*a)}")
    else:
        r1 = (-b + math.sqrt(delta)) / (2*a)
        r2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Duas raízes: {r1:.2f} e {r2:.2f}")

def exe_17():
    ano = int(input("Ano: "))
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): print("Bissexto")
    else: print("Não é Bissexto")

def exe_18():
    data_texto = input("Digite uma data (dd/mm/aaaa): ")
    partes = data_texto.split('/')
    if len(partes) != 3:
        print("Formato inválido! Use dd/mm/aaaa")
        return
    dia = int(partes[0])
    mes = int(partes[1])
    ano = int(partes[2])
    valida = False
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= dia <= 31:
            valida = True
    elif mes in [4, 6, 9, 11]:
        if 1 <= dia <= 30:
            valida = True
    elif mes == 2:
        if 1 <= dia <= 28:
            valida = True
    if valida:
        print(f"A data {dia:02d}/{mes:02d}/{ano} é VÁLIDA.")
    else:
        print("Data INVÁLIDA!")

def exe_19():
    num = int(input("Número (< 1000): "))
    c = num // 100
    d = (num % 100) // 10
    u = num % 10
    print(f"{num} = {c} centenas, {d} dezenas e {u} unidades")

def exe_20():
    print("--- MÉDIA DE 3 NOTAS ---")
    n1 = float(input("Nota 1: ").replace(',', '.'))
    n2 = float(input("Nota 2: ").replace(',', '.'))
    n3 = float(input("Nota 3: ").replace(',', '.'))
    media = (n1 + n2 + n3) / 3
    print(f"\nMédia alcançada: {media:.1f}") 
    if media == 10:
        print("Aprovado com Distinção")
    elif media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

def exe_21():
    saque = int(input("Valor saque (10-600): "))
    if not (10 <= saque <= 600):
        print("Valor inválido")
        return
    notas = [100, 50, 10, 5, 1]
    for n in notas:
        qtd = saque // n
        saque %= n
        if qtd > 0: print(f"{qtd} nota(s) de R$ {n}")

def exe_22():
    num = int(input("Número: "))
    print("PAR" if num % 2 == 0 else "ÍMPAR")

def exe_23():
    print("--- INTEIRO OU DECIMAL ---")
    num_str = input("Digite um número: ").replace(',', '.')
    num = float(num_str)
    if num == round(num):
        print(f"O número {num:g} é INTEIRO.")
    else:
        print(f"O número {num:g} é DECIMAL.")

def exe_24():
    print("--- OPERAÇÕES COMPLETAS ---")
    n1 = float(input("Digite o 1º número: ").replace(',', '.'))
    n2 = float(input("Digite o 2º número: ").replace(',', '.'))
    print("\nQual operação deseja realizar?")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    escolha = input("Escolha (1/2/3/4): ")
    if escolha == '1': resultado = n1 + n2
    elif escolha == '2': resultado = n1 - n2
    elif escolha == '3': resultado = n1 * n2
    elif escolha == '4': resultado = n1 / n2
    else:
        print("Operação inválida!")
        return
    print(f"\nResultado da operação: {resultado:g}")
    if resultado % 2 == 0: info_par = "Par"
    else: info_par = "Ímpar"

    if resultado >= 0: info_sinal = "Positivo"
    else: info_sinal = "Negativo"
    if resultado == round(resultado): info_tipo = "Inteiro"
    else: info_tipo = "Decimal"
    print(f"O resultado é: {info_par}, {info_sinal} e {info_tipo}.")

def exe_25():
    litros = float(input("Litros: "))
    tipo = input("A-Álcool ou G-Gasolina: ").upper()
    if tipo == 'A':
        preco = 1.90
        desc = 0.03 if litros <= 20 else 0.05
    else:
        preco = 2.50
        desc = 0.04 if litros <= 20 else 0.06
    total = litros * preco * (1 - desc)
    print(f"Total a pagar: R$ {total:.2f}")

def exe_26():
    print("--- SISTEMA DA FRUTEIRA ---")
    kg_morango = float(input("Kg de Morango: ").replace(',', '.'))
    kg_maca = float(input("Kg de Maçã: ").replace(',', '.'))

    if kg_morango <= 5:
        preco_morango = 2.50
    else:
        preco_morango = 2.20
        
    if kg_maca <= 5:
        preco_maca = 1.80
    else:
        preco_maca = 1.50
    valor_morango = kg_morango * preco_morango
    valor_maca = kg_maca * preco_maca
    peso_total = kg_morango + kg_maca
    valor_total = valor_morango + valor_maca
    if peso_total > 8 or valor_total > 25:
        valor_total = valor_total * 0.90
        print("Desconto de 10% aplicado!")
    print(f"\nPeso Total: {peso_total:g} Kg")
    print(f"Valor a pagar: R$ {valor_total:.2f}")

def exe_27():
    print("--- HIPERMERCADO TABAJARA ---")
    print("1 - Filé Duplo")
    print("2 - Alcatra")
    print("3 - Picanha")
    opcao = input("Escolha o tipo de carne (1/2/3): ")
    kg = float(input("Quantidade (Kg): ").replace(',', '.'))
    cartao = input("Compra no Cartão Tabajara? (S/N): ").upper()
    if opcao == '1':
        nome_carne = "Filé Duplo"
        preco_kg = 4.90 if kg <= 5 else 5.80
    elif opcao == '2':
        nome_carne = "Alcatra"
        preco_kg = 5.90 if kg <= 5 else 6.80
    elif opcao == '3':
        nome_carne = "Picanha"
        preco_kg = 6.90 if kg <= 5 else 7.80
    else:
        print("Opção de carne inválida!")
        return
    preco_total = kg * preco_kg
    desconto = 0
    tipo_pagamento = "Dinheiro/Outros"
    if cartao == 'S':
        tipo_pagamento = "Cartão Tabajara"
        desconto = preco_total * 0.05
    valor_pagar = preco_total - desconto
    print("\n" + "="*30)
    print("      CUPOM FISCAL      ")
    print("="*30)
    print(f"Carne: {nome_carne}")
    print(f"Quantidade: {kg:g} Kg")
    print(f"Preço Total: R$ {preco_total:.2f}")
    print(f"Pagamento: {tipo_pagamento}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"VALOR A PAGAR: R$ {valor_pagar:.2f}")
    print("="*30)

# --- MENU ---
def menu():
    while True:
        print("\n" + "="*50)
        print("LISTA: ESTRUTURA DE DECISÃO".center(50))
        print("="*50)
        op = input("Exercício (1-27) ou 0 p/ sair: ")
        if op == '0': break
        
        funcoes = {
            '1': exe_01, '2': exe_02, '3': exe_03, '4': exe_04, '5': exe_05,
            '6': exe_06, '7': exe_07, '8': exe_08, '9': exe_09, '10': exe_10,
            '11': exe_11, '12': exe_12, '13': exe_13, '14': exe_14, '15': exe_15,
            '16': exe_16, '17': exe_17, '18': exe_18, '19': exe_19, '20': exe_20, '21': exe_21, 
            '22': exe_22, '23': exe_23, '24': exe_24, '25': exe_25, '26': exe_26, '27': exe_27
        }
        
        if op in funcoes:
            exibir_cabecalho(f"EXERCÍCIO {op}")
            funcoes[op]()
        else:
            print("Exercício não implementado ou inválido.")

if __name__ == "__main__":
    menu()
