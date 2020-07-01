'''Studiacion/turbo-umbrella is licensed under the
GNU General Public License v3.0
'''
import json
with open('llave_2.json') as f:
  data = json.load(f)
  
api_key = data["key"]

from apiclient.discovery import build

youtube = build('youtube','v3',developerKey
                =api_key)
#print(type(youtube))

req = youtube.search().list(q='dogs',part='snippet',type='video',maxResults=1, regionCode = 'US')
res = req.execute()
print("Youtube video ID:")
video_ID = res['items'][0]['id']['videoId']
print(video_ID)

f = open("video_ID.txt", "w")
f.write(video_ID)
f.close()
