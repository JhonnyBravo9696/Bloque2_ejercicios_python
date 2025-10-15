caracter = input("introduce un caracter en minuscula: ")

while caracter == "a" or "e" or "i" or "o" or "u":
  caracter = input("introduce un caracter en minuscula: ")
  print ("VOCAL")
else:
  print ("NO VOCAL")

if caracter == " ":
  print ("fin del bucle")
