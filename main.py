import requests

# 1. Definimos la URL de prueba
url = "https://httpbin.org/get"

# 2. Realizamos la solicitud GET
response = requests.get(url)

# 3. Imprimimos el código de estado (200 significa OK / éxito)
print("Código de estado:", response.status_code)

# 4. Imprimimos el contenido de la respuesta en formato texto
print("Respuesta del servidor:")
print(response.text)
