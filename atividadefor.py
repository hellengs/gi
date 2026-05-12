frutas = ["manga", "banana", "laranja", "uva", "abacaxi"]

frutas_favorita = input("Qual sua fruta favorita?: ")        

if frutas_favorita not in frutas:
  
#para cada psiçao (indice) e fruta NA lista numerada de frutas, 
# faca isso:
# 
 for posiçao, fruta in enumerate(frutas):
    #faça isso:
    #se a fruta dessa iteraçao é igual a fruta favorita do usuario, entao imprima a mensagem e pare o loop

  if fruta == frutas_favorita:
    # salva numa nova variavel a posiçao dessa fruta na lista
    posiçao_fruta_favorita = posiçao
    #quebra o for (faz ele parar)
    break
 
    #saida do algoritmo (print)
    print(f"Sua fruta favorita é a {frutas[posiçao_fruta_favorita]} e ela está na posição {posiçao_fruta_favorita} da lista de frutas.")