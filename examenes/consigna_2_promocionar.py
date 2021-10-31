from datetime import datetime 
from datetime import timedelta
from datetime import date
import pandas

def primeros_jueves():
    """
    '%A' sirve para extraer el nombre del dia. En este caso, importan los jueves solamente ("Thursday")
    timedelta sirve para calcula la distancia entre dos fechas
    """
    fecha_inicial  = date(1970, 1, 1) # fecha de la consigna
    fecha_hoy      = date.today() # fecha de hoy
    lista_dias     = pandas.date_range(fecha_inicial, fecha_hoy - timedelta(days=1), freq='d') # armo una lista de los dias entre ambas fechas
    jueves_primero = [d for d in lista_dias if d.strftime("%A") == "Thursday" and d.strftime("%d") == "01"] # doble condicion: que sea jueves y primero
    cantidad_jueves_primeros = len(jueves_primero) # contador de jueves primeros
    return cantidad_jueves_primeros
    
primeros_jueves()