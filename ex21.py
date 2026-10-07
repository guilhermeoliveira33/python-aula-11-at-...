soma = 0

for n in range(6):
    numero=int(input("digite um numero:"))
    if numero % 2 == 0:
         soma += numero

print(" o valor da somas dos impares é :" , soma)