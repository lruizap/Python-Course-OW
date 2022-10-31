# Para crear un objeto tendremos que usar la palabra clave "class"

import math


class Punto():

    # Para definir los atributos del objeto usamos el contructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        # self => representa el atributo del objeto

    # Para que una función haga algo con el objeto creado, tendremos que pasarle por parámetros "self"
    # "self" tendra los atrubutos del primer objeto que hemos pasado
    def mostrar(self):
        return str(self.x) + ":" + str(self.y)

    # Para que una función compare 2 objetos de la misma clase debemos pasarselo.
    # Ese objeto con el que queremos comparar se creará con el contructor, por tanto, tendrá los miis atributos que self
    def distancia(self, otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        return math.sqrt((dx*dx + dy*dy))

# Las clases, al igual que las funciones se pueden importar entre archivos


punto1 = Punto(0, 0)
punto2 = Punto(4, 5)
print(f"({punto1.x}:{punto1.y})", f"({punto2.x}:{punto2.y})")
# Podemos mostrar los atributos por separado o usar uno de los métodos incluidos en la clase para mostrar el punto entero
print(punto1.mostrar(), punto2.mostrar())
# Para calcular la distancia con otro punto usaremos la funcion que hemos creado.
# Para comparar dos objetos, usaremos el objeto origen, punto1, y usando este, llamaremos a la función que le pasaremos por parámetro el segundo objeto, punto2
print(punto1.distancia(punto2))


# En las clases podemos tener atributos privados, estos comenzarán con dos "__" antes del nombre del atributo y no podremos acceder a ellos desde fuera de la clase
class Alumno():
    def __init__(self, nombre="", __DNI=""):
        self.nombre = nombre
        self.__DNI = __DNI


a1 = Alumno("Paco", "4531855T")
print(a1.nombre)
# print(a1.__DNI)  # No podremos acceder al atributo privado

# Para controlar los atributos de los objetos usaremos los getters y setters

# Controlaremos que ningún usuario pueda intorducir un radio negativo


class Circulo():
    def __init__(self, radio):
        self.radio = radio

    @property
    # Es el método getters => se ejecuta la función cada vez que obtengamos el valor del radio
    # Cada vez que queramos acceder al valor del radio, se ejecutará esta función.
    # Es decir, nosotros controlaremos la salida de los atributos del objeto
    def radio(self):
        print("Estoy dando el radio")
        return self.__radio

    @radio.setter
    # Cada vez que cambie el valor del radio ejecuta esta función
    # Con este tipo de constructores, en el constructor principal del objeto no  dnremos que especificar que es un atributo privado, puesto que cada vez que cambia el valor del atributo o se quiere acceder a él, se accede a estas funciones
    def radio(self, radio):
        if radio >= 0:
            self.__radio = radio
        else:
            print("Radio debe ser positivo")
            self.__radio = 0


print()

c1 = Circulo(5)
print(c1.radio)

print()

c1.radio = 27
print(c1.radio)

print()

c1.radio = -2
print(c1.radio)

print()

# herencia nos permite crear una clase a partir de otra clase


class Punto3d(Punto):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        # Esta función me hace referencia a la clase madre, por tanto, no tendremos que inicializar los atributos de la clase madre, solamente de la clase nueva
        self.z = z

    @property
    def z(self):
        print("Doy z")
        return self.__z

    @z.setter
    def z(self, z):
        print("Cambio z")
        self.__z = z

    def mostrar(self):
      # Aqui usamos el método de la clase anterior, y como lo que devuelve es una string, lo podemos tratar como tal para concatenar strings
        return super().mostrar()+":"+str(self.__z)

    def distancia(self, otro):
      # El método distancia si tenemos que modificarlo porque ha cambiado los puntos y por tanto la distancia anterior no nos sirve ahora
        dx = self.__x - otro.__x
        dy = self.__y - otro.__y
        dz = self.__z - otro.__z
        return (dx*dx + dy*dy + dz*dz)**0.5


# Delegación, con este método podemos introducir en una nueva clase objetos de otras clases como atributos

class circulo2():

    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def mostrar(self):
        return "Centro:{0}-Radio:{1}".format(self.centro.mostrar(), self.radio)


punto3 = Punto(3, 3)
c2 = circulo2(punto3, 5)
print(c2.mostrar())
