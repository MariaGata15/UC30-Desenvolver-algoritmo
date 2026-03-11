distancia = 450.00
consumo = 8.0
precoLitro = 5.50

litrosConsumidos = distancia / consumo
custoTotal = litrosConsumidos * precoLitro

print(f"Distãncia percorrida: {distancia} km")

print(f"Consumo do carro: {consumo} km/litro")

print(f"Preço do litro: R$ {precoLitro:.2f}")

print(f"Litros consumidos: {litrosConsumidos:.2f} litros")

print(f"Custo total: R$ {custoTotal:.2f}")