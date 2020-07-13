import requests

url = "https://api.imgur.com/3/upload"

payload = {}
files = {}
headers = {
  'Authorization': 'samplePrefix2bd14508161d91afd622d5ea1e9659870546a701'
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
