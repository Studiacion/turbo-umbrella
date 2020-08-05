#!/bin/bash

# IMPORTANT!!!
#   Pause crontab when editing this program

source mezzanine.env/bin/activate

python /home/javier/mezzanine.env/trending/covid-API.py > /home/javier/mezzanine.env/trending/covid-API.txt

python /home/javier/mezzanine.env/trending/request_you.py
python /home/javier/mezzanine.env/trending/request_you_live.py
python /home/javier/mezzanine.env/trending/covid-API-graph.py

python /home/javier/mezzanine.env/trending/content_updater.py
python /home/javier/mezzanine.env/trending/content_updater_live.py
python /home/javier/mezzanine.env/trending/imgbb_upload.py

# Programs that require Youtube API wont work if Youtube's API quota limit for requests has been reached
