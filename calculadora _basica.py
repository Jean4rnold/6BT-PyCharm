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
    while true:
        try:
            numero = int(input(mensaje))
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
    choice = leerEntero("Dime que quieres hacer: > ")

# Operación a realizar
def main():
    choice = menu()
    print("opcion =", choice)
    num1 = leerEntero("Primer número ……: ")
    num2 = leerEntero("Segundo numero …..:: ")

    if choice ==0:
        print("saliendo")
    else:
        if choice == 1:
            print(num1, "+", num2, "=", Sumar(leerEntero("num1:"), leerEntero("num2:")))
        else:
            if choice == 2:
                print(num1, "-", num2, "=", Restar(leerEntero("num1:"), leerEntero("num2:")))
            else:
                if choice == 3:
                    print(num1, "*", num2, "=", Multiplicar(leerEntero("num1:"), leerEntero("num2:")))
                else:
                    if choice == 4:
                        print(num1, "/", num2, "=", Dividir(leerEntero("num1:"), leerEntero("num2:")))
                    else:
                        print("opcion invalida")

menu()