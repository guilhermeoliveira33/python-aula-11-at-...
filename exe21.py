n= 1
par = impar =0
while n!=0:
    n = int(input("digite um numero: "))
    if n % 2 == 0:
        par += n
    else:
        impar += n
print("voce digitou : ",par,"numeros pares e",impar,"numeros impares")