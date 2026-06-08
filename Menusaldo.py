def exibir_menu():
    print("=== MENU ===")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver saldo")
    print("0. Sair")

def depositar(saldo):
    valor = float(input("Digite um valor pra depositar: "))
    saldo = saldo + valor
    print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    return saldo

def sacar(saldo):
    saque = float(input("Digite um valor pra sacar: "))
    if saque > saldo:
        print("Saldo insuficiente!")
    else:
        saldo = saldo - saque
        print(f"Saque de R${saque:.2f} realizado com sucesso!")
    return saldo

def ver_saldo(saldo):
    print(f"Seu saldo é de R${saldo:.2f}")

saldo = 0.0 
while True:
        exibir_menu()   
        opcao = input("Escolha uma opção: ")
     
        if opcao == "0":
            print("Saindo...")
            break
        elif opcao == "1":
            saldo = depositar(saldo)
        elif opcao == "2":
            saldo =   sacar(saldo)
        elif opcao == "3":
            saldo =  ver_saldo(saldo)
        else:
            print("Opção inválida!")

