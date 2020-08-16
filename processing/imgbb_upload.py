import base64
import requests
import json
import os   
script_path = os.path.realpath(__file__) 
directory_path = script_path.replace("/processing/imgbb_upload.py", "")

import datetime  
update_time = 'Update date and time: '+str(datetime.datetime.now(datetime.timezone.utc))+ ' GMT'

### Uncomment if you want to store images in the cloud, also change the path of the image to 'image_url'

##with open('/home/vdelaluz/git/turbo-umbrella/credentials/imgbb.json'.format(username)) as f:
##  data = json.load(f)
##  
##api_key = data["key"]
##
##with open("/home/vdelaluz/git/turbo-umbrella/data/fig.jpg".format(username), "rb") as file:
##    url = "https://api.imgbb.com/1/upload"
##    payload = {
##        "key": api_key,
##        "image": base64.b64encode(file.read()),
##        "expiration": '172800', #2 days
##    }
##    res = requests.post(url, payload)
##    contents = json.loads(res.text)
##    image_url = contents['data']['url']
##    print('Image URL:')
##    print (image_url)
##

#if uncommented move all of below one tab -->

import configparser
config = configparser.ConfigParser()
config.read('{}/conf.ini'.format(directory_path))
static_directory = config['PATHS']['PublicHTMLAplicationPart']

f = open("{}/graphics.html".format(static_directory), "w")   


f.write('''
    <!DOCTYPE HTML>
    <!--
        Phantom by HTML5 UP
        html5up.net | @ajlkn
        Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
    -->
    <html>
        <head>
            <title>Studiacion</title>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
            <link rel="stylesheet" href="assets/css/main.css" />
            <noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>

        </head>
        <body class="is-preload">
            <!-- Wrapper -->
                <div id="wrapper">

                    <!-- Header -->
                        <header id="header">
                            <div class="inner">

                                <!-- Logo -->
                                    <a href="index.html" class="logo">
                                        <span class="symbol"><img src="images/UNAM.svg.png" alt="" /></span><span class="title">Studiacion</span>
                                    </a>

                                <!-- Nav -->
                                    <nav>
                                        <ul>
                                            <li><a href="#menu">Menu</a></li>
                                        </ul>
                                    </nav>

                            </div>
                        </header>

                    <!-- Menu -->
                        <nav id="menu">
                            <h2>Menu</h2>
                            <ul>
                                <li><a href="index.html">Home</a></li>
                                <li><a href="lives.html">Streamings</a></li>
                                <li><a href="videos.html">Videos</a></li>
                                <li><a href="graphics.html">Graphics</a></li>
                            </ul>
                        </nav>

                    <!-- Main -->
                        <div id="main">
                            <div class="inner">
                                <h1>COVID-19 Graphics</h1>
                                <!-- <span class="image main"><img src="images/pic13.jpg" alt="" /></span> -->
                            </div>

                            <div class="inner">
                                <!-- <span class="image main"><img src="images/pic13.jpg" alt="" /></span> -->
                                <p style="text-align:center;">{}</p>
                                <img src="fig.jpg" style="max-width:100%;" alt="2019-11-19" border="0">
                                
                        </div>

                    <!-- Footer -->
                        <footer id="footer">
                            <div class="inner">
                                <section>
                                    <h2>Get in touch</h2>
                                    <form method="post" action="#">
                                        <div class="fields">
                                            <div class="field half">
                                                <input type="text" name="name" id="name" placeholder="Name" />
                                            </div>
                                            <div class="field half">
                                                <input type="email" name="email" id="email" placeholder="Email" />
                                            </div>
                                            <div class="field">
                                                <textarea name="message" id="message" placeholder="Message"></textarea>
                                            </div>
                                        </div>
                                        <ul class="actions">
                                            <li><input type="submit" value="Send" class="primary" /></li>
                                        </ul>
                                    </form>
                                </section>
                                <ul class="copyright">
                                    <li>&copy; Untitled. All rights reserved</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
                                </ul>
                            </div>
                        </footer>

                </div>

            <!-- Scripts -->
                <script src="assets/js/jquery.min.js"></script>
                <script src="assets/js/browser.min.js"></script>
                <script src="assets/js/breakpoints.min.js"></script>
                <script src="assets/js/util.js"></script>
                <script src="assets/js/main.js"></script>

        </body>
    </html>
'''.format(update_time))
#.format(image_url))

f.close()
