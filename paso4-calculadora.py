def calculadora():
    print("¡Bienvenido a la calculadora básica!")
    
    while True:
        print("Opciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
    
        opcion = input("Selecciona una opción (1-4): ")
    
        if opcion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Ingresa el primer numero: "))
                num2 = float(input("Ingresa el segundo número: "))
        
                if opcion == "1":
                    resultado = num1 + num2
                    print(f"El resultado de la suma es: {resultado}")
                elif opcion == "2":
                    resultado = num1 - num2
                    print(f"El resultado de la resta es: {resultado}")
                elif opcion == "3":
                    resultado = num1 * num2
                    print(f"El resultado de la multiplicación es: {resultado}")
                elif opcion == "4":
                    if num2 != 0:
                        resultado = num1 / num2
                        print(f"El resultado de la división es: {resultado}")
                    else:
                        print("Error: No se puede dividir entre cero.")
            except ValueError:
                print("Error: Por favor ingresa números validos.")
        else: 
            print("Opción no valida. Intenta de nuevo")
            
        repetir = input("¿Quieres hacer otra operación? (si/no): ").lower()
        if repetir != "si": 
            print("¡Gracias por usar la calculadora!")
            break
        
calculadora ()
