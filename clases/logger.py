from datetime import datetime

def registrar_log(mensaje,tipo="INFO"):
    #Registra eventos del sitema en un archivo de logs

    with open("logs.txt", "a", encoding="utf-8") as archivo:

        archivo.write(f"[{datetime.now()}] [{tipo}] -> {mensaje}\n")