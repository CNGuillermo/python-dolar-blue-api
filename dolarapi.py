##############################################################################################
# Para obtener el valor Dolar Blue
##############################################################################################

# la librería requests, que sirve para realizar consultas HTTP a sitios web y APIs.
import requests

# guardamos la dirección de la api como una variable
URL = "https://dolarapi.com/v1/dolares/blue" 


# Bloque try, si ocurre algún error Python saltará al bloque except
# posibles errores: no internet, API caída, error del servidor, problema de DNS
try:
    response = requests.get(URL, timeout=10) # busca el contenido de la web, esperando 10seg por la respuesta
    response.raise_for_status() # revisa si la respuesta fué exitosa, si no genera excepción y pasa al bloque except

    data = response.json() # la api devuelve json, esto lo transforma en diccionario Python
    valor_blue = data["venta"] # accedemos al campo venta = dolar blue

    print(f"Dólar Blue: ${valor_blue}") # muestra resultado en pantalla

except Exception as e: # si hubo un fallo, la variable e contiene el error ocurrido
    print(f"Error al obtener la cotización: {e}") # muestra el error ocurrido

input("\nPresione Enter para salir...")