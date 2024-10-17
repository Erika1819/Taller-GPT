#Caso 1. Elabora una función que imprima los números impares en un rango de manera inversa.
def imprimir_impares_inverso(inicio, fin):
    # Generar una lista de números impares en el rango
    impares = [num for num in range(inicio, fin + 1) if num % 2 != 0]
    # Imprimir la lista en orden inverso
    for num in reversed(impares):
        print(num)

# Ejemplo de uso
imprimir_impares_inverso(1, 20)

##caso 2
def imprimir_impares_inverso(inicio, fin):
    # Generar una lista de números impares en el rango
    impares = [num for num in range(inicio, fin + 1) if num % 2 != 0]
    # Imprimir la lista en orden inverso y separada por comas
    print(", ".join(map(str, reversed(impares))))

# Ejemplo de uso
imprimir_impares_inverso(1, 20)

#  #Caso 3
def crear_matriz(n):
    matriz = []
    for i in range(n):
        fila = [1] * (i + 1) + [0] * (n - i - 1)
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Definir el tamaño de la matriz
n = 6
matriz = crear_matriz(n)
imprimir_matriz(matriz)

#Caso 4
#Define el número máximo de asteriscos en la primera fila
max_stars = 11

# Genera la matriz
for i in range(max_stars, 0, -2):
    # Imprime los asteriscos centrados
    print(f"{'*' * i:^20}")

#Caso 5

