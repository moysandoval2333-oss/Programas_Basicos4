def reemplazar_caracter(texto, viejo, nuevo):
    return texto.replace(viejo, nuevo)

texto_original = input("Introduce el texto original: ")
caracter_viejo = input("Carácter a reemplazar: ")
caracter_nuevo = input("Nuevo carácter: ")

resultado = reemplazar_caracter(texto_original, caracter_viejo, caracter_nuevo)
print(resultado)
