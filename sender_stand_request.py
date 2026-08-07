import configuration
import requests
import data

# Solicitud POST para crear un nuevo usuario
def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )

# Solicitud GET para obtener la tabla de usuarios
def get_users_table():
    return requests.get(
        configuration.URL_SERVICE + configuration.USERS_TABLE_PATH
    )