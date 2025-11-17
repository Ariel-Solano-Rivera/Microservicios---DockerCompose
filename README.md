# Microservicio con Docker Compose  
## Ejemplo de Gestión de Países con FastAPI + PostgreSQL

Este proyecto muestra cómo implementar un **microservicio de gestión de países** utilizando **FastAPI**, conectado a una base de datos **PostgreSQL**, y orquestado mediante **Docker Compose**.  
Es un ejemplo perfecto para comprender cómo trabajar con múltiples contenedores conectados entre sí bajo una arquitectura de microservicios.

---

# Descripción del Proyecto

Este microservicio permite gestionar una lista de países almacenados en una base de datos PostgreSQL.  
La API está construida con **FastAPI** y se ejecuta dentro de un contenedor Docker, mientras que la base de datos se ejecuta en otro contenedor independiente. Ambos contenedores se comunican mediante la red interna creada automáticamente por **Docker Compose**.

## ¿Qué hace tu microservicio?
- Inserta un país aleatorio en la base de datos cada vez que se accede al endpoint principal (`/`).
- Devuelve una lista completa de países almacenados en la base de datos.
- Presenta los datos tanto en formato HTML como en formato JSON.

## ¿Qué tecnología usa?
- **FastAPI** para construir la API.
- **PostgreSQL** como base de datos.
- **Docker** para contener el microservicio.
- **Docker Compose** para orquestar y conectar los contenedores.

## ¿Cómo se comunican los contenedores?
- El contenedor de la API se conecta al contenedor de la base de datos usando el hostname `db`, definido dentro del archivo `docker-compose.yml`.
- Ambos servicios están dentro de la misma red interna creada por Docker Compose, lo que permite comunicación directa sin exponer puertos innecesarios.

## ¿Qué endpoints tiene?

### `/`
- Inserta un país aleatorio en la BD.
- Devuelve una página HTML con una tabla de países.

### `/datos`
- Devuelve la lista completa de países en **formato JSON**.

## ¿Qué devuelve?

- **HTML** con tabla de países al visitar `/`
- **JSON** con todos los registros al visitar `/datos`
- **Swagger automático** disponible en `/docs`

---

# Estructura del Proyecto
```bash
app/
├── main.py
├── requirements.txt
docker-compose.yml
Dockerfile
init.sql
```

# ¿Cómo ejecutar este proyecto?

Sigue estos pasos después de clonar el repositorio:

### 1. Clonar el repositorio
```bash
git clone <URL-del-repo>
cd <nombre-del-proyecto>
```
## 2. Construir las imágenes
```bash
docker-compose build
```
## 3. Levantar los servicios
```bash
docker-compose up -d
```

## 4. Acceder a la aplicación

Página HTML:
http://localhost:8000/

Datos en JSON:
http://localhost:8000/datos

## 5. Para detener el sistema
```bash
docker-compose down
```
# Comandos usados (Docker Compose)

## Construir imágenes
```bash
docker-compose build
```
**Descripción:**
Este comando construye las imágenes Docker de todos los servicios definidos en el archivo docker-compose.yml, leyendo el contenido del Dockerfile para generar la imagen del microservicio.
**Úsalo cuando:**

Cambias main.py

Cambias Dockerfile

Modificas requirements.txt

## Levantar los servicios

```bash
docker-compose up -d
```

**Descripción:**
Levanta tanto la API como la base de datos en segundo plano.

## Ver el estado de los contenedores

```bash
docker-compose ps
```

**Descripción:**
Muestra contenedores activos, sus puertos y nombres.

## Detener y eliminar los servicios

```bash
docker-compose down
```

**Descripción:**
Detiene todos los contenedores iniciados con Compose y elimina la red interna.
