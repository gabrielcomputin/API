import requests
#Importamos la biblioteca requests, que permite hacer solicitudes HTTP en Python
from dotenv import load_dotenv
#Importamos la función load_dotenv de la biblioteca python-dotenv, que sirve para cargar variables de entorno desde un archivo .env.
import os
#Importamos el módulo os, que permite acceder a funcionalidades del sistema operativo, como obtener variables de entorno.

def load_variable():
    #Definimos una función llamada load_variable que será usada para cargar las variables de entorno necesarias.
    try:
        load_dotenv()

        #Intentamos cargar las variables de entorno desde un archivo .env.

        api_key = os.getenv("API_KEY")
        search_engine_id = os.getenv("ENGINE_ID")

        #Obtenemos las variables API_KEY y ENGINE_ID del entorno. Estas son necesarias para acceder a la API de búsqueda personalizada de Google.

        if not api_key:
            return ValueError("No se encontro el api key")
        if not search_engine_id:
            return ValueError("No se encontro el search engine id")
        
        #Verificamos si las variables están presentes. Si no, devuelve un error usando ValueError

        print(f"Tus variables de entorno son el api key: {api_key} y search engine id: {search_engine_id}")

        #Mostramos las variables en consola

        return api_key, search_engine_id
        #COn return, retornamos ambas variables si todo está correcto.

    except ValueError as e:
        print(e)
        return None
    
    #Con estos comandos, capturamos y mostramos cualquier error tipo ValueError, y retorna a None.

def requestAPI(api_key, search_engine_id):

    #Definimos la función que hará la solicitud a la API de Google.

    try:
        query =  'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'
        page = 1
        lang = "lang_es"

        #Establecemos los parametros de busqueda
        #Query para los archivos, page para el nro de pagina y lang para el lenguaje

        url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}&start={page}&lr={lang}"

        #Construimos la URL para la API de Google Custom Search con los parámetros incluidos.

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"data: {data}")
        
        #Realizamos la solicitud HTTP GET a la URL especificada y si la respuesta es exitosa, convierte los datos de la respuesta a formato JSON y los imprime.
        
        else:
            return ValueError("Algo salio mal con la solicitud")
        
        #Si hay un error en la respuesta, devuelve un ValueError.
        
    except ValueError as e:
        print(e)
        return None
    
    #con except, manejamos errores de tipo ValueError e imprime el mensaje.

def main():
    api_key, search_engine_id = load_variable()
    requestAPI(api_key, search_engine_id)

    #Definimos la función principal que carga las variables de entorno y luego hace la solicitud a la API.

if __name__ == "__main__":
    main()

    #Con esto verificamos si el script se está ejecutando directamente (y no importado como módulo).