#!/bin/bash

#sudo apt install python3-pip
#pip3 install matplotlib


#installing YouTube API
#echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
#curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
#sudo apt-get update && sudo apt-get install google-cloud-sdk
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
#finished 


# copy static directory to the public space where it will be uploaded
#rm -r ~/public_html/
#mkdir ~/public_html
#cp -r ~/turbo-umbrella/static/ ~/public_html/static



DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

/usr/bin/python3 $DIR/processing/covid-API.py
sleep 2

/usr/bin/python3 $DIR/processing/request_you.py
sleep 2
/usr/bin/python3 $DIR/processing/request_you_live.py
sleep 2
/usr/bin/python3 $DIR/processing/covid-API-graph.py
sleep 2

/usr/bin/python3 $DIR/processing/content_updater.py
sleep 2
/usr/bin/python3 $DIR/processing/content_updater_live.py
sleep 2
/usr/bin/python3 $DIR/processing/imgbb_upload.py
sleep 2

# Programs that require Youtube API wont work if Youtube's API quota limit for requests has been reached

