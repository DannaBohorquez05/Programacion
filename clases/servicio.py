from abc import ABC, abstractmethod
from clases.entidad import Entidad
from clases.excepciones import ServicioError

class Servicio(Entidad, ABC):

    def __init__(self, nombre, precio):

        if precio <= 0:
            raise ServicioError("Precio inválido")

        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def __init__(self, nombre, precio, horas):

        super().__init__(nombre, precio)

        if horas <= 0:
            raise ServicioError("Horas inválidas")

        self.horas = horas

    def calcular_costo(self):

        return self.precio * self.horas

    def descripcion(self):

        return f"Reserva de sala por {self.horas} horas"

    def mostrar_informacion(self):

        return self.descripcion()


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio, dias):

        super().__init__(nombre, precio)

        if dias <= 0:
            raise ServicioError("Días inválidos")

        self.dias = dias

    def calcular_costo(self):

        return self.precio * self.dias

    def descripcion(self):

        return f"Alquiler de equipo por {self.dias} días"

    def mostrar_informacion(self):

        return self.descripcion()


class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, precio, nivel):

        super().__init__(nombre, precio)

        self.nivel = nivel

    def calcular_costo(self):

        if self.nivel.lower() == "avanzada":
            return self.precio * 1.5

        return self.precio

    def descripcion(self):

        return f"Asesoría nivel {self.nivel}"

    def mostrar_informacion(self):

        return self.descripcion()