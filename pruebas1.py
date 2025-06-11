import sys

while True:
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    
    if numero1 == 0 or numero2 == 0:
        print("No es divisible entre 0. Use otro número.")
        sys.exit()  
    
    
    resultado = numero1 / numero2
    print(f"El resultado de la división es: {resultado}")
    break  