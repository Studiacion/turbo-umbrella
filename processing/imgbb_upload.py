import base64
import requests
import json
import getpass
username = getpass.getuser()

### Uncomment if you want to store images in the cloud, also change the path of the image to 'image_url'

with open('/home/{}/turbo-umbrella/credentials/imgbb.json'.format(username)) as f:
  data = json.load(f)
  
api_key = data["key"]

with open("/home/{}/turbo-umbrella/data/fig.jpg".format(username), "rb") as file:
    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": api_key,
        "image": base64.b64encode(file.read()),
        "expiration": '172800', #2 days
    }
    res = requests.post(url, payload)
    contents = json.loads(res.text)
    image_url = contents['data']['url']
    print('Image URL:')
    print (image_url)


#if uncommented move all of below one tab -->

    f = open("/home/{}/public_html/static/another_page.html".format(username), "w")   


    f.write('''
    <!DOCTYPE HTML>
    <html>

    <head>
    <style>
    img {{
        width: 100%;
    }}
    </style>
    <title>simplestyle_blue_trees - another page</title>
    <meta name=\"description\" content=\"website description\" />
    <meta name=\"keywords\" content=\"website keywords, website keywords\" />
    <meta http-equiv=\"content-type\" content=\"text/html; charset=windows-1252\" />
    <link rel=\"stylesheet\" type=\"text/css\" href=\"style/style.css\" />
    </head>

    <body>
    <div id=\"main\">
        <div id=\"header\">
        <div id=\"logo\">
            <div id=\"logo_text\">
            <!-- class=\"logo_colour\", allows you to change the colour of the text -->
            <h1><a href=\"index.html\">simple<span class=\"logo_colour\">style_blue_trees</span></a></h1>
            <h2>Simple. Contemporary. Website Template.</h2>
            </div>
        </div>
        <div id=\"menubar\">
            <ul id=\"menu\">
            <!-- put class=\"selected\" in the li tag for the selected page - to highlight which page you\'re on -->
            <li><a href=\"index.html\">Home</a></li>
            <li><a href=\"examples.html\">Examples</a></li>
            <li><a href=\"page.html\">A Page</a></li>
            <li class=\"selected\"><a href=\"another_page.html\">Another Page</a></li>
            <li><a href=\"contact.html\">Contact Us</a></li>
            </ul>
        </div>
        </div>
        <div id=\"content_header\"></div>
        <div id=\"site_content\">
        <div id=\"sidebar_container\">
            <div class=\"sidebar\">
            <div class=\"sidebar_top\"></div>
            <div class=\"sidebar_item\">
                <!-- insert your sidebar items here -->
                <h3>Latest News</h3>
                <h4>New Website Launched</h4>
                <h5>February 1st, 2014</h5>
                <p>2014 sees the redesign of our website. Take a look around and let us know what you think.<br /><a href=\"#\">Read more</a></p>
            </div>
            <div class=\"sidebar_base\"></div>
            </div>
            <div class=\"sidebar\">
            <div class=\"sidebar_top\"></div>
            <div class=\"sidebar_item\">
                <h3>Useful Links</h3>
                <ul>
                <li><a href=\"#\">link 1</a></li>
                <li><a href=\"#\">link 2</a></li>
                <li><a href=\"#\">link 3</a></li>
                <li><a href=\"#\">link 4</a></li>
                </ul>
            </div>
            <div class=\"sidebar_base\"></div>
            </div>
            <div class=\"sidebar\">
            <div class=\"sidebar_top\"></div>
            <div class=\"sidebar_item\">
                <h3>Search</h3>
                <form method=\"post\" action=\"#\" id=\"search_form\">
                <p>
                    <input class=\"search\" type=\"text\" name=\"search_field\" value=\"Enter keywords.....\" />
                    <input name=\"search\" type=\"image\" style=\"border: 0; margin: 0 0 -9px 5px;\" src=\"style/search.png\" alt=\"Search\" title=\"Search\" />
                </p>
                </form>
            </div>
            <div class=\"sidebar_base\"></div>
            </div>
        </div>
        <div id=\"content\">
            <!-- insert the page content here -->


            <img src={} alt=\"2019-11-19\" border=\"0\">
            
            

        </div>
        </div>
        <div id=\"content_footer\"></div>
        <div id=\"footer\">
        <p><a href=\"index.html\">Home</a> | <a href=\"examples.html\">Examples</a> | <a href=\"page.html\">A Page</a> | <a href=\"another_page.html\">Another Page</a> | <a href=\"contact.html\">Contact Us</a></p>
        <p>Copyright &copy; simplestyle_blue_trees | <a href=\"http://validator.w3.org/check?uri=referer\">HTML5</a> | <a href=\"http://jigsaw.w3.org/css-validator/check/referer\">CSS</a> | <a href=\"http://www.html5webtemplates.co.uk\">design from HTML5webtemplates.co.uk</a></p>
        </div>
    </div>
    </body>
    </html>
    '''.format(image_url))

    f.close()
