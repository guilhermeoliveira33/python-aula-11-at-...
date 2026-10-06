total_economizado = 0
mes = 1

while mes <= 3:
    valor = float(input(f"digite o valor a ser economizado no mes{mes}:"))
    total_economizado += valor + total_economizado
    mes +=1 #contator

print("parabéns ! voce economizou", total_economizado)

    #contator normalmente é utilizado na condição do loop
    #contador incrementa valores por padrão +1, ou; +2

    # acumulador pode ser utilizado na condição do loop
    # não soma valores padronizados