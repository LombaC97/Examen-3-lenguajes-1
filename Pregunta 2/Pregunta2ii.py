import os
import threading


#Manejamos una variable global cuenta que iniciara siendo 0
cuenta = 0
#Para la sincronizacion de los hilos, utilizaremos un mutex
mutex = threading.Lock()
#Main simplemente se encarga de pedir el input del usuario
def main():
    #El directorio introducido puede ser relativo al working path actual (cosa que recomiendo)
    #Por ejemplo, al colocar "." (sin las comillas) , buscará en el directorio donde se encuentre este archivo
    #Al poner ".." (sin las comillas), buscará en el directorio anterior
    #Tambien se puede introducir un path ./hola , donde "hola" es una carpeta dentro del directorio actual, etc
    directorio = input("Introduzca el directorio: ")
    create_threads_inicial(directorio)

    #Es importante tener en cuenta que esta implementación sólo cuenta el número de archivos dentro del directorio
    #introducido y subdirectorios dentro de éste, sin embargo, no cuenta los directorios también. Sólo archivos en resumen/
    print("Numero de archivos encontrados:", cuenta)
    


def create_threads_inicial(directorio):
    #Inicialmente, creamos una lista utilizando listas por comprension en que estaran todas las rutas correspondientes
    #a carpetas que se encuentren dentro del directorio inicial introducido                  #Aqui se verifica que dicho camino sea un directorio
    directorios = [entrada for entrada in os.listdir(directorio) if os.path.isdir(os.path.join(directorio,entrada)) ]
    #Creamos tambien una lista inicial para los archivos que esten dentro del directorio inicial introducido.
    #Digamos que esta cuenta la lleva a cabo el proceso principal
    files = [file for file in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, file))]
    #Aunque aquí no deberia ser necesario, ya que de momento tenemos un único proceso, colocamos el mutex por cuestiones de sincronización
    mutex.acquire()
    #Llamamos a la funcion de suma
    add(files)
    #y lo liberamos
    mutex.release()
    
    #Ahora si, por cada subdirectorio que se encuentre dentro del directorio inicial introducido
    for entrada in directorios:
        #Creamos un hilo con target=look y le pasamos como argumento la entrada que corresponde a la ruta al directorio
        #que debe revisar
        t = threading.Thread(target=look, args= (os.path.join(directorio, entrada),))
        #Lo iniciamos
        t.start()
        #Y hacemos join para esperar hasta que cada hilo termine, de otra manera, no se obtendría la suma completa
        t.join()

#Add básicamente recibe un array y modifica el cuenta global
def add(files):
    global cuenta
    cuenta += len(files)

#look es llamado desde create_threads_inicial por cada hilo distinto
def look(directorio):
    
    #Primero revisamos en el directorio que le haya correspondido al hilo la cantidad de archivos que tenga
    files = [file for file in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, file))]
    #Ahora si es necesario el mutex por motivos de sincronización
    mutex.acquire()
    #sumamos
    add(files)
    #liberamos el mutex
    mutex.release()

    #Ahora, cada hilo se va a encargar de revisar cada nuevo directorio dentro del subdirectorio que le haya tocado
    nuevos_directorios = [entrada for entrada in os.listdir(directorio) if os.path.isdir(os.path.join(directorio,entrada)) ]
   
    #Asi, creamos entonces nuevos hilos por cada nuevo subdirectorio dentro de cada subdirectorio
    for new_directory in nuevos_directorios:
        #Creamos el hilo, y llamamos a la funcion look nuevamente pero con un argumento de directorio distinto
        t = threading.Thread(target=look, args=(os.path.join(directorio, new_directory), ))
        #Lo iniciamos
        t.start()
        #Nuvamente, hacemos join para que todos los hilos terminen y el programa imprima la cantidad de archivos correcta
        t.join()
        
main()
