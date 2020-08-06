#!/bin/bash

mkdir ~/public_html
cp -r ~/turbo-umbrella/static/ ~/public_html/static

# IMPORTANT!!!
#   Enable comented both python commented lines below when having all needed credentials.
#   Pause crontab when editing this program

#source mezzanine.env/bin/activate    #NOT USING MEZZANINE WITH THIS BRANCH!

#python ~/turbo-umbrella/processing/covid-API.py

#python ~/turbo-umbrella/processing/request_you.py
#python ~/turbo-umbrella/processing/request_you_live.py
python ~/turbo-umbrella/processing/covid-API-graph.py

python ~/turbo-umbrella/processing/content_updater.py
python ~/turbo-umbrella/processing/content_updater_live.py
python ~/turbo-umbrella/processing/imgbb_upload.py

# Programs that require Youtube API wont work if Youtube's API quota limit for requests has been reached

