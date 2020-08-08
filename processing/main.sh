#!/bin/bash

# IMPORTANT!!!
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
