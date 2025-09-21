# 5 - CRIE UMA FUNÇÃO CONVERTERCELSIUSPARAFAHRENHEIT (CELSIUS) QUE RETORNE A TEMPERATURA CONVERTIDA PARA FAHRENHEIT. DEPOIS, CRIE OUTRA FUNÇÃO CONVERTERFAHRENHEITPARACELSIUS(FAHRENHEIT) PARA A CONVERSÃO INVERSA. USE AS FÓRMULAS: 
# °F = °C × 1.8 + 32 
# °C = (°F - 32) / 1.8


def converterCelsiusParaFahrenheit(celsius):
    fahrenheit = celsius *1.8 +32
    return fahrenheit

def converterFahrenheitParaCelsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

print("--- Conversor de Temperaturas ---")
print("Escolha uma opção:")
print("1 - Converter de Celsius para Fahrenheit")
print("2 - Converter de Fahrenheit para Celsius")
escolha = input("Digite o número da sua opção (1 ou 2): ")


if escolha == '1':
    temp_celsius = float(input("Digite a temperatura em Celsius: "))

    temp_fahrenheit = converterCelsiusParaFahrenheit(temp_celsius)

    print(f"\nResultado: {temp_celsius:.1f}°C é igual a {temp_fahrenheit:.1f}°F")

elif escolha == '2':
    temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    temp_celsius = converterFahrenheitParaCelsius(temp_fahrenheit)
    print(f"\nResultado: {temp_fahrenheit:.1f}°F é igual a {temp_celsius:.1f}°C")
    
else:
    print("\nOpção inválida! Por favor, execute o programa novamente e digite 1 ou 2.")


