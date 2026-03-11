senha = input("Digite a senha: ")

numero = False

for caractere in senha:
    if caractere.isdigit():
        numero = True

if len(senha) >= 8 and numero:
    print("Senha válida.")
else:
    print("Senha inválida.")