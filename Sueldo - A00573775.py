def calcular_sueldo(salario_base, ventas):
    if ventas < 3500:
        comision = 0.07
    elif 3500 <= ventas <= 7000:
        comision = 0.1
    else:
        comision = 0.15

    return salario_base + (ventas * comision)

def main():
    vendedores = []

    while True:
        otro_vendedor = input("¿Hay otro vendedor? (si/no): ").lower()

        if otro_vendedor != 'si':
            break

        nombre = input("Ingrese el nombre del vendedor: ")
        salario_base = float(input("Ingrese el salario base de {}: ".format(nombre)))
        ventas = float(input("Ingrese el total de ventas realizadas por {}: ".format(nombre)))

        sueldo_total = calcular_sueldo(salario_base, ventas)
        vendedores.append((nombre, sueldo_total))

    print("\nResumen de sueldos:")
    for vendedor in vendedores:
        print("{} - {}: ${:.2f}".format(vendedor[0], "Sueldo", vendedor[1]))

if __name__ == "__main__":
    main()
