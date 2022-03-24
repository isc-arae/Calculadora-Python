#Calculadora by Arae
import time
otraOperacion = True
while(otraOperacion):
  try:
    opcion = int(input("""\nBienvenido a tu Calculadora
escoje una opción por favor:\n
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir\n
"""))
    if(opcion == 5):
      print("\nAdios y Gracias!")
      break
    elif(opcion > 0 and opcion < 5):
      num1 = float(input("\nIngrese el 1er número: "))
      num2 = float(input("\nIngrese el 2do número: "))
      if(opcion == 1):
        print(f"\nLa suma de {num1} + {num2} es: {num1 + num2}")
      if(opcion == 2):
        print(f"\nLa resta de {num1} - {num2} es: {num1 - num2}")
      if(opcion == 3):
        print(f"\nLa multiplicación de {num1} x {num2} es: {round((num1 * num2),4)}")
      if(opcion == 4):
        print(f"\nLa división de {num1} ÷ {num2} es: {round((num1 / num2),4)}")
    else:
      print("\nIngrese una opción válida por favor")
    time.sleep(1)
  except:
    print("\nIngrese una opción válida por favor")
    time.sleep(1)