import random
import sys

opciones_validas = ["piedra","papel","tijeras"]
cpu = random.choice(opciones_validas)

while True:
    opciones_de_usuario = input("Cual es tu eleccion: piedra, papel o tijeras: ").strip().lower()    
    if opciones_de_usuario in opciones_validas:
        break
    else:
        print("Esa opcion no es valida! vuelve a intentarlo")
        
print(f"usuario eligio {opciones_de_usuario} y la cpu eligio {cpu}")      
if opciones_de_usuario == cpu:
    print("empateeee")
    sys.exit()
elif opciones_de_usuario == "piedra" and cpu == "tijeras":
    print("Ganasteeeeeeeeeee :)")
    sys.exit()
else:
    print("perdiste :(")
    sys.exit()
     
    
if opciones_de_usuario == "tijeras" and cpu == "papel":
    print("ganasteeee :O")
    sys.exit()
else:
    print("perdiste ;(")
    sys.exit()
    
if opciones_de_usuario == "papel" and cpu == "piedra":
    print("Ganasteeee :)")
    sys.exit()
else:
    print("perdiste :((")
    sys.exit()
    
    

     
   
    

           