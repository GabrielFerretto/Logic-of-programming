print("CALCULADORA")
print("+ Adição")
print("- Subtração")
print("* Subtração")
print("* Multiplicação")
print("/ Divisão")
print("Presione outra tecla para sair")

op = input("Qual operação deseja fazer ? ")
if op == "*" or op == "-" or op == "*" or op == "/":
    x = int(input("Digite o primeiro valor: "))
    y = int(input("Digite o segundo valor: "))

if (op == "+"):
    res = x + y
    print(f"Resultado: {x} + {y} = {res}")
elif(op == "-"):
    res = x - y
    print(f"Resultado: {x} - {y} = {res}")
elif(op == "*"):
    res = x * y
    print(f"Resultado: {x} * {y} = {res}")
elif(op == "/"):
    res = x / y
    print(f"Resultado: {x} / {y} = {res}")

else:
    print("operação invalida")

print("Encerrando o programa...")
