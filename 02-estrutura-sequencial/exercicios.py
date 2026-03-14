import math

def exibir_cabecalho(titulo):
    print(f"\n{'-'*50}")
    print(f"{titulo.center(50)}")
    print(f"{'-'*50}\n")

def exercicio_01():
    print("Alo mundo")

def exercicio_02():
    num = input("Digite um número: ")
    print(f"O número informado foi {num}")

def exercicio_03():
    n1 = float(input("Digite o 1º número: "))
    n2 = float(input("Digite o 2º número: "))
    print(f"A soma é: {n1 + n2}")

def exercicio_04():
    notas = [float(input(f"Nota {i+1}: ")) for i in range(4)]
    media = sum(notas) / 4
    print(f"Média Bimestral: {media:.2f}")

def exercicio_05():
    metros = float(input("Metros: "))
    print(f"{metros}m equivalem a {metros * 100:.0f}cm")

def exercicio_06():
    raio = float(input("Raio do círculo: "))
    area = math.pi * (raio ** 2)
    print(f"Área do círculo: {area:.2f}")

def exercicio_07():
    lado = float(input("Lado do quadrado: "))
    area = lado ** 2
    print(f"Área: {area} | Dobro da área: {area * 2}")

def exercicio_08():
    valor_hora = float(input("Ganho por hora: R$ "))
    horas = float(input("Horas trabalhadas no mês: "))
    print(f"Salário Total: R$ {valor_hora * horas:.2f}")

def exercicio_09():
    f = float(input("Temp. em Fahrenheit: "))
    c = 5 * ((f - 32) / 9)
    print(f"Temperatura em Celsius: {c:.1f}°C")

def exercicio_10():
    c = float(input("Temp. em Celsius: "))
    f = (c * 9/5) + 32
    print(f"Temperatura em Fahrenheit: {f:.1f}°F")

def exercicio_11():
    i1 = int(input("Inteiro 1: "))
    i2 = int(input("Inteiro 2: "))
    r = float(input("Real: "))
    res1 = (i1 * 2) * (i2 / 2)
    res2 = (i1 * 3) + r
    res3 = r ** 3
    print(f"a) Produto do dobro do 1º com metade do 2º: {res1}")
    print(f"b) Soma do triplo do 1º com o 3º: {res2}")
    print(f"c) Terceiro ao cubo: {res3:.2f}")

def exercicio_12():
    gb = float(input("Tamanho em GB: "))
    mb = gb * 1024
    print(f"{gb} GB = {mb:.0f} MB")

def exercicio_13():
    gb = float(input("Tamanho em GB: "))
    mb = gb * 1024
    kb = mb * 1024
    print(f"MB: {mb:,.0f} | KB: {kb:,.0f}")

def exercicio_14():
    peso = float(input("Peso de peixes (kg): "))
    limite = 50
    if peso > limite:
        excesso = peso - limite
        multa = excesso * 4
    else:
        excesso = 0
        multa = 0
    print(f"Excesso: {excesso:.2f}kg | Multa: R$ {multa:.2f}")

def exercicio_15():
    valor_hora = float(input("Quanto ganha por hora: "))
    horas = float(input("Horas trabalhadas: "))
    bruto = valor_hora * horas
    ir = bruto * 0.11
    inss = bruto * 0.08
    sindicato = bruto * 0.05
    liquido = bruto - ir - inss - sindicato
    
    print(f"\n+ Salário Bruto : R$ {bruto:.2f}")
    print(f"- IR (11%) : R$ {ir:.2f}")
    print(f"- INSS (8%) : R$ {inss:.2f}")
    print(f"- Sindicato (5%) : R$ {sindicato:.2f}")
    print(f"= Salário Liquido : R$ {liquido:.2f}")

def exercicio_16():
    area = float(input("Área a pintar (m²): "))
    litros = area / 3
    latas = math.ceil(litros / 18)
    print(f"Latas necessárias: {latas} | Preço: R$ {latas * 80:.2f}")

def exercicio_17():
    area = float(input("Área a pintar (m²): "))
    litros_necessarios = (area / 6) * 1.1  # 10% de folga
    
    # Opção 1: Apenas latas
    latas_apenas = math.ceil(litros_necessarios / 18)
    # Opção 2: Apenas galões
    galoes_apenas = math.ceil(litros_necessarios / 3.6)
    
    # Opção 3: Misto
    latas_misto = int(litros_necessarios // 18)
    resto = litros_necessarios % 18
    galoes_misto = math.ceil(resto / 3.6)
    
    print(f"\n1) Apenas latas (18L): {latas_apenas} - R$ {latas_apenas*80:.2f}")
    print(f"2) Apenas galões (3.6L): {galoes_apenas} - R$ {galoes_apenas*25:.2f}")
    print(f"3) Misto: {latas_misto} latas e {galoes_misto} galões - R$ {(latas_misto*80)+(galoes_misto*25):.2f}")

def exercicio_18():
    tamanho = float(input("Tamanho do arquivo (MB): "))
    velocidade = float(input("Velocidade do link (Mbps): "))
    # Mbps para MB/s (divide por 8)
    tempo_segundos = tamanho / (velocidade / 8)
    tempo_minutos = tempo_segundos / 60
    print(f"Tempo aproximado: {tempo_minutos:.2f} minutos")

# --- MENU PRINCIPAL ---
def menu():
    while True:
        print("\n" + "="*50)
        print("LISTA DE EXERCÍCIOS: ESTRUTURA SEQUENCIAL".center(50))
        print("="*50)
        print("01 a 18 - Escolha o exercício")
        print("0 - Sair")
        
        escolha = input("\nSelecione uma opção: ")
        
        if escolha == '0':
            print("Saindo... Até logo!")
            break
            
        funcoes = {
            '1': exercicio_01, '2': exercicio_02, '3': exercicio_03, '4': exercicio_04,
            '5': exercicio_05, '6': exercicio_06, '7': exercicio_07, '8': exercicio_08,
            '9': exercicio_09, '10': exercicio_10, '11': exercicio_11, '12': exercicio_12,
            '13': exercicio_13, '14': exercicio_14, '15': exercicio_15, '16': exercicio_16,
            '17': exercicio_17, '18': exercicio_18
        }
        
        if escolha in funcoes:
            exibir_cabecalho(f"EXERCÍCIO {escolha.zfill(2)}")
            funcoes[escolha]()
            input("\nPressione Enter para voltar ao menu...")
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
