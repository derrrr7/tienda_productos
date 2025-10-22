# Tienda de Productos 🛍️

Aplicación web desarrollada con Django para la gestión de productos. Permite crear, visualizar, editar y eliminar productos con una interfaz pastelizada, responsiva y amigable.

## ✨ Funcionalidades

- CRUD completo usando vistas basadas en clases (CBVs)
- Carga y visualización de imágenes de productos
- Estética pastel personalizada con CSS
- Formularios armoniosos y responsivos
- Panel de administración de Django
- Validación de datos y pruebas locales

## 🧰 Requisitos

- Python 3.10 o superior
- Django 5.2
- Pillow (para manejo de imágenes)

## ⚙️ Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/derrrr7/tienda_productos.git
cd tienda_productos

python -m venv env
env\Scripts\activate  # En Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

🚀 Uso
Accede a las siguientes rutas en tu navegador:
http://localhost:8000/productos/ → Lista de productos
http://localhost:8000/productos/crear/ → Agregar nuevo producto
http://localhost:8000/productos/<id>/ → Ver detalle de producto
http://localhost:8000/productos/<id>/editar/ → Editar producto
http://localhost:8000/productos/<id>/eliminar/ → Eliminar producto

Autor: Derwin Viera Proyecto académico para práctica de Django y desarrollo web
