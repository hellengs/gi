frutas = ["manga", "banana", "laranja", "uva", "abacaxi"]

frutas_favorita = input("Qual sua fruta favorita?: ")        

#para cada psiçao (indice) e fruta NA lista numerada de frutas, faca isso:
for posiçao, fruta in enumerate(frutas):
    #faça isso:
    #se a fruta dessa iteraçao é igual a fruta favorita do usuario, entao imprima a mensagem e pare o loop

 if fruta == frutas_favorita:
    # salva numa nova variavel a posiçao dessa fruta na lista
    posiçao_fruta_favorita = posiçao
    #quebra o for (faz ele parar)
    break