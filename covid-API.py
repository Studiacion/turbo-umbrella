import requests

countries = ['united-states','brazil','mexico','colombia','argentina','canada','peru','venezuela','chile','ecuador']


for country in countries:
	response = requests.get('https://api.covid19api.com/total/country/{}/status/confirmed'.format(country))
	jsonResponse = response.json()

	f = open("/home/javier/mezzanine.env/trending/data/{}_data.txt".format(country), "w")

	for dia in jsonResponse:
		record = str(dia['Date'])+' '+str(dia['Cases'])+'\n'
		f.write(record)
	
	f.close()
