import math

def calcular_raiz_cuadrada(numero):
    if numero < 0:
        return "No se puede calcular la raíz de un número negativo en reales."
    return math.sqrt(numero)

valor = float(input("Introduce un número: "))
print(f"La raíz cuadrada de {valor} es: {calcular_raiz_cuadrada(valor)}")
