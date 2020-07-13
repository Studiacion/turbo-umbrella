import requests

response = requests.get('https://api.covid19api.com/total/country/mexico/status/confirmed')
jsonResponse = response.json()
for dia in jsonResponse:
    print(dia['Date'],dia['Cases'])
    
#print('\n')
#print(jsonResponse)

'''
url = "https://api.covid19api.com/total/country/mexico/status/confirmed"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
'''
