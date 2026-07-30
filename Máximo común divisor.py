def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
print(f"El MCD de {num1} y {num2} es: {calcular_mcd(num1, num2)}")
