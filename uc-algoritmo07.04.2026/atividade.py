P = int(input()) 
D = int(input())
B = int(input())

pontos = P + D + B

if pontos >= 150:
    print("B")
elif pontos >= 120:
    print("D")
elif pontos >= 100:
    print("P")
else:
    print("N")