
from datetime import datetime
import dateutil.parser

fecha = []
confirmados = []


f = open("covid-API.txt", "r")


dia = 0
while True: 
    line = f.readline() 
    if not line: 
        break
    tupla = line.split()
    #object_fecha = dateutil.parser.isoparse(tupla[0])
    fecha.append(dia)
    confirmados.append(tupla[1])
    dia += 1
x = fecha
y = confirmados
    
f.close() 
#import matplotlib
#print(matplotlib.get_backend())
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
'''
pltr.get_xaxis().get_major_formatter().set_useOffset(False)
plt.plot(x, y)
#plt.ylabel('some numbers')
plt.show()
'''


###############################################################################################################################################################





  
fig = plt.figure() 
ax = fig.add_subplot('''111''') 
ax.plot(x, y) 
  
# Create your ticker object with M ticks 
M = 10
yticks = ticker.MaxNLocator(M) 
xticks = ticker.MaxNLocator(18)
  
# Set the yaxis major locator using 
# your ticker object.  
ax.yaxis.set_major_locator(yticks) 
ax.xaxis.set_major_locator(xticks) 

  
plt.grid(b=None, which='major', axis='both')
plt.title('Casos diarios de COVID19 en México')
plt.ylabel('casos')
plt.xlabel('Dias desde el primer caso documentado')

plt.savefig('mexico.png')
#plt.show() 
