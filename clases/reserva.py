from clases.excepciones import ReservaError
from clases.logger import registrar_log

#Clase que gestiona las reservas del sistema
#Controla estados,validaciones y procesamiento del costo

class Reserva:

    def __init__(self, cliente, servicio, duracion):

#Validacion de duración
        if duracion <= 0:
            raise ReservaError("La duración debe ser mayor a 0")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "PENDIENTE"

    def confirmar(self):

        self.estado = "CONFIRMADA"

    def cancelar(self):

        self.estado = "CANCELADA"

    def procesar_reserva(self):

        try:
            #Calculo del costo del servicio
            costo = self.servicio.calcular_costo()
            
            #Validación del costo
            if costo <= 0:
                raise ReservaError("Costo inválido en la reserva")
            
            #Confirmar reserva
            self.confirmar()
            
            #Registrar evento en logs
            registrar_log(f"Reserva confirmada para {self.cliente.get_nombre()}")
            
            return costo

        except Exception as e:
            registrar_log(f"Error procesando reserva:{str(e)}")
            
            raise ReservaError("Error procesando reserva") from e
        
    #Metodo opcional para consultar estado
    def estado_actual(self):
        
        return self.estado