import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


def mostrar_respuesta(response):
    print(f"Código de estado: {response.status_code}")
    try:
        print("Respuesta:")
        print(response.json())
    except ValueError:
        print("Respuesta:")
        print(response.text)
    print("-" * 60)


def ejecutar_crud():
    try:
        # GET: obtener posts y mostrar los primeros 2
        print("1. GET - Primeros 2 posts")
        response = requests.get(f"{BASE_URL}/posts", timeout=TIMEOUT)
        response.raise_for_status()

        print(f"Código de estado: {response.status_code}")
        posts = response.json()
        print("Primeros 2 posts:")
        for post in posts[:2]:
            print(post)
        print("-" * 60)

        # POST: crear un nuevo post
        print("2. POST - Crear un nuevo post")
        nuevo_post = {
            "title": "Post creado con Python",
            "body": "Prueba de operación POST usando requests.",
            "userId": 1
        }

        response = requests.post(
            f"{BASE_URL}/posts",
            json=nuevo_post,
            timeout=TIMEOUT
        )
        mostrar_respuesta(response)

        # PUT: actualizar el post con ID 1
        print("3. PUT - Actualizar el post con ID 1")
        post_actualizado = {
            "id": 1,
            "title": "Post actualizado con Python",
            "body": "Contenido actualizado mediante PUT.",
            "userId": 1
        }

        response = requests.put(
            f"{BASE_URL}/posts/1",
            json=post_actualizado,
            timeout=TIMEOUT
        )
        mostrar_respuesta(response)

        # DELETE: eliminar el post con ID 1
        print("4. DELETE - Eliminar el post con ID 1")
        response = requests.delete(
            f"{BASE_URL}/posts/1",
            timeout=TIMEOUT
        )
        mostrar_respuesta(response)

    except requests.exceptions.Timeout:
        print("Error: la solicitud excedió el tiempo de espera.")
    except requests.exceptions.ConnectionError:
        print("Error: no fue posible establecer conexión con la API.")
    except requests.exceptions.HTTPError as error:
        print(f"Error HTTP: {error}")
    except requests.exceptions.RequestException as error:
        print(f"Error en la solicitud: {error}")
    except Exception as error:
        print(f"Error inesperado: {error}")


if __name__ == "__main__":
    ejecutar_crud()
