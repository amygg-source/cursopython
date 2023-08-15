#crea un programa en python que solicite al usuario ingresar un numero entero 
#y determine si es positivo, negativo o cero

numero = int(input("digite el número"))
if numero > 0:
    if numero %2 == 0:
       print(f"su numero es par positivo")
elif numero == 0: 
   print(f"su número es 0")
else:
   print(f"su numero es negativo") 

#escribe un programa en python que solicite al usuario ingresar un número entero 
# y determine si es par, impar y si es divisible por 3

x = int(input( f"digite el número: "))

if x > 0 and x %2 == 0:
   print(f"el número es par:")  
elif x > 0 and x % 2 != 0 : 
   print("es un numero impar")
elif x == 0:
   print("el número es 0")   
elif x % 3 == 0:
   print(f"su número es multiplo de tres:")
else: 
   print("es un número negativo")

#Escribe un programa en python que solicite al usuario ingresar una letra y determine
# si es vocal o una consonante.
vocales = ("aeiou")
consonantes = ("bcdfghjklmnñpqrstvwxyz")
letras = str(input("digite la letra")) 
if letras == vocales :
   print(f"la letra es una vocal:")
else:
   print(f"La letra es una consonante:")   
#obtener la entrada del usuario usando input, ingresa tu edad si el usuario tiene 18
#decirle que es lo suficiente mayor para conducir, si es menor indica cuantos años le faltan.

edadUsuario = int(input("ingrese su edad"))
variable1 = (18 -edadUsuario)
if edadUsuario > 18:
   print(f"Eres lo suficiente mayor para conducir")
elif edadUsuario < 18:
   print(f"te hacen falta: {variable1} años para ser mayor de edad")

#comparar los valores de mi_edad y tu_edad usando if... else quien es mayor?
#(yo o tú) utiliza el inut ingresa tu edad para optener la edad como entrada.
#puedes usar condicion anidada para imprimir año para una diferencia de edad
#de un año, para diferencias mmayores y un texto personalizado si mi edad= tu edad

miEdad = int(input(f"introduzca mi edad"))
tuEdad = int(input(f"introduzca su edad"))
if miEdad > tuEdad:
    variableZ = miEdad - tuEdad
    print("tengo {varible1} años mas que tú")
    if miEdad != tuEdad + 1:
       print("tienes un año más")
elif miEdad < tuEdad:
   varible1 = tuEdad - miEdad
   print("Tú tienes {variablesZ} que yo")
else:
   print("tenemos la misma edad")   