class MenorEdadException(Exception):
    pass
class Persona():
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        if self.edad< 18:
            raise MenorEdadException