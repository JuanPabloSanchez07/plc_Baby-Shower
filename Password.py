import re

def generar_password():
    password = ""
    while len(password) < 8:
        caracter = input("Introduce un carácter para el password: ")

        # Validación: Verifica si el carácter es una letra o un número
        if re.match("^[a-zA-Z0-9]$", caracter):
            password += caracter
            print(f"Carácter añadido. Longitud actual del password: {len(password)}")
        else:
            print("Error: El password solo puede contener letras y números.")

    print(f"\n¡Password generado exitosamente! El password es: {password}")

# Llamamos a la función principal
generar_password()
