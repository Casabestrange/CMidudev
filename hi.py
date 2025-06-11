import random
# ciudadfav = input("Cual es tu ciudad favorita? ")
# nombre_mascota = input("Cual es el nombre de tu mascota?")

# print(f"{nombre_mascota} luis {ciudadfav}")

# numero1 = int(input("Ingresa un numero: "))
# numero2 = int(input("Ingresa otro numero: "))
# if numero1 + numero2 < 50:
    # print("bieeen")
# else:
    # print("que boludo")
###
numero_random = random.randint(1, 10000)
acertado = False
intentos = 0

while not acertado:
    ingtunumero = int(input("Adivina el número: "))
    intentos += 1
    if intentos >= 5: 
        print("superaste los intentos maximos, el numero era: ", numero_random )
        break

    if numero_random == ingtunumero:
        print("¡Acertaste! El número era:", numero_random)
        acertado = True
    elif numero_random < ingtunumero:
        print("Estás por encima del número al azar.")
        

    else:
        print("Estás por debajo del número al azar.")
    