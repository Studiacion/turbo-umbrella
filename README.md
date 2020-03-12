# turbo-umbrella
Repositorio con cada uno de los proyectos durante la clase: Computo distribuido, 2020-2

## Práctica 1
## Título: Trending Mundial

## Autores:  
Javier Navarro Espindola - javojavojavojavo@gmail.com
Pablo Francisco Fonseca Márquez - fonseking21@gmail.com
	  
## Licencia: GNU General Public License v3.0

## Introducción:
Consulta videos de Youtube de varios países(por definir) de un tema en particular.
El proyecto tiene como objetivo desplegar en una página web el video(mostrando thumbnail y título) más relevante(criterio por definir) de varios países especificando el tema con una palabra clave que el usuario consultará y obtendrá respuesta en tiempo real, aunque se pueda consultar cualquier palabra o frase en inglés con traducción a los demás idiomas(por definir), la idea es que el usuario consulte un tema relevante mundialmente para que se dé una idea de ćomo se percibe tal tema en los diferentes paises.

### Objetivos de la práctica 1:
Lo que planeamos hacer es recibir la palabra consultada (en inglés), y luego iterar la traducción de esa palabra en los idiomas que elegiremos usando el servicio de traducción de Google. Ya con las traducciones, haremos la consulta con el API de Youtube de cada video para cada país en su idioma correspondiente. Obteniendo así el Id de los videos que desplegaremos en la página.

### Herramientas de software a utilizar:
* Usaremos el API de traducción de google cloud
* API versión 3 de Youtube
* mySQL o MariaDB (por definir)
* Python3
* Wordpress o Wix (por definir)

### Fuente de datos:
* Servicio de traducción de google
* API versión 3 de Youtube

### Sistema de almacenamiento:
La información por ahora la guardaremos localmente usando mySQL o MariaDB

### Sistema de procesamiento:
Todos los procesos se harán usando python:

## Información para instalación y ejecucón:
Necesitaremos hacer varias cosas para poder recibir información exitosamente de Cloud Translation API y de Youtube DATA API v3.
* Paso 1: Necesitas tener una cuenta de Google
* Paso 2: Hacer una cuenta en Google Cloud Platform (se necesita ingresar tarjeta de crédito)
* Paso 3: Activar el Youtube Data API v3 y guardar la clave API asignada
* Paso 4: Activar el Cloud Translation API y guardar las claves que te asignen en el formato .JSON
	* Setup Cloud Translation API
		* Create a project or select one
		* Create a service account
		* Download JSON with the private key
		* Enter: 'set GOOGLE_APPLICATION_CREDENTIALS=[path to the JSON file]' in the terminal you are going to use
		* Install Cloud SDK
		* Install python client library
	* Setup Youtube Data API v3
		* Install the Google APIs Client Library for Python
* Step 5: Write a python script for each service:
	* Youtube Data API v3 -> request_you.py
	* Cloud Translation API -> request_tran.py

## Introducción

## Metodología
## Implementación
## Pruebas
## Resultados
## Conclusiones y bibliografía


Página web:
Usaremos algún servicio como Wix o Wordpress para desplegar los videos
Fuente de datos:
Google:
Cloud Translation API
Youtube Data API v3
Test para adquisición de datos:

Ejemplo de adquisición de datos de Cloud Translation API:
text = 'coronavirus is deadly'
target = 'hi'

from google.cloud import translate_v2 as translate
translate_client = translate.Client()

result = translate_client.translate(text, target_language=target)

print(u'Text: {}'.format(result['input']))
print(u'Translation: {}'.format(result['translatedText']))
print(u'Detected source language: {}'.format(
    result['detectedSourceLanguage']))
Out:
Text: coronavirus is deadly
Translation: el coronavirus es mortal
Detected source language: en

Ejemplo de adquisición de datos de Youtube Data API v3
api_key =

from apiclient.discovery import build

youtube = build('youtube','v3',developerKey = api_key)

req = youtube.search().list(q='coronavirus',part='snippet',type='video',maxResults=1)
res = req.execute()
print(res['items'][0]['id']['videoId'])
Out:
G9oqvJ3iXGI

El output obtenido arriba se inserta después de ‘v=’ en:  ‘https://www.youtube.com/watch?v=’
El URL obtenido con G9oqvJ3iXGI es https://www.youtube.com/watch?v=G9oqvJ3iXGI , y éste nos llevará al primer video de la búsqueda ‘coronavirus’ en Youtube.
