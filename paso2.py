#Condicionales if y else
numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
    
#Bucle for
lista_numeros = [1, 2, 3, 4, 5]

print("Los cuadrados de los números en la lista son:")
for num in lista_numeros: 
    print(f"{num} al cuadrado es {num ** 2}")
    
#Bucle while
entrada = ""
while entrada.lower() != "salir":
    entrada = input("Escribe 'Salir' para terminar el programa:")
    print("¡Programa finalizado!")