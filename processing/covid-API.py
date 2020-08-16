import requests
import json
import os   
script_path = os.path.realpath(__file__) 
directory_path = script_path.replace("/processing/covid-API.py", "")

countries = ['united-states','brazil','mexico','colombia','argentina','canada','peru','venezuela','chile','ecuador']


for country in countries:
	response = requests.get('https://api.covid19api.com/total/country/{}/status/confirmed'.format(country))
	jsonResponse = response.json()

	f = open("{}/data/{}_data.txt".format(directory_path,country), "w")

	for dia in jsonResponse:
		record = str(dia['Date'])+' '+str(dia['Cases'])+'\n'
		f.write(record)
	
	f.close()
