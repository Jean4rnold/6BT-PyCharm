def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


def validaCero(divisor):
    if (divisor == 0):
        print("Error: El divisor no puede ser cero.")
        return leerEntero("  Nuevo divisor (0 para salir):")
    else:
        return divisor


# def leerEntero(mensaje):
#     numero = 0
#     try:
#         numero = int(input(mensaje))
#     except:
#         print("Error... debe ingresar un entero.")
#     return numero

# def leerEntero(mensaje):
#     try:
#         return int(input(mensaje))
#     except:
#         return "Error... debe ingresar un entero."

def leerEntero(mensaje):
    contador = 0
    while contador < 3:
        try:
            # num = int(input(mensaje))
            return int(input(mensaje))
            # break;
        except:
            print(": Entero no válido..")
            contador = contador + 1
            if (contador == 3):
                print("El caracter ingresado no es entero. Regresando al menu.")
                print()
                main()
            else:
                print("Ingrese un entero valido")
                print()

            # return int(input(mensaje))

    # contador == 0
    # while contador < 3:
    #     contador += 1
    #     print(contador)


def menu():
    print("0- Salir")
    print("1- suma")
    print("2- resta")
    print("3- multiplicacion")
    print("4- division")
    return leerEntero("  >> Ingrese una opcion:")


def main():

    opcion = 0
    while opcion >= 0:
        print("========= MENU ==========")
        opcion = menu()
        print("Opcion = ", opcion)
        match (opcion):
            case 0:
                print("Chau ...")
                exit()
                print()
            case 1:
                print("La suma es:",suma(leerEntero("Num1: "), leerEntero("Num2: ")))
                print()
            case 2:
                print("La resta es:",resta(leerEntero("Num1: "), leerEntero("Num2: ")))
                print()
            case 3:
                print("La multiplicacion es:",multiplicacion(leerEntero("Num1: "), leerEntero("Num2: ")))
                print()
            case 4:
                num1 = leerEntero("Num1: ")
                num2 = validaCero(leerEntero("Num2: "))
                if (num2 != 0):
                    print("La division es:",division(num1, num2))
                    print()
                else:
                    print("El divisor sigue siendo cero. Regresando al menu.")
                    print()

    #if opcion == 0:
        #print("Chau ...")
    #else:
     #   if opcion == 1:
      #      print(suma(leerEntero("Num1: "), leerEntero("Num2: ")))
       # else:
        #    if opcion == 2:
         #       print(resta(leerEntero("Num1: "), leerEntero("Num2: ")))
          #  else:
           #     if opcion == 3:
            #        print(multiplicacion(leerEntero("Num1: "), leerEntero("Num2: ")))
             #   else:
              #      if opcion == 4:
               #         num1 = leerEntero("Num1: ")
                #        num2 = validaCero(leerEntero("Num2: "))
                 #       if (num2 != 0):
                  #          print(division(num1, num2))
                   #     else:
                    #        print("El divisor sigue siendo cero. Regresando al menu.")
                    #else:
                     #   print("Opcion inválida")


main()