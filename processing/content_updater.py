import getpass
username = getpass.getuser()

f = open("/home/{}/turbo-umbrella/data/video_ID.txt".format(username), "r")
video_ID_US = f.readline()
video_ID_BR = f.readline()
video_ID_MX = f.readline()
video_ID_AR = f.readline()
video_ID_CO = f.readline()
video_ID_CA = f.readline()
video_ID_PE = f.readline()
video_ID_VE = f.readline()
video_ID_CL = f.readline()
video_ID_EC = f.readline()

f.close()

f = open("/home/{}/public_html/static/page.html".format(username), "w")

f.write('''
<!DOCTYPE HTML>
<html>

<head>
  <title>simplestyle_blue_trees - a page</title>
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
          <li class=\"selected\"><a href=\"page.html\">A Page</a></li>
          <li><a href=\"another_page.html\">Another Page</a></li>
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


        <h2 style=\"text-align: center;\">United States</h2>
        <p style=\"text-align: center;\"><iframe allowfullscreen=\"allowfullscreen\" height=\"315\" src=\"https://www.youtube.com/embed/{}\" width=\"560\"></iframe></p>
        <h2 style=\"text-align: center;\">Brazil</h2>
        <p><iframe width=\"560\" height=\"315\" style=\"display: block; margin-left: auto; margin-right: auto;\" allowfullscreen=\"allowfullscreen\" src=\"https://www.youtube.com/embed/{}\"></iframe></p>
        <h2 style=\"text-align: center;\">Mexico</h2>
        <p><iframe width=\"560\" height=\"315\" style=\"display: block; margin-left: auto; margin-right: auto;\" allowfullscreen=\"allowfullscreen\" src=\"https://www.youtube.com/embed/{}\"></iframe></p>
        <h2 style=\"text-align: center;\">Argentina</h2>
        <p><iframe width=\"560\" height=\"315\" style=\"display: block; margin-left: auto; margin-right: auto;\" allowfullscreen=\"allowfullscreen\" src=\"https://www.youtube.com/embed/{}\"></iframe></p>
        <h2 style=\"text-align: center;\">Colombia</h2>
        <p><iframe width=\"560\" height=\"315\" style=\"display: block; margin-left: auto; margin-right: auto;\" allowfullscreen=\"allowfullscreen\" src=\"https://www.youtube.com/embed/{}\"></iframe></p>
        <h2 style=\"text-align: center;\">Canada</h2>
        <p><iframe width=\"560\" height=\"315\" style=\"display: block; margin-left: auto; margin-right: auto;\" allowfullscreen=\"allowfullscreen\" src=\"https://www.youtube.com/embed/{}\"></iframe></p>
        <h2 style=\"text-align: center;\">Peru</h2>
        <p><iframe width=\"560\" height=\"315\" style=\"display: block; margin-left: auto; margin-right: auto;\" allowfullscreen=\"allowfullscreen\" src=\"https://www.youtube.com/embed/{}\"></iframe></p>
        <h2 style=\"text-align: center;\">Venezuela</h2>
        <p><iframe width=\"560\" height=\"315\" style=\"display: block; margin-left: auto; margin-right: auto;\" allowfullscreen=\"allowfullscreen\" src=\"https://www.youtube.com/embed/{}\"></iframe></p>
        <h2 style=\"text-align: center;\">Chile</h2>
        <p><iframe width=\"560\" height=\"315\" style=\"display: block; margin-left: auto; margin-right: auto;\" allowfullscreen=\"allowfullscreen\" src=\"https://www.youtube.com/embed/{}\"></iframe></p>
        <h2 style=\"text-align: center;\">Ecuador</h2>
        <p><iframe width=\"560\" height=\"315\" style=\"display: block; margin-left: auto; margin-right: auto;\" allowfullscreen=\"allowfullscreen\" src=\"https://www.youtube.com/embed/{}\"></iframe></p>

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
'''.format(video_ID_US, video_ID_BR, video_ID_MX, video_ID_AR, video_ID_CO, video_ID_CA, video_ID_PE, video_ID_VE, video_ID_CL,  video_ID_EC))




f.close()

