# Práctica 2

* instalar mezzanine

Crear una carpeta para el servidor.
From terminal: <pre><code>/mnt/d$ mkdir (nombre del servidor, por ejemplo: server)</code></pre> 

Crear un ambiente virtual.
From terminal : <pre><code>/mnt/d/server$ virtualenv mezzanine_env</code></pre>

Instalar mezzanine.
From terminal: <pre><code>/mnt/d/server/mezzanine_env$ pip install mezzanine</code></pre>

Una vez instalado, crear el proyecto.
From terminal: <pre><code>/mnt/d/server/mezzanine_env$ mezzanine-project (nombre del proyecto, por ejemplo: caliz)</code></pre>

Si se desea, configurar (zona horaria, idioma, etc).
From terminal: <pre><code>/mnt/d/server/mezzanine_env/caliz/caliz$ nano settings.py</code></pre>

Crear la base de datos (te pedira algunas cosas).
From terminal: <pre><code>/mnt/d/server/mezzanine_env/caliz$ python manage.py createdb</code></pre>
From terminal: <pre><code>/mnt/d/server/mezzanine_env/caliz$ python manage.py collecttemplates</code></pre>

Correr el servidor.
From terminal: <pre><code>/mnt/d/server/mezzanine_env/caliz$ python manage.py runserver</code></pre>

Confirmar éxito en la ejecución visitando: http://[your droplet's IP]:8000


* hacer una proyecto y una db en mezzanine (localmente para empezar)

* hacer una base de datos con mysql
* conectar la base de datos al proyecto (código de python que saca información, también debe de poder hacer consultas para plotear las gráficas
