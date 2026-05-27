produtos = ["Arroz", "Feijão", "Macarrão"]
precos = [5.99, 6.99, 12.99]

for posicao_produto, produto in enumerate(produtos):
    

    if precos[posicao_produto] < 10:
        preco_ajustado = round(precos[posicao_produto] * 1.10, 2)
        print(f"O produto {produto} custa R${preco_ajustado} e subiu para R${preco_ajustado}.")

    else:
        print(f"O produto {produto} custa R${precos[posicao_produto]}")
