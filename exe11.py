#Do-while
while True:
    n = int(input("digite 0 ou 1 para sair: "))

    if n == 0:
        print(f"você digitou {n}. Saindo do laço")
        break
    elif n == 1:
       print("você digitou ",n, "tente novamente")

    print("fora do laço")