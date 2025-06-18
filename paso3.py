#Listas y bucles
estudiantes = ["Ana Ruiz", "Luis Coy", "Carlos Manzanares", "Maria Quintero", "Fabian Novoa"]

print("----- Lista inicial de estudiantes ------")
for estudiante in estudiantes:
    print(estudiante)
    
#Diccionario simple con informacion de contacto
contacto = {
    "nombre": "Stefania Coy",
    "correo": "stefaniacoy97@gmail.com"
}

print("----- Información de contacto -----")
for clave, valor in contacto.items():
    print(f"{clave}: {valor}")
    
#Script para agregar a la lista o actualizar el diccionario
while True:
    print("¿Qué deseas hacer?")
    print("1. Agregar un estudiante a la lista")
    print("2. Actualizar información de contacto")
    print("3. Ver lista de estudiantes")
    print("4. Ver información de contacto")
    print("5. Salir")
    
    opcion = input("Elige una opción (1-5): ")
    
    if opcion == "1":
        nuevo_estudiante = input("Escribe el nombre del estudiante: ")
        estudiantes.append(nuevo_estudiante)
        print("Estudiante agregado exitosamente.")
        
    elif opcion == "2":
        clave = input("¿Qué deseas actualizar? (nombre o correo): ").lower()
        if clave in ["nombre", "correo"]:
            valor = input(f"Escribe el nuevo valor para {clave}: ")
            contacto[clave] = valor
            print(f" {clave.capitalize()} actualizado correctamente.")
        else: 
            print("Opción no valida.")
    
    elif opcion == "3":
        print("----- Lista actualizada de estudiantes -----")
        for estudiante in estudiantes:
            print(estudiante)
    
    elif opcion == "4":
        print("----- Información actualizada de contacto -----")
        for clave, valor in contacto.items():
            print(f"{clave}: {valor}")
            
    elif opcion == "5":
        print("¡Hasta luego! Gracias por usar el programa.")
        break
    
    else:
        print("Opción inválida. Intenta de nuevo.")
