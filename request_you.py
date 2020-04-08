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

req = youtube.search().list(q='cats',part='snippet',type='video',maxResults=1)
res = req.execute()
print("Youtube video ID:")
print(res['items'][0]['id']['videoId'])

