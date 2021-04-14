from tablas import *

#Es valida verifica que el input que haya introducido el usuario sea valido
def es_valida(opcion):
    if len(opcion) < 2:
        return False

    if opcion[0].upper() == "CLASS":
        if(len(opcion) < 3): return False
        
        if opcion[2] == ":":
            for elem in opcion[3:]:
                if not elem.isalpha():
                    return False
            if len(opcion) < 4:
                return False
            else:
                return True
        else:
            for elem in opcion[2:]:
                if not elem.isalpha():
                    return False
            if len(opcion) < 3:
                return False
            else:
                return True
    elif opcion[0].upper() == "DESCRIBIR":
        if len(opcion) != 2:
            return False
        else:
            return True
    else:
        return False

#En main básicamente se pide al usuario una acción repetidamente, y se llama al resto de funciones
def main():

    print("Bienvenido al sistema. Podrá crear clases y asignar a cada una métodos")

    while True:
        
        print("\nIntroduzca CLASS <tipo> [<nombre>] para crear una nueva clase en el sistema")
        print("Introduzca DESCRIBIR <nombre> para ver los metodos de una clase\n")

        opcion = input("Por favor, introduzca una opcion ").strip().split(" ")
      
        if(es_valida(opcion)):
            if opcion[0] == "CLASS":
                crear_clase(opcion[1:])
            else:
                initialize_describir(opcion[1])               
        else:
            print("Por favor introduzca un input en formato válido")


if __name__ == "__main__":
    main()