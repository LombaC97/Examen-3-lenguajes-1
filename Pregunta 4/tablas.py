import sys
# Creamos una clase... clase  que va a tener las distintas clases que cree el usuario, la misma tendrá un nombre
# Un padre, y sus metodos propios
class Clase:
    def __init__(self, nombre, padre = None):
        self.nombre = nombre
        self.padre = padre
        self.tabla = []
    #Creamos la tabla
    def crear_tabla(self, metodos):
        #Si tiene padre
        if self.padre:
            for elem in self.padre.tabla:
                #Copiamos la tabla del padre
                self.tabla.append([elem[0], elem[1]])
            #Y luego verificamos si algun metodo de la clase padre
            #se encuentra sobreescrito en la clase hija
            for i in range(len(self.tabla)):
                if self.tabla[i][1] in metodos:
                    #De ser asi, actualizamos el nombre
                    self.tabla[i][0] = self.nombre
                    #Removemos el metodo del array de metodos
                    metodos.remove(self.tabla[i][1])
        #Y finalmente, para todos los metodos que esten en el array metodos lo agregamos a la tabla
        for metodo in metodos:
            self.tabla.append([self.nombre, metodo])
        
#Clases validas es un diccionario que contiene todas las clases que el usuario ha creado hasta el momento, sin importar
# su jerarquia, sencillamente las tiene
clases_validas = dict()

#Funcion para verificar si se introdujeron métodos repetidos
def repetidos(array):
    conjunto = set()
    for elem in array:
        if elem in conjunto:
            return True
        else:
            conjunto.add(elem)         
    return False

# Funcion que verifica dependencias circulares porque el enunciado lo pide, pero en realidad bajo las condiciones
# en que funciona este programa, no se crean dependencias circulares
def verificar_dependencias_circulares(clase_actual, ya_revisados):

    if(clase_actual in ya_revisados):
        return True
    ya_revisados.append(clase_actual)
    if clase_actual.padre is not None:
        return verificar_dependencias_circulares(clase_actual.padre, ya_revisados)

#Basicamente se crean todas las clases aqui
def crear_clase(opciones):
    #Si el primer elemento que corresponde al nombre de la clase, ya existe
    if(opciones[0].upper() in clases_validas.keys()):
        #Decimos que ya existe
        return print("La clase ya fue creada previamente, por favor introduzca otro nombre")
    #Si se trata de una herencia
    if(opciones[1] == ":"):
        #Mapeamos lower para escribir en minuscula los nombres de los distintos metodos
        metodos = list(map(lambda x: x.lower(), opciones[3:]))
        #Tomamos al padre de la clase
        padre = opciones[2]
        #Si el padre no existe en el diccionario de clases_validas, no ha sido creado
        if padre.upper() not in clases_validas.keys(): return print("Error, la clase padre no ha sido creada")
        #Si los metodos fueron escritos varias veces
        if repetidos(metodos): return print("Error, los metodos no deben estar repetidos en la declaración de la clase")
        #Creamos un nuevo objeto
        nueva_clase = Clase(opciones[0].upper(), clases_validas[padre])
        #Si no hay dependencias circulares
        if verificar_dependencias_circulares(nueva_clase, []): return print("Error, existen dependencias circulares en la declaración de la clase")
        #Guardamos la nueva entrada
        clases_validas[opciones[0].upper()] = nueva_clase
        #Finalmente, creamos la tabla de dependencias
        nueva_clase.crear_tabla(metodos)
        print("Clase {} creada con éxito".format(nueva_clase.nombre))
        return nueva_clase

    else:
        #Muy similar a lo escrito mas arriba
        metodos = list(map(lambda x: x.lower(), opciones[1:]))
        if repetidos(metodos): return print("Error, los metodos no deben estar repetidos en la declaración de la clase")
        #La diferencia es que, al no tener herencia, el padre es None
        nueva_clase = Clase(opciones[0])
        clases_validas[opciones[0]] = nueva_clase
        nueva_clase.crear_tabla(metodos)
        print("Clase {} creada con éxito".format(nueva_clase.nombre))
        return nueva_clase

#Verifica si la clase existe o no, en todo caso, de existir, llama a describir clase
def initialize_describir(opcion):
    if opcion not in clases_validas.keys(): return print("Error, la clase no existe")
    
    describir_clase(clases_validas[opcion])

#Describir clase recorre
def describir_clase(a_describir):
    for fila in a_describir.tabla:
        print("{} -> {} :: {}".format(fila[1], fila[0], fila[1]))

#Es valida verifica que el input que haya introducido el usuario sea valido
def es_valida(opcion):
    if opcion[0].upper() == "SALIR":
        return True
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

        opcion = sys.stdin.readline()[:-1].strip().split(' ')
        print(opcion)
        if(es_valida(opcion)):
            if opcion[0].upper() == "CLASS":
                crear_clase(opcion[1:])
            elif opcion[0].upper() == "DESCRIBIR":
                initialize_describir(opcion[1])    
            elif opcion[0].upper() == "SALIR":
                break           
        else:
            print("Por favor introduzca un input en formato válido")


if __name__ == "__main__":
    main()