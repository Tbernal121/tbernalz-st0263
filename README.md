# info de la materia: ST0263 - TÓPICOS ESPECIALES EN TELEMÁTICA <nombre>
#
# Estudiante: Tomás Bernal Zuluaga, tbernalz@eafit.edu.co
#
# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#
# Reto 1 y 2 P2P
#
# 1. breve descripción de la actividad#
<texto descriptivo>
Este proyecto evidencia un sistema P2P basada en servidor, el cual tiene como función compartir archivos, con un servidor central que actúa como directorio. Los peers, compuestos por un cliente y un servidor, interactúan entre sí y con el servidor central para la transferencia de archivos por medio de comunicación API REST y gRPC.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
En el proyecto se cumplió con requisitos tales como:
- Existe un servidor central que facilita el descubrimiento de peers y archivos. En el cual se implementa la autenticación de peers (login, logout)
- Consulta de recursos (query, sendIndex)
- Implementación de comunicación basada en API REST
- Uso de Docker para la creacion y despliegue de contenedores en el Server y despliegue en AWS Academy

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
No se logró establecer una conexión mediante gRPC entre el Pclient y el Pserver, por lo cual no se puede hacer upload, ni download de archivos. Por lo tanto tampoco se pudo dockerizar y desplegar el Pclient y el Pserver en AWS.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
-  **Información general diseño de alto nivel:** se implementó una red P2P basada en servidor, que usa un servidor central para ayudar a localizar y compartir archivos entre los peers. El servidor lleva un registro de los archivos y su ubicación. Cada peer tiene un cliente y un servidor, que gestionan los archivos y se comunican con el servidor central.
- **Arquitectura:** se utilizó API REST para la comunicación entre el servidor central y el Pclient debido a su simplicidad, eficiencia y escalabilidad. Por otro lado, gRPC se empleó para la comunicación entre el pclient y el pserver, ya que se tiene un alto rendimiento y velocidad.

![image](https://private-user-images.githubusercontent.com/88950619/309927139-3871d09c-99ed-4516-add9-d58cce54d182.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDk1OTM5NzUsIm5iZiI6MTcwOTU5MzY3NSwicGF0aCI6Ii84ODk1MDYxOS8zMDk5MjcxMzktMzg3MWQwOWMtOTllZC00NTE2LWFkZDktZDU4Y2NlNTRkMTgyLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAzMDQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMzA0VDIzMDc1NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTFhNjE0MDRjMDgyNmIyOTA5MzQ3OTkwYjljNjk4OGYzMTVhODQ1MjVmZWQzN2M1MDg3OGRlNjkyODVjMmIwMmYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.tNEhqVW1BgZPZkLMVnYaxFmreKV7IJYvTuYzS0eucqY)

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
- **Lenguaje de Programación:** Python 3.11.8

**Librerías:**
- grpcio: 1.62.01
- grpcio-tools: 1.62.02
- requests: 2.31.03
- fastapi: 0.109.24
- uvicorn: 0.27.15
- Flask: 3.0.26
- python-dotenv: 1.0.17

## Estructura de Directorios
- **Peer:** contiene los archivos relacionados con la funcionalidad del peer
    - Pclient: Contiene el código del cliente
    - Pserver: Contiene el código del servidor

- **Server:** contiene los archivos relacionados con el servidor central
    - dockerfile: Definición para construir la imagen Docker para el servidor central
    - main.py: Punto de entrada principal para el servidor central.
    - requirements.txt: Lista de dependencias necesarias para ejecutar el servidor central

# Referencias:
- **[gRPC](https://www.paradigmadigital.com/dev/grpc-que-es-como-funciona/)**
- **[Docker](https://docs.docker.com/)**
