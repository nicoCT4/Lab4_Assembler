#Calcularador de  numero entero a  binario de 8 bits
#Que permita ingresar un número binario de 8 bits y  devuelva como resultado la representación de ese número en complemento a dos.  
# Que permita el ingreso de un número en hexadecimal de 3 dígitos y devuelva el número en decimal o que 
#se ingrese un número (que pueda representarse con 3 dígitos hexadecimales) y este se transforme e imprima en pantalla como hexadecimal.

#Nicolás Concuá y Javier Chavez
#Universidad del Valle de Guatemala

#Menu de opciones
def menu():
    print("1. Convertir un número entero a binario de 8 bits")
    print("2. Convertir un número binario de 8 bits a complemento a dos")
    print("3. Convertir un número hexadecimal a decimal")
    print("4. Convertir un número decimal a hexadecimal")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))
    return opcion

#Funcion para convertir un número entero a binario de 8 bits
def enteroBinario():
    numero = int(input("Ingrese un número entero: "))
    if numero > 255 or numero < -128:
        print("El número ingresado no es válido")
    else:
        if numero < 0:
            numero = numero + 256
        binario = bin(numero)
        binario = binario[2:]
        while len(binario) < 8:
            binario = "0" + binario
        print("El número en binario es: ", binario)

#Funcion para convertir un número binario de 8 bits a complemento a dos
def binarioComplemento():
    binario = input("Ingrese un número binario de 8 bits: ")
    if len(binario) != 8:
        print("El número ingresado no es válido")
    else:
        if binario[0] == "1":
            binario = binario.replace("0", "2")
            binario = binario.replace("1", "0")
            binario = binario.replace("2", "1")
            binario = binario.replace("0", "1", 1)
            print("El número en complemento a dos es: ", binario)
        else:
            print("El número en complemento a dos es: ", binario) 

#Funcion para convertir un número hexadecimal a decimal
def hexaDecimal():
    hexa = input("Ingrese un número hexadecimal de 3 dígitos: ")
    if len(hexa) != 3:
        print("El número ingresado no es válido")
    else:
        decimal = int(hexa, 16)
        print("El número en decimal es: ", decimal)

#Funcion para convertir un número decimal a hexadecimal
def decimalHexa():
    decimal = int(input("Ingrese un número decimal: "))
    if decimal > 4095 or decimal < 0:
        print("El número ingresado no es válido")
    else:
        hexa = hex(decimal)
        hexa = hexa[2:]
        print("El número en hexadecimal es: ", hexa)

#Funcion principal
def main():
    opcion = menu()
    while opcion != 5:
        if opcion == 1:
            enteroBinario()
        elif opcion == 2:
            binarioComplemento()
        elif opcion == 3:
            hexaDecimal()
        elif opcion == 4:
            decimalHexa()
        else:
            print("Opción no válida")
        opcion = menu()
    print("Fin del programa")

main()
