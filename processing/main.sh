#!/bin/bash



DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"


/usr/bin/python3 $DIR/covid-API.py
sleep 2
/usr/bin/python3 $DIR/request_you.py
sleep 2
/usr/bin/python3 $DIR/request_you_live.py
sleep 2
/usr/bin/python3 $DIR/covid-API-graph.py
sleep 2
/usr/bin/python3 $DIR/content_updater.py
sleep 2
/usr/bin/python3 $DIR/content_updater_live.py
sleep 2
/usr/bin/python3 $DIR/imgbb_upload.py

# Programs that require Youtube API wont work if Youtube's API quota limit for requests has been reached
