# 📌 Actividad 3 - API con Flask y MySQL

Este proyecto es una API RESTful desarrollada con Flask y MySQL para la gestión de usuarios y publicaciones. Proporciona endpoints para realizar operaciones CRUD sobre una base de datos.

## 📌 Tecnologías utilizadas

- Python 3
- Flask
- MySQL
- PyMySQL
- Flask-MySQL

## 📂 Estructura del proyecto

```
📦 Actividad3
│-- 📜 api.py          Gestión de usuarios (CRUD)
│-- 📜 conection.py    Conexión a la base de datos MySQL
│-- 📜 posts.py        Gestión de publicaciones (CRUD)
│-- 📜 requirements.txt Dependencias del proyecto
```

## 🚀 Instalación y ejecución

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/josecamargo83/Actividad3.git
cd Actividad3
```

### 2️⃣ Crear entorno virtual y activarlo

```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar base de datos MySQL

Crear la base de datos `python3` y la tabla `users` y `posts` con la siguiente estructura:

```sql
CREATE DATABASE python3;

USE python3;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

### 5️⃣ Ejecutar la API

```bash
python api.py
```

La API se ejecutará en `http://127.0.0.1:5000/`.

## 📡 Endpoints disponibles

### 📌 Gestión de usuarios

- **Obtener todos los usuarios:** `GET /users`
- **Crear un usuario:** `POST /users`
- **Actualizar un usuario:** `PUT /users/<user_id>`
- **Eliminar un usuario:** `DELETE /users/<user_id>`

### 📌 Gestión de publicaciones

- **Obtener todas las publicaciones:** `GET /posts`
- **Crear una publicación:** `POST /posts`
- **Actualizar una publicación:** `PUT /posts/<post_id>`
- **Eliminar una publicación:** `DELETE /posts/<post_id>`

## 📄 Licencia

Este proyecto está bajo la licencia MIT.

---

## 👤 Autores:

**Jose Camargo**,
**Julian Venegas**,
**German Gutierrez**,
**Victor Yepes**
