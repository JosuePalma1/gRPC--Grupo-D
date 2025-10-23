# Proyecto gRPC con PostgreSQL

Este proyecto utiliza una base de datos **PostgreSQL** para almacenar y gestionar los datos, junto con un servidor **gRPC** para la comunicación entre servicios.

---

## ⚙️ Configuración del entorno

Antes de ejecutar el proyecto, es necesario crear un archivo llamado `.env` en la raíz del repositorio.  
Este archivo contendrá las variables de entorno necesarias para la conexión con la base de datos.

### 🧩 Ejemplo de archivo `.env`

```env
# Dirección del host de la base de datos
# Puede ser localhost o 127.0.0.1 si la base de datos se ejecuta localmente
DB_HOST=localhost

# Puerto en el que PostgreSQL está escuchando (por defecto 5432)
DB_PORT=5432

# Nombre de la base de datos
DB_NAME=grpc

# Usuario con permisos para acceder a la base de datos
DB_USER=postgres

# Contraseña del usuario
DB_PASS=123
