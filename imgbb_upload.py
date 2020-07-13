import base64
import requests
import json
import sqlite3

with open('imgbb.json') as f:
  data = json.load(f)
  
api_key = data["key"]

with open("mexico.png", "rb") as file:
    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": api_key,
        "image": base64.b64encode(file.read()),
        "expiration": '172800', #2 days
    }
    res = requests.post(url, payload)
    contents = json.loads(res.text)
    image_url = contents['data']['url']
    print (image_url)
    
    
    '''
    '''
    conn = sqlite3.connect('dev.db')

    c = conn.cursor()    
    c.execute("UPDATE pages_richtextpage SET content = '<img src={} alt=\"2019-11-19\" border=\"0\">' WHERE page_ptr_id = '9'".format(image_url))
    conn.commit()

    conn.close()
