#!/bin/bash

#sudo apt install python3-pip
#pip3 install matplotlib


#installing YouTube API
#echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
#curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
#sudo apt-get update && sudo apt-get install google-cloud-sdk
#pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
#finished 



rm -r ~/public_html/
mkdir ~/public_html
cp -r ~/turbo-umbrella/static/ ~/public_html/static

# IMPORTANT!!!
#   Enable comented both python commented lines below when having all needed credentials.
#   Pause crontab when editing this program

#source mezzanine.env/bin/activate    #NOT USING MEZZANINE WITH THIS BRANCH!

python3 ~/turbo-umbrella/processing/covid-API.py

python3 ~/turbo-umbrella/processing/request_you.py
python3 ~/turbo-umbrella/processing/request_you_live.py
python3 ~/turbo-umbrella/processing/covid-API-graph.py

python3 ~/turbo-umbrella/processing/content_updater.py
python3 ~/turbo-umbrella/processing/content_updater_live.py
python3 ~/turbo-umbrella/processing/imgbb_upload.py

# Programs that require Youtube API wont work if Youtube's API quota limit for requests has been reached

