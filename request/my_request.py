import copy

import requests
import json
from models.response import Response


def my_request(url, params, method='GET'):
    try:
        if method.upper() == 'GET':
            risposta = requests.get(url, params=params)
        elif method.upper() == 'POST':
            risposta = requests.post(url, data=params)
        else:
            raise ValueError("Metodo non supportato. Utilizza 'GET' o 'POST'.")

        # Verifica se la richiesta ha avuto successo (status code 2xx)
        risposta.raise_for_status()
        return Response(risposta.headers, json.loads(risposta.text))

    except requests.exceptions.RequestException as e:
        print(f"Errore nella chiamata HTTP: {e}")
        return None

