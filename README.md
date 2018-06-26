Proyecto final - Desarrollo web - Tópicos 2
========================================================================================================================================


Descipción del problema
========================================================================================================================================
El problema de desarrollo web está enfocado en un rent a car, donde nos enfocaremos en el arriendo de auto, para ser mas específico se crearan tres diferentes tipos de entidades, estas son vehículo, cliente y ejecutivo, donde el vehículo y el ejecutivo van a tener "CRUD", también se realizará un autentificado, para los privilegios de los diferentes tipos de usuarios del sistema.
>El usuario cliente solo tendrá acceso a los distintos vehículos que tiene la empresa y también puede visualizar los autos que arrendó con anterioridad

>El usuario ejecutivo puede añadir nuevos vehículos, efectuar arriendo, cambiar estado actual de los vehículos, tambien puede añadir, eliminar y editar clientes.




(Todos los pasos son para el sistema operativo linux, ubuntu)
========================================================================================================================================
Como primera parte debes tener instalado python version 3.5.2 que lo puedes descargar de su respectivo sitio oficial.
"Todos los pasos deben ser ejecutados desde la terminal"
se explicará las acciones que debe hacer el usuario y su respectivo codigo para ello.

1. Instalar git
>sudo apt-get install git

2. Instalar virtualenv
>sudo apt-get install python-virtualenv virtualenv

3. Crear el ambiente virtual
>virtualenv -p python3 "nombre carpeta a crear"

4. Clonar el archivo desde git dentro de la carpeta del ambiente virtual
>git clone git@github.com:GonzAndre/Proyecto_final.git


5. Activar ambiente virtual (esto se realiza donde se encuentra la carpeta bin)
>source bin/activate

si, todo funciona correctamente debería mostrar el nombre del ambiente virtual al lado derecho entro parentesis:

![ambiente virtual](https://user-images.githubusercontent.com/26631971/41884519-d0006636-78c1-11e8-84b6-c98318c43697.png)


6. Instalar el archivo requirements
>sudo pip install requirements.txt

para desplegar el proyecto (ubicarse en carpeta donde se encuentre el archivo manage.py)
>python manage.py runserver

si todo funciona de forma correcta, deberia tener una salida similar a lo siguente:

![runserver](https://user-images.githubusercontent.com/26631971/41884549-ef097d42-78c1-11e8-83e0-a09efe76aca2.png)


7. Copiar la URL que indica al ejecutar el codigo anterior y agregarle Rent/index:

  **Ejemplo :
   http://127.0.0.1:8000/Rent/index**

