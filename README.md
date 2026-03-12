# Task Management API

API REST para gestión de tareas desarrollada con Django REST Framework, autenticación JWT y contenedores Docker.

## Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- JWT Authentication
- PostgreSQL
- Docker
- Docker Compose

## Funcionalidades

- Autenticación con JWT
- Crear tareas
- Listar tareas
- Ver una tarea específica
- Actualizar tareas
- Eliminar tareas

## Requisitos

- Docker
- Docker Compose

## Instalación y ejecución

Clonar el repositorio:

git clone https://github.com/TU_USUARIO/task-api.git

Entrar al proyecto:

cd task-api

Levantar los contenedores:

docker-compose up --build

Aplicar migraciones:

docker-compose exec web python manage.py migrate

Crear usuario administrador:

docker-compose exec web python manage.py createsuperuser

Servidor disponible en:

http://localhost:8000

## Endpoints

### Autenticación

POST /signin/

Body:

{
"username": "usuario",
"password": "password"
}

### Crear tarea

POST /tasks/

### Listar tareas

GET /tasks/

### Ver tarea

GET /tasks/{id}/

### Actualizar tarea

PATCH /tasks/{id}/

### Eliminar tarea

DELETE /tasks/{id}/

## Estados de tarea

pending  
in_progress  
done

## Autor

Benjamin Becerra