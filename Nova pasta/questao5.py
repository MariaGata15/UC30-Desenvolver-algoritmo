nome = input("Digite o nome completo do aluno: ")

matriculastr = input("Digite a sua matrícula: ")
matricula = int(matriculastr)

nota1str = input("Digite a primeira nota: ")
nota1 = float(nota1str)

nota2str = input("Digite a segunda nota: ")
nota2 = float(nota2str)

media = (nota1 + nota2) / 2

print(f"Nome do aluno: {nome}")

print(f"Matrícula: {matricula}")

print(f"Nota 1: {nota1:.2f}")

print(f"Nota 2: {nota2:.2f}")

print(f"Média final: {media:.2f}")