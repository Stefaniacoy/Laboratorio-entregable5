import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 10)
    intentos = 0
    print("¡Adivina el numero entre 1 y 10!")
    
    while True: 
        intento = int(input("Ingresa tu número:"))
        intentos += 1
        
        if intento < numero_secreto:
            print("El número es mayor.")
        elif intento > numero_secreto:
            print("El número es menor.")
        else: 
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
    
juego_adivinanza()
