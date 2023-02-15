# Test3
#Programa para imprimir tu nombre

nombre = input("¿Cúal es tu nombre?")
for i in range(50):
    print(f"{nombre}")

# Programa para contar

accion = input("Teclea Up para contar en positivo desde 0/ teclea Down para contar en negativo")
numeros_de_veces = int(input("¿Cuantas veces quieres repetir?"))
if accion == "Up" or accion == "up":
    for i in range(numeros_de_veces):
        print(i)
elif accion == "Down" or accion == "down":
    for i in range(numeros_de_veces,-1,-1):
        print (i)
else:
    print("Ingrese un valor valido")

# Invitados a la fiesta
gente=int(input("¿Cuanta gente acudira a la fiesta?"))
invitados = []
Max_invitados=5
if gente > Max_invitados:
    print(f"Lo siento solo,{Max_invitados} personas pueden acudir a la fiesta")
else:
    for i in range (gente):
        nombre_invitado = input("Introduce el nombre de los invitados ")
        print(f"El invitado {i} es {nombre_invitado}")
        invitados.append(nombre_invitado)
