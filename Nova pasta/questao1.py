salarioBase = 3500.00
bonus = 800.00
desconto = 250.00

salarioBruto = salarioBase + bonus
salarioLiquido = salarioBruto - desconto

print(f"Salário Base: R$ {salarioBase:.2f} ({type(salarioBase)})")

print(f"Bônus: R$ {bonus:.2f} ({type(bonus)})")

print(f"Desconto: R$ {desconto:.2f} ({type(desconto)})")

print(f"Salário Bruto: R$ {salarioBruto:.2f} ({type(salarioBruto)})")

print(f"Salário líquido: R$ {salarioLiquido:.2f} ({type(salarioLiquido)})")