api_key ='AIzaSyA8HRRB6-CPAOs2YZYdU6gUi2aHnWyK-So'

from apiclient.discovery import build

youtube = build('youtube','v3',developerKey
                =api_key)
#print(type(youtube))

req = youtube.search().list(q='cats',part='snippet',type='video',maxResults=1)
res = req.execute()
print(res['items'][0]['id']['videoId'])

