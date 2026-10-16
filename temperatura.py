# entrada
temperatura = float(input("Digite a temperatura: "))

if temperatura == 0:
    print("Temperatura baixa, cuidado com o congelamento.")
elif temperatura <= 15:
    print("Frio intenso no laboratorio.")
elif temperatura <= 25:
    print("Temperatura agradável.")
else:
    print("Temperatura alta! Ligar sistema de refrigeração.")