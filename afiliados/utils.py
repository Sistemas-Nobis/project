import requests
import json
 
def actualizar_token_wise():
    """Obtiene un nuevo token desde la API y lo guarda."""
    url_token = 'https://api.wcx.cloud/core/v1/authenticate'
    query_params = {'user': 'apinobis'}
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': 'be9dd08a9cd8422a9af1372a445ec8e4',
    }
    try:
        response = requests.get(url_token, headers=headers, params=query_params)
        response.raise_for_status()  # Lanza un error si la solicitud falla
       
        # Imprimir la respuesta completa para verificar la estructura
        #print(f"Respuesta de la API: {response.text}")
       
        # Suponiendo que el token está en la clave 'token'
        response_json = response.json()
        token = response_json.get('token', None)
       
        if token:
            #print(f"Nuevo token obtenido y guardado: {token}")
            return token
        else:
            raise Exception("No se encontró el token en la respuesta.")
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el token: {e}")
 
 
def actualizar_token_gecros():
    url = "https://appmobile.nobissalud.com.ar/connect/token"
    payload = {
        'userName': '2|24588999',
        'password': 'wiseapi',
        'grant_type': 'password',
        'client_id': 'gecrosAppAfiliado'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    try:
        response = requests.post(url, data=payload,headers=headers)
        response.raise_for_status()  # Lanza un error si la solicitud falla
       
        # Imprimir la respuesta completa para verificar la estructura
        #print(f"Respuesta de la API: {response.text}")
       
        # Suponiendo que el token está en la clave 'access_token'
        response_json = response.json()
        token = response_json.get('access_token', None)
       
        if token:
            #print(f"Nuevo token obtenido y guardado: {token}")
            return token
        else:
            raise Exception("No se encontró el token en la respuesta.")
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el token: {e}")
        return None
    

def actualizar_preexistencias():
    url = "https://cotizador.nobis.com.ar/api/preex"

    headers = {
        "Content-Type": "application/json",
        'Authorization': 'Bearer 496ae7b9-0787-482e-bbe2-235279237940'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response_json = response.json()

        if response_json:
            # Obtén la clave dinámica
            dynamic_key = next(iter(response_json.keys()))  # Obtiene la primera clave
            data_to_save = response_json[dynamic_key]  # Extrae el contenido asociado a la clave

            # Guardar en un archivo JSON
            with open('home/static/preexistencias.json', 'w', encoding='utf-8') as json_file:
                json.dump(data_to_save, json_file, ensure_ascii=False, indent=4)

            print("Datos guardados en 'preexistencias.json'")
        else:
            raise Exception("No hay datos de preexistencias.")

    except requests.exceptions.RequestException as e:
        print(f"Error al renovar preexistencias: {e}")
        return None