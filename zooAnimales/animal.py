class Animal:
    _totalAnimales = 0
    
    def __init__(self, nombre, edad, habitat, genero, zona=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona

    def movimiento(self):
        return "desplazarse"

    @classmethod
    def totalPorTipo(cls):
        return f"Mamiferos: {len(cls.Mamifero._listado)}\nAves: {len(cls.Ave._listado)}\nReptiles: {len(cls.Reptil._listado)}\nPeces: {len(cls.Pez._listado)}\nAnfibios: {len(cls.Anfibio._listado)}"

    def toString(self):
        if self._zona != None:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona._nombre}, en el {self._zona._nombre}"
        else:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero

    def setNombre(self, nombre):
        self._nombre = nombre
    
    def setEdad(self, edad):
        self._nombre = edad

    def setHabitat(self, habitat):
        self._nombre = habitat

    def setGenero(self, genero):
        self._nombre = genero

    