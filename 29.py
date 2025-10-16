Numero = int(input("introduce el numero base: "))
Base = int(input("introduce el exponente: "))

resultado = 1

if Base > 1:
  resultadoF = resultado * Numero
  resultadoFF = resultadoF * (Base * Numero)
print(f'el resultado es {resultadoFF}')
