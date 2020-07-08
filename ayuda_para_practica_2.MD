# Setting up Mezzanine webpage and working environment
## create virtualenv
documentation: https://virtualenv.pypa.io/  
<pre><code>pipx install virtualenv</code></pre>   
<pre><code>virtualenv mezzanine.env</code></pre>   

## activate it
source mezzanine.env/bin/activate   

## create database
<pre><code>python manage.py createdb</code></pre>   
    

## change allowed hosts and langualge and timezone in settings.py

## run server
<pre><code>python manage.py runserver 0.0.0.0:8000</code></pre>   

## open server in browser with localhost
http://127.0.0.1:8000/  

## embed youtube video using the easy admin function in local host using browser
 * You can retreive the html embeded video directly in youtube and then just change the video id to change the
   embeded video, you can get new video ids through the youtube API as shown in the first part of this proyect 
## the embeded video is in the .db file, then with python script you can automate video updates directlly in the database which you should see on the webpage.  
------------------------------------------------------------------------------------------------------------------
## SQLITE3 
The software that handles our database is sqlite3     
You can open the dev.db file with: <code>sqlite3 dev.db</code>    
<code>.tables</code> --> shows tables on our database      
<code>.schema pages_richtext...<code> --> shows schema on the selected table    

------------------------------------------------------------------------------------------------------------------
### NOT CURRENTLY USED ###
ENABLING CRON       

sudo systemctl enable cron     

## entering cron
crontab -e  
###                    ###
------------------------------------------------------------------------------------------------------------------
### APIs para COVID19 ###
## PARA USAR PyTrends.py
se necesita instalar pytrends con:    
pip install pytrends     

### covid19api
se puede solicitar con python can la librería 'requests', en la documentación vienen ejemplos.   
Documentación: https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest    

------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------

## EXTRA INFO   
------------------------------------------------------------------------------------------------------------------
## Suported countries:
 (Top 10 most populated countries in America)   
 1. Estados Unidos
 2. Brazil
 3. Mexico
 4. Colombia
 5. Argentina
 6. Canada
 7. Peru
 8. Venezuela
 9. Chile
 10. Ecuador
 
------------------------------------------------------------------------------------------------------------------
## YOUTUBE TESTS
<iframe width="560" height="315" src="https://www.youtube.com/embed/VMyjxx3y27Y" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>   


www.youtube.com/embed/VMyjxx3y27Y <-- link para embedar   
https://www.youtube.com/watch?v=VMyjxx3y27Y <-- link para ver   

###         THE VIDEO ID IS THE SAME             ###

In this tests I confirmed that de videos IDs are the same in the youtube video itself  and in the youtube api,
which means I can use the YoutubeAPI to automatize video updates.  
