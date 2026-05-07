produtos = ["arroz", "feijao", "maça", "agua", "suco", ]
precos = [10.00, 13.00, 4.00, 6.00, 15.00]

print(produtos)
print(produtos[0]) # imprime ""
print(produtos[-1]) # imprime "arroz"
print(len(produtos))

# para exibir:
print(f"o produto {produtos[0]} custa R${precos[0]}.")

# para remover o ultimo produto e o preço tambem:
produtos.remove(produtos[-1])
precos.remove(precos[-1])

# para somar o preço de todos os produtos:
total = sum(precos)
print(f"o total da compra é R${total}.")

# logica condicional ifelse para desconto:
if total <100:
    exit()
else:
    desconto = 0.95
    total = total * desconto 
    print(f"o total da compra com desconto é R${total}.")
