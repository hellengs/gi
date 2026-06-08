def exibir_menu():
    print("=== MENU ===")
    print("1. Adicionar")
    print("2. Listar")
    print("3. Remover")
    print("0. Sair")

def adicionar_tarefa(lista):
    tarefa = input("Digite a tarefa: ")
    lista.append(tarefa)
    print("Tarefa adicionada!")

def listar_tarefas(lista):
    if len(lista) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Tarefas:")
        for i, tarefa in enumerate(lista, start=1):
            print(f"{i}. {tarefa}")

def remover_tarefa(lista):
    if len(lista) == 0:
        print("Nenhuma tarefa cadastrada.")
        return

    listar_tarefas(lista)

    indice = int(input("Digite o número da tarefa para remover: ")) - 1

    if 0 <= indice < len(lista):
        removida = lista.pop(indice)
        print(f"Tarefa '{removida}' removida!")
    else:
        print("Número inválido!")

# Lista vazia
tarefas = []

while True:
    exibir_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa(tarefas)

    elif opcao == "2":
        listar_tarefas(tarefas)

    elif opcao == "3":
        remover_tarefa(tarefas)

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
        
        