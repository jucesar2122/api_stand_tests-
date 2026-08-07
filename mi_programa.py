import requests

# 1. URL base de TripleTen (sin la barra final)
url_base = "https://cnt-4ab872f4-5f80-42e2-bfe0-7ef6461190bc.containerhub.tripleten-services.com"

# 2. La ruta que te dio el ejercicio
CREATE_USER_PATH = "/api/v1/users/"

# 3. Concatenamos ambas para formar la URL completa
url = url_base + CREATE_USER_PATH

# 4. Encabezados de la solicitud
headers = {
    "Content-Type": "application/json"
}

# 5. Cuerpo de la solicitud
payload = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

# 6. Enviar la solicitud POST
respuesta = requests.post(url, json=payload, headers=headers)

# 7. Ver el resultado
print("URL enviada:", url)
print("Código de estado:", respuesta.status_code)

try:
    print("Respuesta del servidor:", respuesta.json())
except Exception:
    print("Respuesta (texto plano):", respuesta.text)