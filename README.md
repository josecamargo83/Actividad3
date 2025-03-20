# 📌 REST API con Flask y MySQL

### ✨ Plataforma para la gestión de usuarios y publicaciones


## ✨ Descripción
Este repositorio contiene una API REST desarrollada en **Python** utilizando **Flask** y **MySQL**, que permite gestionar usuarios y publicaciones (CRUD: Create, Read, Update, Delete).

## 🌐 Tecnologías utilizadas
- **Python 3**
- **Flask**
- **Flask-CORS** (para permitir peticiones desde distintos orígenes)
- **Flask-Bcrypt** (para encriptación de contraseñas)
- **PyMySQL** (para conexión con MySQL)

## 📖 Estructura del proyecto
```
📦 tu-repositorio
 ┣ 📜 api.py         # Rutas para la gestión de usuarios
 ┣ 📜 posts.py       # Rutas para la gestión de posts
 ┣ 📜 conection.py   # Configuración de la conexión a la base de datos
 ┣ 📜 README.md      # Documentación del proyecto
```

## ⚙️ Instalación y configuración
### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/josecamargo83/Actividad3
```
### 2️⃣ Crear un entorno virtual (opcional)
```bash
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts ctivate
```
### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```
### 4️⃣ Configurar la base de datos
Ejecuta en MySQL:
```sql
CREATE DATABASE python;
```
Modifica `conection.py` si es necesario.

## 🛠 Uso de la API
### 🔹 Iniciar el servidor
```bash
python api.py
```
La API correrá en `http://127.0.0.1:5000/`

### 🔹 Endpoints disponibles
#### 📌 Usuarios
| Método | Endpoint          | Descripción            |
|--------|------------------|------------------------|
| GET    | `/users`         | Obtener todos los usuarios |
| POST   | `/users`         | Crear un nuevo usuario |
| PUT    | `/users/<id>`    | Actualizar un usuario  |
| DELETE | `/users/<id>`    | Eliminar un usuario    |

#### 📌 Publicaciones (Posts)
| Método | Endpoint         | Descripción            |
|--------|------------------|------------------------|
| GET    | `/posts`         | Obtener todos los posts |
| POST   | `/posts`         | Crear un nuevo post |
| PUT    | `/posts/<id>`    | Actualizar un post  |
| DELETE | `/posts/<id>`    | Eliminar un post    |

## 🔒 Seguridad y buenas prácticas
✅ **Cifrado de contraseñas:** Implementado con Flask-Bcrypt.  
✅ **Protección CORS:** Flask-CORS habilitado.  
✅ **Validaciones de datos:** Se recomienda usar Marshmallow o Flask-Validator.  
✅ **Autenticación:** Se recomienda implementar JWT con Flask-JWT-Extended.

## 📜 Licencia
Este proyecto está bajo la **Licencia MIT**.

## 👤 Autores
**Jose Camargo**, 
**Julian Venegas**, 
**German Gutierrez**, 
**Victor Yepes**
