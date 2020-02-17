# Herencia
class Nave:
    def __init__(self, nombre, distancia):
        self.nombre = nombre
        self.distancia = distancia

    def lanzamiento(self):
        return "%s se ha lanzado %s" % (self.nombre, self.distancia)


class RoverCuriosity(Nave): # Herencia de la clase base.
    def __init__(self, nombre, distancia, fabricante):
        Nave.__init__(self, nombre, distancia)
        self.fabricante = fabricante

    def get_fabricante(self):
        return "%s Lanzado por %s" % (self.nombre, self.fabricante)


if __name__ == "__main__":
    x = Nave("Nave Espacial", "hacia la atmosfera")
    y = RoverCuriosity("Rover", "hacia marte", "ISRO")
    print(x.lanzamiento())
    print(y.lanzamiento())
    print(y.get_fabricante())

#Composición

class RoverComp():
    def __init__(self, nombre, distancia, fabricante):
        self.nave = Nave(nombre, distancia) # Instanciando.
        self.fabricante = fabricante

    def get_fabricante(self):
        return "%s Lanzando por %s" % (self.nave.nombre, self.fabricante)


if __name__ == "__main__":
    z = RoverCuriosity("Rover 2", "hacia marte", "ISRO")
    print(z.lanzamiento())
    print(z.get_fabricante())
