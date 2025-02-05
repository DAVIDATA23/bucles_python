# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 3.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realizar una calculadora
- Realizar un programa que se ejecute infinitas
  veces usando un bucle While True
- El programa se deberá terminar cuando el
  usuario indique la opción correspondiente
- Dentro del se debe ingresar por línea de comando dos números
- Luego se ingresará como tercera entrada al programa 
  la operación que se desea ejecutar:
- 1- Suma (+)
- 2- Resta (-)
- 3- Multiplicación (*)
- 4- División (/)
- 5- SALIR

Se debe efectuar el cálculo correcto según la
operación ingresada por consola

Alumno:
- Comience por generar el bucle While True
- Dentro del bucle imprima con prints el menú
  de opciones en consola.

- Crear una una variable llamada numero_1
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Crear una una variable llamada numero_2
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Crear una una variable llamada operacion
  para almacenar la operación que se desea efectuar
  ingresada por consola con la función input

- Armar una serie de condicionales para evaluar
  que operación efectuar. Deberá guardar el resultado
  de la operación en una variable llamada resultado

- Si el usuario ingresa la operación de SALIR, deberá
  finalizar el bucle con la sentencia break.

- Si el usuario ingresa una opción fuera del rango
  solicitado de opciones, el programa no deberá 
  estallar, no deberá hacer nada permitiendo
  que el bucle While vuelva a realizar la consulta
  en la próxima iteración.
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

operacion=0



while True:
  numero_1=int(input("ingrese el primer numero: "))
  numero_2=int(input("ingrese el segundo numero: "))


  print(".......Calculadora......")
  print(".....Menu......")
  print(" Suma.............1\n Resta...........2\n Multiplicacion...3\n Divicion.........4\n Salir............5\n" )
  operacion= int(input("Digite opcion: "))
  
  if operacion == 1:
      resultado=(numero_1+numero_2)
      print(f"el resultado de la suma es : {resultado}")
  elif operacion == 2:
      resultado=(numero_1-numero_2)
      print(f"El resultado de la resta es: {resultado}")
  elif operacion== 3:
      resultado=(numero_1*numero_2)
      print(f"El resultado de la multiplicacion es: {resultado}")
  elif operacion == 4:
    resultado=(numero_1/numero_2)
    print(f"El resultado de la divicion es: {resultado}")
  elif operacion== 5:  
    print("hasta pronto....")
    break



