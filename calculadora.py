while True:
    print("Calculadora")
    print("1 - soma +")
    print("2 - subtração -")
    print("3 - multiplicação *")
    print("4 - divisão /")
    print("5 - sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = num1 + num2
        print("Resultado:", resultado)

    elif opcao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = num1 - num2
        print("Resultado:", resultado)

    elif opcao == 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = num1 * num2
        print("Resultado:", resultado)

    elif opcao == 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if num2 != 0:
            resultado = num1 / num2
            print("Resultado:", resultado)
        else:
            print("Erro: divisão por zero não é permitida.")

    elif opcao == 5:
        print("Saindo da calculadora. Até mais!")
        break

    else:
        print("Opção inválida!")
   