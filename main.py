#-----------------------------------------------------------------
#SISTEMA INTEGRAL DE GESTION DE RESERVAS
#-----------------------------------------------------------------
#Empresa: InnovaTech
#Proyecto desarrollado en Python
#Programacion orientada a objetos(POO)
#Incluye gestión de clientes,servicios y reservas
#-----------------------------------------------------------------

#Importacion de clases de reservas

from clases.cliente import Cliente
from clases.servicio import ReservaSala
from clases.servicio import AlquilerEquipo
from clases.servicio import AsesoriaEspecializada
from clases.reserva import Reserva
from clases.logger import registrar_log


#Listas del sitema de gestión

clientes = []
servicios = []
reservas = []

print("========== SOFTWARE FJ ==========")

# OPERACION 1
#Registro de cliente valido

try:

    cliente1 = Cliente("Juan Perez", "juan@gmail.com", "3001234567")
    clientes.append(cliente1)

    print("Cliente registrado correctamente")
    registrar_log("Cliente Juan registrado")

except Exception as e:

    registrar_log(str(e))

# OPERACION 2
# Prueba de cliente con datos invalidos

try:

    cliente2 = Cliente("", "correo", "abc")
    clientes.append(cliente2)

except Exception as e:

    print("Error en cliente inválido")
    registrar_log(str(e))

# OPERACION 3
try:
    
    sala = ReservaSala("Sala VIP",120,5)
    servicios.append(sala)
    
    print ("Servicio sala registrado")
    registrar_log("Sala registrada")
    
except Exception as e:
    registrar_log(str(e))
    

# OPERACION 4
try:

    equipo = AlquilerEquipo("Portátil Gamer", 80, 3)
    servicios.append(equipo)

    print("Equipo registrado")
    registrar_log("Equipo registrado")

except Exception as e:

    registrar_log(str(e))

# OPERACION 5
try:
    asesoria= AsesoriaEspecializada("Inteligencia Artificial",200,"avanzada")
    servicios.append(asesoria)
    
    print ("Asesoria registrada")
    registrar_log("Asesoria registrada")
    
except Exception as e:
    registrar_log(str(e))
    

# OPERACION 6
try:

    servicio_error = ReservaSala("Sala Error", -10, 0)

except Exception as e:

    print("Error creando servicio")
    registrar_log(str(e))

# OPERACION 7
# Creación y procesamiento de reservas de servicio

try:
    
    reserva1 = Reserva(cliente1,sala,5)
    reservas.append(reserva1)
    
    total=reserva1.procesar_reserva()
    
    print("Reserva procesada correctamente")
    print("costo:", total)
    
    registrar_log("Reserva exitosa")
    
except Exception as e:
    
    registrar_log(str(e))
    

# OPERACION 8
try:

    reserva2 = Reserva(cliente1, equipo, -1)

except Exception as e:

    print("Reserva inválida")
    registrar_log(str(e))

# OPERACION 9
try:

    reserva3 = Reserva(cliente1, asesoria, 2)

    reservas.append(reserva3)

    total = reserva3.procesar_reserva()

    print("Reserva asesoría exitosa")
    print("Costo:", total)

    registrar_log("Reserva asesoría exitosa")

except Exception as e:

    registrar_log(str(e))

# OPERACION 10
try:

    cliente3 = Cliente("Ana", "ana.com", "999")

except Exception as e:

    print("Cliente inválido")
    registrar_log(str(e))

finally:

    print("Sistema funcionando correctamente")
    
    #Resumen final del sistema de gestion
    
    print("\n============= RESUMEN DEL SISTEMA =====================")
    print(f"Clientes registrados:{len(clientes)}")
    print(f"Servicios Creados:{len(servicios)}")
    print(f"Reservas realizadas:{len(reservas)}")
    print("sistema funcionando correctamente")