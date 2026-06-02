def exibir_menu():
    print("=== MENU ===")
    print("1. Converter celsius para fahrenheit")
    print("2. Converter reais para dolares")
    print("3. Cnverter horas para minutos")
    print("0. Sair")


def converter_celsius_para_fahrenheit():
    celsius =float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F") 

def converter_reais_para_dolares():
    reais = float(input("Digite o valor em Reais: "))
    dolar = reais / 5.0
    print(f"R${reais} é igual a ${dolar:.2f}")

def converter_horas_para_minutos():
    horas = float(input("Digite o valor em Horas: "))
    minutos = horas * 60
    print(f"{horas} horas é igual a {minutos} minutos")

while True:
    exibir_menu()
    
    opcao = input("Escolha uma opção: ")  

    if opcao == "0":

        break

    elif opcao == "1":
        converter_celsius_para_fahrenheit()
    elif opcao == "2":
        converter_reais_para_dolares()
    elif opcao == "3":
        converter_horas_para_minutos()
    else:
        print("Opção inválida. Tente novamente.")
