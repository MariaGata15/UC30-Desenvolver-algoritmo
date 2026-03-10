#sem dicionário
matricula1 = 2026001
nome = "Ana Silva"
telefone = "9999-8888"

#com dicionário
aluno = {
    "matricula": 2026001,
    "nome": "Ana Silva", 
    "telefone": "9999-8888"
}

print(aluno)

contato = {
    "@camilaqueiroz" : "Camila Queiroz",
    "@brunamarquezine": "Bruno M.",
    "@sheronmenezes": "Sheron M.",
    "@paolaoliveira": "Paola O."
}

print(contato)
print(type(contato))

# Acesso direto
print(type(contato))

# Acesso seguro com get ()
print(contato.get("@paolaoliveira"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente", "Não encontrado"))


#add novo elemento
contato["@giovana"] = "Giovana"
print("Após add: ", contato)

#atualiza elemento existente
contato["@paolaoliveira"] = "Paola Oliveira"
print("Após add: ", contato)

contato.update({
    "@brunamarquezine": "Bruna Marquezine",
    "@camilaqueiroz": "Camila Q."
})

print("Após atualização: ", contato)

#pop: remove e retorna
removido = contato.pop("@paolaoliveira")
print(f"Removido: {removido}")
print("Após o pop: ", contato)

#del remove sem retornar

del contato ["@rivimirelle"]
print("Após del: ", contato)

#clear esvazia tudo 

copia = dict(contato)
contato.clear()
print("Apó~s clear: ", contato)
print("Cópia: ", copia)

print("Número de contato: ", len(contato))#tamanho dicio

#verificar existência
if "@joao" in contato:
    print(f"Encontrado: {contato['@joao']}")

if"@inexistente" in contato:
    print("Existe")
else:
    print("Não existe.")
