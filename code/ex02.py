A = int(input("Digite o 1 lado do triangulo: "))
B = int(input("Digite o 1 lado do triangulo: "))
C = int(input("Digite o 1 lado do triangulo: "))

if (A > 0) and (B > 0) and (C > 0):

    if (A + B > C) and (A + C > B) and (B + C > A):

        if A != B and A != C and B != C:
            print(("Triangulo Escaleno"))
        else:
            if A  == B and A == C and B == C:
                print("Triangulo equilatero!")
            else:
                print("Triangulo isóceles!")
    else:
        print("Ao menos um dos valores indicados não servem para formar um triangulo")

else:
    print("Ao menos um dos valores indicados não servem para formar um triangulo")




