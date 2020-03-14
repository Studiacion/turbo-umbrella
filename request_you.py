'''Studiacion/turbo-umbrella is licensed under the
GNU General Public License v3.0
'''

api_key =[API_KEY]

from apiclient.discovery import build

youtube = build('youtube','v3',developerKey
                =api_key)
#print(type(youtube))

req = youtube.search().list(q='cats',part='snippet',type='video',maxResults=1)
res = req.execute()
print(res['items'][0]['id']['videoId'])

