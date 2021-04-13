load 'Pregunta1i.rb'
#El grafo lo representamos con un objeto del tipo grafo
#Es importante tener en cuenta que estamos representando cada
#Posicion del grafo como un Diccionario. Las claves son los nodos
#Y los values son las listas de adyacencias que contienen
#La informacion sobre a que nodo se conecta
class Grafo
    attr_accessor :grafo
    def initialize
        @grafo = Hash.new()
        #Aqui creé un grafo de ejemplo
        self.insert(0,[1,6,8])
        self.insert(1,[0,4,6,9])
        self.insert(2,[4,6])
        self.insert(3,[4,5,8])
        self.insert(4,[1,2,3,5,9])
        self.insert(5,[3,4])
        self.insert(6,[0,1,2])
        self.insert(7,[8,9])
        self.insert(8,[0,3,7])
        self.insert(9,[1,4,7])
        #Este nodo, el 10, no es alcanzable desde ningun lado
        self.insert(10,[])
    end
    #En el diccionario de grafo, se colocan los pares clave/valor
    def insert(clave, valor)
        @grafo[clave] = valor
    end
end
#Definimos una clase busqueda. Esta clase ya tiene casi todo el comportamiento definido
#A excepcion del orden de busqueda que va a realizar, en todo caso, eso se define en DFS y BFS
class Busqueda
    #buscar setea las condiciones iniciales y devuelve realizar busqueda, que como tal es la que se encarga
    #de iniciar la busqueda
    def buscar(d, h)
        visitados_inicial = Array.new() << d
        if (d == h)
            return "Nodos recorridos 0"
        end
        return self.realizar_busqueda(d, h, 0, visitados_inicial, [])
    end
    #Realizar busqueda recibe el nodo inicial, el final, un contador que inicialmente es 0
    #Maneja un array de visitados que inicialmente solo tiene el nodo de partida, y nodos que es
    #un array donde se van guardando la cantidad de nodos recorridos cada vez que logra llegar al nodo
    def realizar_busqueda(d, h, count, visitados, nodos)
        #Tomamos el array de elementos de la variable global tipo Grafo (Decidi manejarla global por simplicidad)
        array_elementos = $g.grafo[d]
        #Basicamente pila_cola va a depender de si se trata de un DFS o de un BFS. Este comportamiento se da en la funcion
        #Orden definida en cada uno
        
        pila_cola = self.orden(array_elementos)
        #Si la pila_cola incluye el h, retornamos true
        if pila_cola.elements.include? h 
            nodos << count
        #En cualquier otro caso
        else
            #Recorremos la pila_cola mientras que no este vacias
            while not(pila_cola.vacio)
                #Tomamos un elemento
                elem = pila_cola.remover
                #Si el elemento todavia no ha sido visitado (no esta en el array de visitados)
                if not(visitados.include? elem)
                    #Lo ponemos en el array
                    visitados << elem
                    #Y llamamos recursivamente
                    realizar_busqueda(elem, h , count + 1 , visitados, nodos)
                end
            end
        end
        #Si el array de nodos nunca tuvo nada, esta vacio, entonces no era alcanzable. Retornamos -1
        if nodos.empty?
            return -1
        end
        #En otro caso, retornamos la cantidad de nodos recorridos
        #Es importante aclarar que solo retorna los recorridos para la primera vez que encontró el elemento
        #Si se quiere que retorne todos los caminos en los que lo encontró es tan sencillo como retornar
        #nodos en lugar de nodos[0]
        return "Nodos recorridos #{nodos[0]}"
    end
end
#DFS basicamente crea una pila con los elementos y la retorna
class DFS < Busqueda
    def orden(elementos)
        return Pila.new(elementos)
    end
end
#BFS basicamente crea una cola con los elementos y la retorna
class BFS < Busqueda
    def orden(elementos)
        return Cola.new(elementos)
    end
end

$g = Grafo.new

dfs = DFS.new()
bfs = BFS.new()

puts dfs.buscar(2,8)

puts bfs.buscar(2,8)