# Renacer con Color

## Descripción

Renacer con Color es una plataforma web desarrollada con Flask y MySQL que permite administrar cursos de pintura. Los usuarios pueden consultar cursos, acceder a materiales de aprendizaje, explorar una galería de obras, subir sus propios trabajos e iniciar sesión según su rol.

## Objetivo
Desarrollar una aplicación web para la gestión de cursos de pintura que facilite el acceso a materiales, la administración de participantes y la interacción entre alumnos y administradores.

## Tecnologías utilizadas
- Python
- Flask
- MySQL
- HTML5
- CSS3


## Funcionalidades
- Página de inicio.
- Inicio de sesión para usuarios y administradores.
- Panel de administración (Dashboard).
- Consulta de cursos.
- Acceso a materiales de apoyo.
- Galería de obras.
- Subida de obras por los participantes.
- Gestión y edición de participantes.
- Ejemplos de paisajes.
- Almacenamiento de archivos PDF y presentaciones.

## Estructura del proyecto

```
RENACER_CON_COLOR/
│── app.py
│── README.md
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── img/
│   └── presentaciones/
│
├── templates/
│   ├── index.html
│   ├── cursos.html
│   ├── materiales.html
│   ├── galeria.html
│   ├── participantes.html
│   ├── subir_obra.html
│   ├── login.html
│   ├── login_usuario.html
│   ├── login_admin.html
│   ├── dashboard.html
│   ├── editar_participante.html
│   ├── ejemplos_paisajes.html
│   └── base.html
```

## Instalación

1. Clonar o descargar el proyecto.
2. Instalar las dependencias:

```bash
pip install flask
pip install flask-mysqldb
```

3. Crear la base de datos correspondiente en MySQL.
4. Configurar la conexión en `app.py`.
5. Ejecutar el proyecto:

```bash
python app.py
```

6. Abrir el navegador en:

```
http://127.0.0.1:5000
```

## Autor

**Equipo 03**

## Licencia

Proyecto desarrollado con fines académicos para el CECyTE.