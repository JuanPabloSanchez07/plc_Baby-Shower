contar = 0
categoria1 = 0
categoria2 = 0 
animal = input("¿Quieres comenzar a contar animales? (si/no): ")
while animal.lower() == "si":
  contar += 1
  #print(contar)
  edad = int(input("¿Quieres comenzar a contar animales? (si/no)"))
  animal = input("¿Quieres contar mas animales? (si/no): ")
  if edad <2:
    categoria1 += 1
  elif edad >= 2 and edad < 5:
    categoria2 += 1
porcentaje1 = categoria1*100/contar
porcentaje2 = categoria2*100/contar
print(f"Total de animales: {contar}")
print(f"Categoria 1: {porcentaje1}")
print(f"Categoria 1 : {porcentaje2}")
