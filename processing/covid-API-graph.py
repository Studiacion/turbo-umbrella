import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime
import dateutil.parser
import getpass
username = getpass.getuser()

#f = open("{}_data.txt".format(country), "w")

def total_to_daily(confirmed):
	total = 0
	daily = []
	for i in range(len(confirmed)):
		day_i = int(confirmed[i])-int(total)
		daily.append(day_i)
		total = int(confirmed[i])
	return (daily)




plt.figure(figsize=(25,8)) 

ax = plt.axes() 
ax.grid(linewidth=0.4, color='#8f8f8f')  
  
ax.set_facecolor("black")  
ax.set_xlabel('Date',size=25)#,color='#4bb4f2') 
ax.set_ylabel('Daily Confirmed Cases\n', 
              size=25)#,color='#4bb4f2') 

plt.title("COVID-19 America",
          size=50)#,color='#28a9ff')





countries = ['united-states','brazil','mexico','colombia','argentina','canada','peru','venezuela','chile','ecuador']
countriesN = ['US','Brazil','Mexico','Colombia','Argentina','Canada','Peru','Venezuela','Chile','Ecuador']
colors = ['#ff0000','#e33500','#e3c900','#149c05','#06c2c2','#023b9e','#4c0ccc','#cc0c9f','#d45068','#bdbfc7']
color = -1

for country in countries:
    color += 1
    fecha = []
    confirmados = []
    #f = open("/home/javier/mezzanine.env/trending/covid-API.txt", "r")
    f = open("/home/vdelaluz/git/turbo-umbrella/data/{}_data.txt".format(country), "r")
    dia = 0
    while True: 
        line = f.readline() 
        if not line: 
            break
        tupla = line.split()
        object_fecha = dateutil.parser.isoparse(tupla[0])
        fecha.append(object_fecha)
        confirmados.append(tupla[1])
        dia += 1
    f.close() 

    confirmados = total_to_daily(confirmados)

    x = fecha
    y = confirmados

    ax.plot(x,y, 
        color=colors[color], 
        marker='o', 
        linewidth=1.5, 
        markersize=3, 
        markeredgecolor='#1e94a6',
        label=countriesN[color]) 
    ax.legend()


#ax.set_xlabel('Date ({}-{})'.format(fecha[0].strftime(,fecha[len(fecha)-1]),size=25,color='#4bb4f2') 
ax.annotate('Second Lockdown 15th April', 
            xy=(15.2, fecha[0]), 
            xytext=(19.9,500), 
            color='white', 
            size='100', 
            arrowprops=dict(color='white', 
                            linewidth=0.025)) 

plt.savefig('/home/vdelaluz/public_html/gicc/static/cursos/2020-II/turbo-umbrella/fig.jpg'.format(username),quality=96)
