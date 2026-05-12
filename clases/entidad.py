#Clase base abstracta del sistema
#Define el metodo obligatorio de mostrar información

from abc import ABC, abstractmethod

class Entidad(ABC):

    @abstractmethod
    def mostrar_informacion(self):
        pass