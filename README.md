# turbo-umbrella - Trending America      
What we are aiming at is to have updated regional videos about COVID-19	news in a webpage. Also to have a graph showing the curves of new cases in each of those countries. The updates will happen every 6 hours and the countries will be the 10 most populated countries in America.

## Authors
* Javier Navarro - javojavojavojavo@gmail.com
* Francisco Fonseca - fonseking21@gmail.com
	  
## License 
GNU General Public License v3.0

### Software tools and services
* Data sources
	* Youtube Data API v3
	* COVID-19 API (https://covid19api.com/)
* Storage
	* text files for graph data, graph and youtube codes (stored locally in server)
* Processing system
	* Cron to schedule daily updates
	* Bash files to manage python programs
	* Python3
	* Matplotlib to generate graph
* Frontend
	* Based html template

## Quickstart (You must have the credentials)    
Using ubuntu18.4.4   (Also tested on Ubuntu20)              
Using python 3                

### Clone git
From terminal in /home/user/: <pre><code>git clone https://github.com/Studiacion/turbo-umbrella.git</code></pre>

### Setup cron   
Enter the following in the crontab so that the application updates its data every 6 hours (enter crontab using <code>crontab -e</code>):     
<pre><code>0 */6 * * * /bin/bash /[yourPATH]/turbo-umbrella/processing/main.sh</code></pre>

### Move 'static' folder
Move to the public path where the application is going to be. For example: <code>mv /home/user/turbo-umbrella/static/* /home/user/public_html/static/
</code>

### Configure 'conf.ini'
Open file in your text editor and write the public path where the application is going to be.   

### Place credentials
Place the credetials file along with the others.                  


### Deploy website
Enter turbo-umbrella folder and run: <pre><code>bash deploy.sh</code></pre>     

### Looks of the application
![](https://i.ibb.co/wMGmbq6/2020-08-16.png)

### Application working here:
http://132.247.186.67/jnavarro/index.html
		
## Bibliography
* Cloud AI | Google Cloud. (2020). Google Cloud. Retrieved 14 March 2020, from https://cloud.google.com/products/ai/
* Cloud Translation API | ML onramp | Google Cloud. (2020). Google Cloud. Retrieved 14 March 2020, from https://cloud.google.com/ml-onramp/translation
* YouTube Data API | Google Developers. (2020). Google Developers. Retrieved 14 March 2020, from https://developers.google.com/youtube/v3
* PostgreSQL: The world's most advanced open source database. (2020). Postgresql.org. Retrieved 14 March 2020, from https://www.postgresql.org/
* Python 3.0 Release. (2020). Python.org. Retrieved 14 March 2020, from https://www.python.org/download/releases/3.0/
* WordPress.com: Create a Free Website or Blog. (2020). WordPress.com. Retrieved 14 March 2020, from https://wordpress.com/
* Wix.com: Free Website Builder. (2020). Wix.com. Retrieved 14 March 2020, from https://www.wix.com/
* Indian Pythonista. (2018, September 26). Searching Content using YouTube Data API | Exploring YouTube Data API (Part-2). Retrieved 14 March 2020, from https://www.youtube.com/watch?v=b_jOJNUD350&list=LLlSrTwtMgwhhCYbsghKnluA&index=8
* Phantom by HTML5 UP. (2020). Retrieved August 9, 2020, from HTML5 UP website: https://html5up.net/phantom
* What Is Coronavirus? (2019). Retrieved August 9, 2020, from https://www.hopkinsmedicine.org/health/conditions-and-diseases/coronavirus

## Conclusions
This proyect was supposed to work for trending streamings and videos from the most populated countries around the world; However, due to global concerned about covid-19, we decided to focus exclusively on that topic.\
Also, because we live in Mexico and we care more about our continent, the searches are from the TOP 10 most populated countries in America.
