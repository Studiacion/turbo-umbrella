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

req = youtube.search().list(q = 'coronavirus US', part = 'snippet', type = 'video', eventType = 'live', maxResults = 1, regionCode = 'US')
res_US = req.execute()

req = youtube.search().list(q = 'coronavirus brazil', part = 'snippet', type = 'video', eventType = 'live', maxResults = 1, regionCode = 'BR')
res_BR = req.execute()

req = youtube.search().list(q = 'coronavirus mexico', part = 'snippet', type = 'video', eventType = 'live', maxResults = 1, regionCode = 'MX')
res_MX = req.execute()

req = youtube.search().list(q = 'coronavirus colombia', part = 'snippet', type = 'video', eventType = 'live', maxResults = 1, regionCode = 'CO')
res_CO = req.execute()

req = youtube.search().list(q = 'coronavirus argentina', part = 'snippet', type = 'video', eventType = 'live', maxResults = 1, regionCode = 'AR')
res_AR = req.execute()

req = youtube.search().list(q = 'coronavirus canada', part = 'snippet', type = 'video', eventType = 'live', maxResults = 1, regionCode = 'CA')
res_CA = req.execute()

req = youtube.search().list(q = 'coronavirus peru', part = 'snippet', type = 'video', eventType = 'live', maxResults = 1, regionCode = 'PE')
res_PE = req.execute()

req = youtube.search().list(q = 'coronavirus venezuela', part = 'snippet', type = 'video', eventType = 'live', maxResults = 1, regionCode = 'VE')
res_VE = req.execute()

req = youtube.search().list(q = 'coronavirus chile', part = 'snippet', type = 'video', eventType = 'live', maxResults = 1, regionCode = 'CL')
res_CL = req.execute()

req = youtube.search().list(q = 'coronavirus ecuador', part = 'snippet', type = 'video', eventType = 'live', maxResults = 1, regionCode = 'EC')
res_EC = req.execute()


print("Youtube video ID:")

video_ID_US = res_US['items'][0]['id']['videoId']
print(video_ID_US)

video_ID_BR = res_BR['items'][0]['id']['videoId']
print(video_ID_BR)

video_ID_MX = res_MX['items'][0]['id']['videoId']
print(video_ID_MX)

video_ID_CO = res_CO['items'][0]['id']['videoId']
print(video_ID_CO)

video_ID_AR = res_AR['items'][0]['id']['videoId']
print(video_ID_AR)

video_ID_CA = res_CA['items'][0]['id']['videoId']
print(video_ID_CA)

video_ID_PE = res_PE['items'][0]['id']['videoId']
print(video_ID_PE)

video_ID_VE = res_VE['items'][0]['id']['videoId']
print(video_ID_VE)

video_ID_CL = res_CL['items'][0]['id']['videoId']
print(video_ID_CL)

video_ID_EC = res_EC['items'][0]['id']['videoId']
print(video_ID_EC)


f = open("video_ID_live.txt", "w")
f.write("{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(video_ID_US, video_ID_BR, video_ID_MX, video_ID_AR, video_ID_CO, video_ID_CA, video_ID_PE, video_ID_VE, video_ID_CL,  video_ID_EC))
f.close()
