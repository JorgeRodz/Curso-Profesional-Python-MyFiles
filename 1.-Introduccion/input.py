nombre_completo = input("Ingresa tu nombre completo: ") # input() returns a string
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura: "))
autorizacion = input("¿Estás autorizado? (si/no): ") == "si"

print("Value type: ", type(nombre_completo))
print("Value type: ", type(edad))
print("Value type: ", type(altura))
print("Value type: ", type(autorizacion))
# print(nombre_completo)
