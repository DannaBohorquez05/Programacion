from clases.entidad import Entidad
from clases.excepciones import ClienteError

class Cliente(Entidad):

    def __init__(self, nombre, correo, telefono):

        self.set_nombre(nombre)
        self.set_correo(correo)
        self.set_telefono(telefono)

    def set_nombre(self, nombre):

        if not nombre.strip():
            raise ClienteError("El nombre no puede estar vacío")

        self.__nombre = nombre

    def set_correo(self, correo):

        if "@" not in correo:
            raise ClienteError("Correo inválido")

        self.__correo = correo

    def set_telefono(self, telefono):

        if not telefono.isdigit():
            raise ClienteError("El teléfono debe tener solo números")

        self.__telefono = telefono

    def get_nombre(self):

        return self.__nombre

    def mostrar_informacion(self):

        return f"Cliente: {self.__nombre}"