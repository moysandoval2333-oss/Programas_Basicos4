def es_palindromo(texto):
    texto_limpio = "".join(texto.split()).lower()
    return texto_limpio == texto_limpio[::-1]

frase = input("Introduce una palabra o frase: ")
if es_palindromo(frase):
    print(f"'{frase}' es un palíndromo.")
else:
    print(f"'{frase}' no es un palíndromo.")
    
