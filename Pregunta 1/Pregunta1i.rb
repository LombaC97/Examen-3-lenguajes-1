#En ruby no existen clases abstractas como tal, pero podemos simular una clase
#que define estos métodos, sin embargo, no incluye comportamiento
class Secuencia
    #@abstract
    def agregar
        raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
    end
    def remover
        raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
    end
    def vacio
        raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
    end
end
#Pila hereda de Secuencia, y va a tener un array de elements que básicamente va a representar la pila
class Pila < Secuencia
    attr_accessor :elements
    #Inicializamos el array de los elementos, y por cada elemento que tenga el array con el que se crea,
    #se llama a la funcion de agregar para que los agregue en el orden similar a una pila
    def initialize(elementos)
        @elements = []
        elementos.each {|element| self.agregar(element)}
    end
    #Agregamos elementos al final
    def agregar(elemento)
        @elements << elemento
    end
    #Removemos elementos del final
    def remover
        return @elements.pop
    end
    #Devuelve si el @elements esta vacio
    def vacio
        return @elements.empty?
    end
end
#Cola hereda de Secuencia, y va a tener un array de elements que básicamente va a representar la cola
class Cola < Secuencia
    attr_accessor :elements
    #Inicializamos el array de elementos, basicamente llamamos a la función de agregar por cada elemento 
    #para que lo agregue similar a una cola
    def initialize(elementos)
        @elements = []
        elementos.each {|element| self.agregar(element)}
    end
    #Agregamos los elementos al principio
    def agregar(elemento)
        @elements.insert(0,elemento)
    end
    #Removemos los elementos del final
    def remover
        return @elements.pop
    end
    #Retornamos si la cola esta vacia
    def vacio
        return @elements.empty?
    end
end
