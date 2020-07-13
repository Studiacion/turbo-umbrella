import pandas as pd
from pytrends.request import TrendReq
#import matplotlib
import matplotlib.pyplot as plt

pytrends = TrendReq(hl='en-US', tz=360)

keywords = ['Coronavirus']
pytrends.build_payload(
     kw_list=keywords,
     cat=0,
     timeframe='today 3-m',
     #geo='WW',
     gprop='')
data = pytrends.interest_over_time()
data= data.drop(labels=['isPartial'],axis='columns')
image = data.plot(title = 'Coronavirus in last 3 months on Google Trends Worldwide')
fig = image.get_figure()
fig.savefig('/home/javier/mezzanine.env/trending/static/media/uploads/figure.png')
data.to_csv('Py_VS_R.csv', encoding='utf_8_sig')
