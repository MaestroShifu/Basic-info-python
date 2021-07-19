class Coche:
    marca = ''
    color = 'Blanco'
    # __ Sirve para encapsular como private
    __encendido = False
    velocidad = 0

    def __init__(self):
        pass

    def __init__(self, marca, color):
        self.color = color
        self.marca = marca

    def pintar(self, color):
        self.color = color

    def preder_apagar(self):
        self.__encendido = not self.__encendido

    def get_encender(self):
        return self.__encendido

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad


# Herencia multiple
'''
class Coche4x4(class1, class2):
    size_ruedas = 19
'''


# Manejo de herencia
class CocheDeportivo(Coche):
    cv = 60

    def __init__(self, marca, color, cv):
        Coche.__init__(marca, color)
        self.cv = cv