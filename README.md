# Django Testapp

Una aplicación web básica escrita en Django para ejecutar pruebas de paquetes, despliegue, etc.

No haga pruebas sobre las ramas principales (master y develop), manténgalas lo más limpias posible, 
si desea implementar una prueba cree una rama nueva, trabaje localmente y si la prueba es de valor 
sincronicela al repositorio sin integrarla a las ramas principales.

## Prerequisitos

* Python 3.8
* PIP
* Pipenv

## Instalación

Ejecute los siguientes comandos en una terminal:

```bash
# instalar dependencias
$ pipenv install

# crear la base de datos
$ pipenv run python manage.py migrate

# llena la base de datos con registros dummy
$ pipenv run python manage.py loaddata populate.json

# crea un usuario administrador
$ pipenv run python manage.py createsuperuser
```

## Despliegue

Puede desplegar este proyecto en un ambiente productivo para ejecutar sus pruebas en un entorno lo 
más real posible, para ello realice las configuraciones que requieren atención en el archivo 
[`testapp/settings/production.py`](testapp/settings/production.py), luego cambie el nombre del achivo de configuración usado por Django 
en [`manage.py`](manage.py#L8) así:

```python
# de
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testapp.settings.development')

# a esto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testapp.settings.production')
```
