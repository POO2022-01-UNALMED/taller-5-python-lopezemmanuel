from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    def movimiento(self):
        return "volar"

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")

    @classmethod
    def getListado(cls):
        return cls._listado

    def getColorPlumas(self):
        return self._colorPlumas

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas