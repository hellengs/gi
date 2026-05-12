produtos = [ "camisa", "calça", "sapato", "meia", "bermuda" ,]
preços = [ 50.00, 100.00, 150.00, 20.00, 80.00]
quantidades = [2, 1, 2, 1, 1]
subtotais = [] # lista para armazenar os subtotais de cada produto

# ANTES, FARIA ASSIM PARA PEGAR O PRODUTO E PREÇO:

print(f"O produto {produtos[0]} custa R${preços[0]}.")

for indice, produto in enumerate (produtos):
    preço = preços[indice] # preço = preços 
    quantidade = quantidades[indice] # quantidade = quantidades
    subtotal = quantidade * preço # subtotal = preço * quantidade
    subtotais.append(subtotal) # adiciona o subtotal na lista de subtotais

    mensagem = f"""
    --------------------------------------
    O produto {produto} 
    Quantidade: {quantidade}
    Subtotal: R${subtotal:.2f}
    --------------------------------------
    """
    print(mensagem)