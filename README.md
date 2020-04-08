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
Request Youtube videos from several countries(pending) of a particular topic at once.
The project aims to show the most relevant video(thumbnail and title) in a single webpage from several countries at once, having the client to specify the keyword or phrase in English. The client will get an answer in real time. Even though the client can query any word or phrase, the goal of this system is to show how an event with worldwide relevance is viewed by different people in different places.

### Practice 1 goals
What we are trying to accomplish is receiving the queried word and then iterate the translation of that word in the different languages we will choose using the Cloud Translation API. With those results, we will query to the Youtube API for each video, for each country. We will get the videos Ids which we will use to show the videos.

### Software tools and services
* Data sources
	* Youtube Data API v3
	* Cloud Translation API
* Storage
	* PostgreSQL (pending)
* Processing system
	* Python3
* Wordpress or Wix (pending)

## Quickstart (if you already have the credentials)
Using ubuntu18.4.4  
Using python 2.7  
Copy and save both python codes (in this repository) in your system. (request_tran.py and request_you.py)   
You should have 2 credentials with these specific names in the same directory as the 2 python codes so they run successfully:
* llave.json
* llave_2.json
### Install Cloud SDK
Add the Cloud SDK distribution URI as a package source:  
From terminal: <pre><code>echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list</code></pre>  

Import the Google Cloud Platform public key:  
From terminal: <pre><code>curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -</code></pre>  

Update the package list and install the Cloud SDK:  
From terminal: <pre><code>sudo apt-get update && sudo apt-get install google-cloud-sdk</code></pre>  

### Install Google Cloud Translate Library (python)
(Install pip if you don't have it)          
Then
From terminal: <pre><code>pip install --upgrade google-cloud-translate</code></pre>

### Install the Google Cloud Library (python)
From terminal: <pre><code>pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib</code></pre>

### Run sample code for translation
Open new terminal  
Change directory to the one where you have the codes and credentials  
Set credentials to the .json file with them:  
From terminal: <pre><code>export GOOGLE_APPLICATION_CREDENTIALS=llave.json</code></pre>  
Run sample code for translation. (request_tran.py)  

### Run Sample code for getting Youtube video code
Run sample code for getting Youtube video code. (request_you.py)

## Information needed for installation and execution
We'll need to follow several steps to be able to receive information successfully from both Google services.
* Step 1: You need a Google Account 
* Step 2: Open a Google Cloud Platform Account with your google account (you'll need a credit card)
* Step 3: Enable the Youtube Data API v3 and save assigned API key
* Step 4: Enable the Cloud Translation API and save the JSON file with the key.
	* Setup Cloud Translation API
	* Setup Youtube Data API v3
* Step 5: Write a python script for each service:
	* Youtube Data API v3 -> request_you.py
	* Cloud Translation API -> request_tran.py

## Testing
Successful!

## Results
* request_you.py
	* Out:	     
		<pre><code>Text: coronavirus is deadly    
		Translation: el coronavirus es mortal   
		Detected source language: en</code></pre>   
* request_tran.py
	* Out:   
		<pre><code>Youtube video ID:    
		G9oqvJ3iXGI</code></pre>   
	* The code obtained is inserted after ‘v=’ in:  ‘https://www.youtube.com/watch?v=’
	* The obtained URL https://www.youtube.com/watch?v=G9oqvJ3iXGI , which will take us to the first video of searching 'coronavirus' on Youtube.
		
## Bibliography
* Cloud AI | Google Cloud. (2020). Google Cloud. Retrieved 14 March 2020, from https://cloud.google.com/products/ai/
* Cloud Translation API | ML onramp | Google Cloud. (2020). Google Cloud. Retrieved 14 March 2020, from https://cloud.google.com/ml-onramp/translation
* YouTube Data API | Google Developers. (2020). Google Developers. Retrieved 14 March 2020, from https://developers.google.com/youtube/v3
* PostgreSQL: The world's most advanced open source database. (2020). Postgresql.org. Retrieved 14 March 2020, from https://www.postgresql.org/
* Python 3.0 Release. (2020). Python.org. Retrieved 14 March 2020, from https://www.python.org/download/releases/3.0/
* WordPress.com: Create a Free Website or Blog. (2020). WordPress.com. Retrieved 14 March 2020, from https://wordpress.com/
* Wix.com: Free Website Builder. (2020). Wix.com. Retrieved 14 March 2020, from https://www.wix.com/
* Indian Pythonista. (2018, September 26). Searching Content using YouTube Data API | Exploring YouTube Data API (Part-2). Retrieved 14 March 2020, from https://www.youtube.com/watch?v=b_jOJNUD350&list=LLlSrTwtMgwhhCYbsghKnluA&index=8

## Conclusions
The plan is working for now. Indeed you don't need to know everything to do something.
