from clases.excepciones import ReservaError

class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ReservaError("Duración inválida")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):

        self.estado = "Confirmada"

    def cancelar(self):

        self.estado = "Cancelada"

    def procesar_reserva(self):

        try:

            costo = self.servicio.calcular_costo()

            if costo <= 0:
                raise ReservaError("Costo inválido")

            self.confirmar()

            return costo

        except Exception as e:

            raise ReservaError("Error procesando reserva") from e