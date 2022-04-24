from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)
    
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        cls.caballos += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)

    @classmethod
    def getListado(cls):
        return cls._listado

    def isPelaje(self):
        return self._pelaje

    def getPatas(self):
        return self._patas

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def setPatas(self, patas):
        self._patas = patas