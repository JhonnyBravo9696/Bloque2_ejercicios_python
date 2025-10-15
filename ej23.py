numero = int(input("Introduce un numero: "))

suma = 0
contador = 1

while numero != 0:
  suma += numero
  contador += 1
  numero = int(input("Introduce un numero: "))
media = suma / contador

print (f'la suma es: {suma}')
print (f'numeros introducidos: {contador}')
print (f'la media de los numeros es: {media}')
