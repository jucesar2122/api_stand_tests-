import sender_stand_request
import data


# Función auxiliar para modificar el nombre en el cuerpo de la solicitud
def get_user_body(first_name):
    # Se copia el diccionario base definido en data.py
    current_body = data.user_body.copy()
    # Se actualiza el campo firstName con el nombre recibido
    current_body["firstName"] = first_name
    # Devuelve el cuerpo listo para la solicitud
    return current_body


# Prueba 1. Creación de un nuevo usuario con el nombre de 2 caracteres ("Aa")
def test_create_user_2_letter_in_first_name_get_success_response():
    # 1. Guarda el cuerpo de la solicitud con el nombre "Aa"
    user_body = get_user_body("Aa")

    # 2. Guarda el resultado de la solicitud para crear el usuario
    user_response = sender_stand_request.post_new_user(user_body)

    # 3. Comprueba si el código de estado es 201
    assert user_response.status_code == 201

    # 4. Comprueba que el campo authToken exista y no esté vacío
    assert user_response.json()["authToken"] != ""

    # 5. Obtiene los datos actuales de la tabla de usuarios
    users_table_response = sender_stand_request.get_users_table()

    # 6. Estructura el formato en texto del usuario tal como aparece en la tabla
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    # 7. Comprueba que el usuario exista exactamente 1 vez en la base de datos
    assert users_table_response.text.count(str_user) == 1

def test_create_user_2_letter_in_first_name_get_success_response():
        user_body = get_user_body("Aa")
        user_response = sender_stand_request.post_new_user(user_body)

        # Imprimir el código de estado y la respuesta
        print("\nCódigo de estado:", user_response.status_code)
        print("Respuesta JSON:", user_response.json())

        assert user_response.status_code == 201
        assert user_response.json()["authToken"] != ""
        # ... resto del código

import sender_stand_request
import data

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

# Prueba 1. Creación de un nuevo usuario o usuaria (2 caracteres)
def test_create_user_2_letter_in_first_name_get_success_response():
    user_body = get_user_body("Aa")
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    assert users_table_response.text.count(str_user) == 1

    # Prueba 2. Creación de un nuevo usuario o usuaria
    # El parámetro "firstName" contiene 15 caracteres

def test_create_user_15_letter_in_first_name_get_success_response():
        user_body = get_user_body("Aaaaaaaaaaaaaaa")
        user_response = sender_stand_request.post_new_user(user_body)

        assert user_response.status_code == 201
        assert user_response.json()["authToken"] != ""

        users_table_response = sender_stand_request.get_users_table()
        str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
                   + user_body["address"] + ",,," + user_response.json()["authToken"]

        assert users_table_response.text.count(str_user) == 1


def negative_assert_symbol(first_name):
    # 1. Obtiene el cuerpo actualizado con el nombre ingresado
    user_body = get_user_body(first_name)

    # 2. Guarda el resultado de la solicitud en la variable response
    response = sender_stand_request.post_new_user(user_body)

    # 3. Comprueba si el código de estado HTTP es 400
    assert response.status_code == 400

    # 4. Comprueba si el atributo "code" en el cuerpo de la respuesta es 400
    assert response.json()["code"] == 400

    # 5. Comprueba si el mensaje de error es exactamente el esperado
    assert response.json()["message"] == "Has introducido un nombre de usuario no válido. " \
                                         "El nombre solo puede contener letras del alfabeto latino, " \
                                         "la longitud debe ser de 2 a 15 caracteres."

    # Prueba 3. Error cuando el nombre tiene 1 carácter (menor al mínimo permitido)


def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")

    # Prueba 3. Error
    # El parámetro "firstName" contiene un carácter


def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")

    # Prueba 4. Error
    # El parámetro "firstName" contiene 16 caracteres
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")

# Prueba 5. Error cuando el nombre contiene espacios
def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("A Aaa")

    # Prueba 6. Error cuando el nombre contiene caracteres especiales


def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\"")

    # Prueba 7. Error cuando el nombre contiene números
def test_create_user_has_number_in_first_name_get_error_response():
        negative_assert_symbol("123")

def negative_assert_no_firstname(user_body):
    # 1. Guarda la respuesta de la solicitud en la variable response
    response = sender_stand_request.post_new_user(user_body)

    # 2. Comprueba si la respuesta contiene el código 400
    assert response.status_code == 400

    # 3. Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

    # 4. Comprueba el mensaje de error esperado
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"


# Prueba 8. Error cuando no se envía el parámetro "firstName"


def test_create_user_no_first_name_get_error_response():
    # Copia el cuerpo predeterminado de data.py
    user_body = data.user_body.copy()
    # Elimina el parámetro firstName
    user_body.pop("firstName")

    # Llama a la función auxiliar
    negative_assert_no_firstname(user_body)


# Prueba 9. Error cuando el parámetro "firstName" está vacío
def test_create_user_empty_first_name_get_error_response():
    # Obtiene el cuerpo con el nombre vacío ""
    user_body = get_user_body("")

    # Llama a la función auxiliar
    negative_assert_no_firstname(user_body)

# Prueba 10. Error
# El tipo del parámetro "firstName" es un número
def test_create_user_number_type_first_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(12)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    response = sender_stand_request.post_new_user(user_body)

    # Comprobar el código de estado de la respuesta
    assert response.status_code == 400

