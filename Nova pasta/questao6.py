idade = int(input("Digite a idade do atleta: "))

if idade < 12:
    categoria = "infantil"
elif idade < 18:
    categoria = "Juvenil"
elif idade < 60:
    categoria = "Adulto"
else:
    categoria = "Sênior"

print("Categoria: ", categoria)