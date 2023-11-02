print("Hola Mundo")
#soy un comentario

"""
Texto
"""
#variables
texto = "Repaso de python"
nombre = "willy"
year = 2023

print(f"{texto} - {nombre} - {str(year)}")

# Entrada
#sitioweb = input("¿Cuál es tu página web?:")
#print("El sitio web del usuario es: " + sitioweb)

# Condiciones
"""
altura = int(input("¿Cuál es tu altura?: "))
if altura >= 170:
    print("Muy bien")
else:
    print("Eres bajito")
"""

# Funciones
"""
var_altura = int(input("¿Cuál es tu altura?: "))

def mostrarAltura(altura):
    resultado = ""

    if altura >= 170:
         resultado = "Muy bien"
    else:
         resultado = "Eres bajito"
    
    return resultado

print(mostrarAltura(var_altura))
"""

# Listas
personas = ["Víctor", "Paco", "Pepe"]
print(personas[1])

for persona in personas:
    print("-" + persona)