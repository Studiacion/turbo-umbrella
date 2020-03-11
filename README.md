# turbo-umbrella
Repositorio con cada uno de los proyectos durante la clase: Computo distribuido, 2020-2

licencia, información para instalación y ejecución, introducción, metodología, implementación, pruebas, resultados, conclusiones y bibliografía.

Práctica 1
Título: Trending Mundial
Autores:  Javier Navarro Espindola - javojavojavojavo@gmail.com
          Pablo Francisco Fonseca Márquez - fonseking21@gmail.com
Definición de proyecto:
Trending Mundial (Youtube)
	Consulta videos de Youtube de varios países(por definir) de un tema en particular.
Objetivos generales:
El proyecto tiene como objetivo desplegar en una página web el video(mostrando thumbnail y título) más relevante(criterio por definir) de varios países especificando el tema con una palabra clave que el usuario consultará y obtendrá respuesta en tiempo real
Aunque se pueda consultar cualquier palabra o frase en inglés con traducción a los demás idiomas(por definir), la idea es que el usuario consulte un tema relevante mundialmente para que se dé una idea de ćomo se percibe tal tema en los diferentes paises.
Herramientas de software a utilizar:
Usaremos el API de traducción de google cloud
API versión 3 de Youtube
mySQL o MariaDB (por definir)
Python3
Wordpress o Wix (por definir)
Arquitectura general del sistema:
Fuente de datos:
Servicio de traducción de google
API versión 3 de Youtube
Sistema de almacenamiento:
La información por ahora la guardaremos localmente usando mySQL o MariaDB
Sistema de procesamiento:
Todos los procesos se harán usando python:
Lo que planeamos hacer es recibir la palabra consultada (en inglés), y luego iterar la traducción de esa palabra en los idiomas que elegiremos usando el servicio de traducción de Google. Ya con las traducciones, haremos la consulta con el API de Youtube de cada video para cada país en su idioma correspondiente. Obteniendo así el Id de los videos que desplegaremos en la página.
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
api_key ='AIzaSyA8HRRB6-CPAOs2YZYdU6gUi2aHnWyK-So'

from apiclient.discovery import build

youtube = build('youtube','v3',developerKey = api_key)

req = youtube.search().list(q='coronavirus',part='snippet',type='video',maxResults=1)
res = req.execute()
print(res['items'][0]['id']['videoId'])
Out:
G9oqvJ3iXGI

El output obtenido arriba se inserta después de ‘v=’ en:  ‘https://www.youtube.com/watch?v=’
El URL obtenido con G9oqvJ3iXGI es https://www.youtube.com/watch?v=G9oqvJ3iXGI , y éste nos llevará al primer video de la búsqueda ‘coronavirus’ en Youtube.
