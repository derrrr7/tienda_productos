# Tienda de Productos 🛍️

Aplicación web desarrollada con Django para la gestión de productos. Permite crear, visualizar, editar y eliminar productos con una interfaz pastelizada y amigable.

## ✨ Funcionalidades

- CRUD completo usando vistas basadas en clases (CBVs)
- Carga y visualización de imágenes
- Estética pastel personalizada con CSS
- Formularios armoniosos y responsivos
- Panel de administración de Django

## 🧰 Requisitos

- Python 3.10+
- Django 5.2+
- Pillow (para imágenes)

## ⚙️ Instalación

```bash
git clone https://github.com/derrrr7/tienda_productos.git
cd tienda_productos
python -m venv env
env\Scripts\activate

Accede a http://localhost:8000/productos/ para ver la lista de productos.
Usa http://localhost:8000/productos/crear/ para agregar nuevos productos.
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
