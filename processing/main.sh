#!/bin/bash

# IMPORTANT!!!
#   Pause crontab when editing this program

#source mezzanine.env/bin/activate    #NOT USING MEZZANINE WITH THIS BRANCH!

/usr/bin/python3 /home/vdelaluz/git/turbo-umbrella/processing/covid-API.py
sleep 2
/usr/bin/python3 /home/vdelaluz/git/turbo-umbrella/processing/request_you.py
sleep 2
/usr/bin/python3 /home/vdelaluz/git/turbo-umbrella/processing/request_you_live.py
sleep 2
/usr/bin/python3 /home/vdelaluz/git/turbo-umbrella/processing/covid-API-graph.py
sleep 2
/usr/bin/python3 /home/vdelaluz/git/turbo-umbrella/processing/content_updater.py
sleep 2
/usr/bin/python3 /home/vdelaluz/git/turbo-umbrella/processing/content_updater_live.py
sleep 2
/usr/bin/python3 /home/vdelaluz/git/turbo-umbrella/processing/imgbb_upload.py

# Programs that require Youtube API wont work if Youtube's API quota limit for requests has been reached
