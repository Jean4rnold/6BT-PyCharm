# PCaculadora.

#Suma
def Sumar(x, y):
    return x + y

# Resta
def Restar(x, y):
    return x - y

# Multiplica
def Multiplicar(x, y):
    return x * y

# División
def Dividir(x, y):
    return x/y

def leerEntero(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            break;
        except:
            print("Error >> Entero no valido.")

#Menu
def menu():
    print("Ingrese la Operación a Realizar: ")
    print(">>> 0.Salir")
    print(">>> 1.Sumar")
    print(">>> 2.Restar")
    print(">>> 3.Multiplicar")
    print(">>> 4.Dividdir")
    return leerEntero("    Dime que quieres hacer: > ")

# Operación a realizar
def main():
    #num1 = leerEntero("Primer número ……: ")
    #num2 = leerEntero("Segundo numero …..:: ")

    opcion = menu()
    print("opcion = ", opcion)

    if opcion == 0:
        print("saliendo")
    else:
        if opcion == 1:
            print(Sumar(leerEntero("num1:"), leerEntero("num2:")))
        else:
            if opcion == 2:
                print(Restar(leerEntero("num1:"), leerEntero("num2:")))
            else:
                if opcion == 3:
                    print(Multiplicar(leerEntero("num1:"), leerEntero("num2:")))
                else:
                    if opcion == 4:
                        print(Dividir(leerEntero("num1:"), leerEntero("num2:")))
                    else:
                        print("opcion invalida")

menu()