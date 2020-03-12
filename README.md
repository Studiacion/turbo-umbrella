# turbo-umbrella
Repositorio con cada uno de los proyectos durante la clase: Computo distribuido, 2020-2

## Practice 1
## Title
Worldwide Trending
## Authors
* Javier Navarro Espindola - javojavojavojavo@gmail.com
* Pablo Francisco Fonseca Márquez - fonseking21@gmail.com
	  
## License 
GNU General Public License v3.0

## Introduction
Request videos from Youtube of several countries(pending) of a particular topic at once.
The project aims to show the most relevant video(thumbnail and title) in a single webpage of several countries at once, having the client to specify the keyword or phrase in English. The client will get an answer in real time. Even though the client can query any word or phrase, the goal of this system is to show how an event with worldwide relevance is viewed by different people in different places.

### Practice 1 goals
What we are trying to accomplish is receiving the queried word and then iterate the translation of that word in the different languages we will choose using the Cloud Translation API. With those results, we will query to the Youtube API for each video, for each country. We will get the videos Ids which we will use to show the videos.

### Software tools and services
* Data sources
	* Youtube Data API v3
	* Cloud Translation API
* Storage
	* mySQL or MariaDB (pending)
* Processing system
	* Python3
* Wordpress or Wix (pending)

## Information needed for installation and execution
We'll need to follow several steps to be able to receive information successfully from both Google services.
* Step 1: You need a Google Account 
* Step 2: Open a Google Cloud Platform Account with your google account (you'll need a credit card)
* Step 3: Enable the Youtube Data API v3 and save assigned API key
* Step 4: Enable the Cloud Translation API and save the JSON file with the key.
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

## Testing
Successful!

## Results
* request_you.py
	* Out:	
		* Text: coronavirus is deadly
		* Translation: el coronavirus es mortal
		* Detected source language: en
* request_tran.py
	* Out:
		* G9oqvJ3iXGI
		
## Bibliography
* https://developers.google.com/youtube/v3
* https://cloud.google.com/products/ai/
* https://www.youtube.com/watch?v=b_jOJNUD350&list=LLlSrTwtMgwhhCYbsghKnluA&index=8

## Conclusions
The plan is working for now. Indeed you don't need to know everything to do something.


