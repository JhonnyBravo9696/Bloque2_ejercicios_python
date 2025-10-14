numero = int(input("introduce tu numero:"))

multiplicador=1
resultado=1

while multiplicador <= numero:
    resultado *= multiplicador
    multiplicador += 1

print (f'el factorial de {numero} es igual a {resultado}')
