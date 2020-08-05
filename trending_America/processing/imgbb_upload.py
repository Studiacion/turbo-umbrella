import base64
import requests
import json
import sqlite3

with open('/home/javier/mezzanine.env/trending/imgbb.json') as f:
  data = json.load(f)
  
api_key = data["key"]

with open("/home/javier/mezzanine.env/trending/fig.jpg", "rb") as file:
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



    f = open("/home/javier/html_v/simplestyle_bluetrees/another_page.html", "w")   
    
    f.write('<!DOCTYPE HTML>')
    f.write('<html>')

    f.write('<head>')
    f.write('<style>')
    f.write('img {')
    f.write('  width: 100%;')
    f.write('}')
    f.write('</style>')
    f.write('<title>simplestyle_blue_trees - another page</title>')
    f.write('<meta name=\"description\" content=\"website description\" />')
    f.write('<meta name=\"keywords\" content=\"website keywords, website keywords\" />')
    f.write('<meta http-equiv=\"content-type\" content=\"text/html; charset=windows-1252\" />')
    f.write('<link rel=\"stylesheet\" type=\"text/css\" href=\"style/style.css\" />')
    f.write('</head>')

    f.write('<body>')
    f.write('<div id=\"main\">')
    f.write('    <div id=\"header\">')
    f.write('    <div id=\"logo\">')
    f.write('        <div id=\"logo_text\">')
    f.write('        <!-- class=\"logo_colour\", allows you to change the colour of the text -->')
    f.write('        <h1><a href=\"index.html\">simple<span class=\"logo_colour\">style_blue_trees</span></a></h1>')
    f.write('        <h2>Simple. Contemporary. Website Template.</h2>')
    f.write('        </div>')
    f.write('    </div>')
    f.write('    <div id=\"menubar\">')
    f.write('        <ul id=\"menu\">')
    f.write('        <!-- put class=\"selected\" in the li tag for the selected page - to highlight which page you\'re on -->')
    f.write('        <li><a href=\"index.html\">Home</a></li>')
    f.write('        <li><a href=\"examples.html\">Examples</a></li>')
    f.write('        <li><a href=\"page.html\">A Page</a></li>')
    f.write('        <li class=\"selected\"><a href=\"another_page.html\">Another Page</a></li>')
    f.write('        <li><a href=\"contact.html\">Contact Us</a></li>')
    f.write('        </ul>')
    f.write('    </div>')
    f.write('    </div>')
    f.write('    <div id=\"content_header\"></div>')
    f.write('    <div id=\"site_content\">')
    f.write('    <div id=\"sidebar_container\">')
    f.write('        <div class=\"sidebar\">')
    f.write('        <div class=\"sidebar_top\"></div>')
    f.write('        <div class=\"sidebar_item\">')
    f.write('            <!-- insert your sidebar items here -->')
    f.write('            <h3>Latest News</h3>')
    f.write('            <h4>New Website Launched</h4>')
    f.write('            <h5>February 1st, 2014</h5>')
    f.write('            <p>2014 sees the redesign of our website. Take a look around and let us know what you think.<br /><a href=\"#\">Read more</a></p>')
    f.write('        </div>')
    f.write('        <div class=\"sidebar_base\"></div>')
    f.write('        </div>')
    f.write('        <div class=\"sidebar\">')
    f.write('        <div class=\"sidebar_top\"></div>')
    f.write('        <div class=\"sidebar_item\">')
    f.write('            <h3>Useful Links</h3>')
    f.write('            <ul>')
    f.write('            <li><a href=\"#\">link 1</a></li>')
    f.write('            <li><a href=\"#\">link 2</a></li>')
    f.write('            <li><a href=\"#\">link 3</a></li>')
    f.write('            <li><a href=\"#\">link 4</a></li>')
    f.write('            </ul>')
    f.write('        </div>')
    f.write('        <div class=\"sidebar_base\"></div>')
    f.write('        </div>')
    f.write('        <div class=\"sidebar\">')
    f.write('        <div class=\"sidebar_top\"></div>')
    f.write('        <div class=\"sidebar_item\">')
    f.write('            <h3>Search</h3>')
    f.write('            <form method=\"post\" action=\"#\" id=\"search_form\">')
    f.write('            <p>')
    f.write('                <input class=\"search\" type=\"text\" name=\"search_field\" value=\"Enter keywords.....\" />')
    f.write('                <input name=\"search\" type=\"image\" style=\"border: 0; margin: 0 0 -9px 5px;\" src=\"style/search.png\" alt=\"Search\" title=\"Search\" />')
    f.write('            </p>')
    f.write('            </form>')
    f.write('        </div>')
    f.write('        <div class=\"sidebar_base\"></div>')
    f.write('        </div>')
    f.write('    </div>')
    f.write('    <div id=\"content\">')
    f.write('        <!-- insert the page content here -->')
    
    
    f.write('<img src={} alt=\"2019-11-19\" border=\"0\">'.format(image_url))

    f.write('    </div>')
    f.write('    </div>')
    f.write('    <div id=\"content_footer\"></div>')
    f.write('    <div id=\"footer\">')
    f.write('    <p><a href=\"index.html\">Home</a> | <a href=\"examples.html\">Examples</a> | <a href=\"page.html\">A Page</a> | <a href=\"another_page.html\">Another Page</a> | <a href=\"contact.html\">Contact Us</a></p>')
    f.write('    <p>Copyright &copy; simplestyle_blue_trees | <a href=\"http://validator.w3.org/check?uri=referer\">HTML5</a> | <a href=\"http://jigsaw.w3.org/css-validator/check/referer\">CSS</a> | <a href=\"http://www.html5webtemplates.co.uk\">design from HTML5webtemplates.co.uk</a></p>')
    f.write('    </div>')
    f.write('</div>')
    f.write('</body>')
    f.write('</html>')


    f.close()
