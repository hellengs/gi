def exibir_menu():
    print("=== Menu ===")
    print("1. boas vindas!")
    print("2. Sobre o curso")
    print("3. ajuda (sobre o exercicio)")
    print("0. Sair")

def saudacao():
    nome = input("Digite seu nome: ")
    print(f"Bem-vindo ao curso,{nome}!")

def ajuda():
        print("esta ultilizando o loop infinito, ultilizando o while")

while True:
    exibir_menu()
    opçao = input("Escolha uma opção: ")

    if opçao == "0":
        
        break

    elif opçao == "1": 
        saudacao()  
    elif opçao == "2":
        print("O curso jovem programador tem como objetivo ensinar os jovens a programar")

    elif opçao == "3":
        ajuda()
        
    else:
        print("Opção inválida. Tente novamente.")
        