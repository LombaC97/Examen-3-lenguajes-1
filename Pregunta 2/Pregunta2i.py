import random
import threading

matrizA = []
matrizB = []
matrizC = []

#Valor por defecto para la dimension y el numero de hilos
dimension = 2
num_hilos = 1

def input_dimensiones():
    global dimension
    global num_hilos
    #Introducimos los valores de dimension y la cantidad de hilos que se deseen utilizar
    dimension = int(input("Introduce un número para generar las matrices NxN : "))
    num_hilos = int(input("Introduce el número de hilos que quieras utilizar : "))

#Aqui creamos matrices con valores aleatorios (para no tener que introducir valor por valor)
def matrices_aleatorias():
    for i in range(dimension):
        #Por cada dimension, se crean listas por compresión en un rango del 0 al 100
        matrizA.append([random.randint(0,100) for numero in range(dimension)])
        matrizB.append([random.randint(0,100) for numero in range(dimension)])
        #Y la matriz C del resultado se inicializa con únicamente 0
        matrizC.append([0 for numero in range(dimension)])

#La función de sumar matrices es llamada para cada hilo, el cual se va a encargar de sumar su parte correspondiente
def sumar_matrices(comienzo, final):
    for i in range(comienzo, final):
        for j in range(dimension):
            matrizC[i][j] = int(matrizA[i][j] + matrizB[i][j])

#En esta función creamos un hilo según la cantidad de hilos introducida por el usuario  
def crear_hilos():
    #Por cada j en el range hasta el numero de hilos
    for j in range(0, num_hilos):
        #Crearemos un hilo distinto                     #Nótese que cada hilo se encargará de sumar una parte de la matriz, que dependerá de las dimensiones y num de hilos
        t = threading.Thread(target = sumar_matrices, args=(int((dimension/num_hilos) * j), int((dimension/num_hilos) * (j+1))))
        #Lo iniciamos
        t.start()  
        #Hacemos join
        t.join() 
      
#Aqui imprimimos las matrices mas bonito
def print_matrix(array):
    for elem in array:
        print(elem)
  
            
if __name__=="__main__":
    #Aqui simplemente llamamos a cada una de las funciones anteriormente explicadas
    input_dimensiones()
    matrices_aleatorias()

    crear_hilos()
    
    print_matrix(matrizA)
    print("\n")
    print_matrix(matrizB)
    print("\n")
    print_matrix(matrizC)