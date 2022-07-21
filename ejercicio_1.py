import random

def main():
    # Escribir un programa que genere contraseñas aleatorias de un largo 
    # de 12 caracteres. Luego escriba 15 contraseñas generadas en un archivo 
    # llamado claves_generadas.txt. Por pantalla se deben mostrar las contraseñas
    # que se generaron en el archivo una por linea.
    largo_contrasena= 12
    contrasena = generar_contrasena(largo_contrasena)
    cant_contrasenas = 15
    f = open('./claves_generadas.txt', 'w')
    for i in range(cant_contrasenas):
        f.write( generar_contrasena(largo_contrasena))
        f.write("\n")
    f.close()
    with open('./claves_generadas.txt', 'r') as file:
        for linea in file:
            print(linea)

def generar_contrasena(len = 15):
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + numeros
    contrasena = []

    for i in range(len):
        caracter_aleatorio = random.choice( caracteres )
        contrasena.append( caracter_aleatorio )

    contrasena = ''.join(contrasena)

    return contrasena


if __name__ == '__main__':
    main()