from abc import ABC, abstractmethod
from clases.entidad import Entidad
from clases.excepciones import ServicioError
from clases.logger import registrar_log

# Modulo de servicios del sistema
# Implementa herencia y polimorfismo para diferentes tipos de servicios

class Servicio(Entidad, ABC):

    def __init__(self, nombre, precio):
        
        #Validacion de precio
        if precio <= 0:
            raise ServicioError("El precio debe ser mayor a 0")

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
        
        # validacion de horas
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
        
        # Validación de dias
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
        
        #Normalzación de nivel
        self.nivel = nivel.lower()

    def calcular_costo(self):
        
        if self.nivel == "avanzada":
            return self.precio * 1.5
    
        return self.precio

    def descripcion(self):
        
        return f"Asesoria nivel {self.nivel}"
    
    def mostrar_informacion(self):
        
        return self.descripcion()