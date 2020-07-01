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

req = youtube.search().list(q = 'coronavirus mexico', part = 'snippet', type = 'video', eventType = 'completed', maxResults = 1, regionCode = 'MX')
res_MX = req.execute()

req = youtube.search().list(q = 'coronavirus US', part = 'snippet', type = 'video', eventType = 'completed', maxResults = 1, regionCode = 'US')
res_US = req.execute()

req = youtube.search().list(q = 'coronavirus brazil', part = 'snippet', type = 'video', eventType = 'completed', maxResults = 1, regionCode = 'BR')
res_BR = req.execute()

req = youtube.search().list(q = 'coronavirus chile', part = 'snippet', type = 'video', eventType = 'completed', maxResults = 1, regionCode = 'CL')
res_CL = req.execute()


print("Youtube video ID:")
video_ID_MX = res_MX['items'][0]['id']['videoId']
print(video_ID_MX)
video_ID_US = res_US['items'][0]['id']['videoId']
print(video_ID_US)
video_ID_BR = res_BR['items'][0]['id']['videoId']
print(video_ID_BR)
video_ID_CL = res_CL['items'][0]['id']['videoId']
print(video_ID_CL)

f = open("video_ID.txt", "w")
f.write("{}\n{}\n{}\n{}".format(video_ID_MX,video_ID_US,video_ID_BR,video_ID_CL))
f.close()
