class Animal:
    _totalAnimales = 0
    
    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero

    def movimiento(self):
        return "desplazamiento"

    @classmethod
    def totalPorTipo(cls):
        return f"Mamiferos: {len(Mamifero._listado)}\nAves: {len(Ave._listado)}\nReptiles: {len(Reptil._listado)}\nPeces: {len(Pez._listado)}\nAnfibios: {len(Anfibio._listado)}"

    def __str__(self):
        if self._zona != None:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona._nombre}, en el {self._zona._nombre}"
        else:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"