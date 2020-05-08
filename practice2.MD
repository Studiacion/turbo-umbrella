# Práctica 2

* instalar mezzanine
Crear una carpeta para el servidor.
From terminal: <pre><code>mkdir (nombre del servidor, por ejemplo: server)</code></pre> 

Crear un ambiente virtual estando en: '/mnt/d/server'
From terminal : <pre><code>virtualenv mezzanine_env</code></pre>

Instalar mezzanine estando en: '/mnt/d/server/mezzanine_env'
From terminal: <pre><code>pip install mezzanine</code></pre>

Una vez instalado, crear el proyecto estando en: '/mnt/d/server/mezzanine_env'
From terminal: <pre><code>mezzanine-project (nombre del proyecto, por ejemplo: caliz)</code></pre>

Crear la base de datos estando en: '/mnt/d/server/mezzanine_env/caliz'
From terminal: <pre><code>python manage.py createdb</code></pre>

Te pedirá las siguientes cosas:

1)<pre><code>A site record is required.
Please enter the domain and optional port in the format 'domain:port'.
For example 'localhost:8000' or 'www.example.com'.
Hit enter to use the default (127.0.0.1:8000): </code></pre>

* hacer una proyecto y una db en mezzanine (localmente para empezar)

* hacer una base de datos con mysql
* conectar la base de datos al proyecto (código de python que saca información, también debe de poder hacer consultas para plotear las gráficas
