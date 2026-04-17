total = 0.0
valor = float(input("Digite o valor do item ou 0 para encerrar: "))


while valor != 0:
    total += valor 
    valor = float(input("Digite o valor do item ou 0 para encerrar: "))


print("O total da compra é:", total)