contador = 1

while contador <= 10:
    contador += 1
    if contador == 5:
        print("pulei o numero 5!")
        continue #força o laço a realizar a verificação da condição (ou pular um loop)

    print(contador)

