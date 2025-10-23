produto= int(input('qual o preço do produto que você quer?'))
if produto > 100:
    desconto = 0.2
else:
    desconto = 0.1
preco =produto - (produto * desconto)
print(f"o valor do produto vai ser de {preco} entao o desconto final será de {desconto *100:.2f}%")