preco = float(input("Digite o preço do produto:"))
p = float(input("Digite o percentual de desconto (0-100) :"))

desconto = preco * (p / 100)
final = preco - desconto

print(f"O preço do produto é {preco} o desconto será de {p}")
print(f"Valor calculado de desconto: {desconto} e o valor final do produto : {final}")

