import random

numeros = [45, 12, 78, 23, 56]
print("Lista original: ", numeros)

# sort crescente
numeros.sort(reverse=True)
print("Após sort(): ", numeros)

# embaralha
random.shuffle(numeros)
print("LIsta embaralhada: ", numeros)

