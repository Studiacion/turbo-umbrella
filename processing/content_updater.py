import getpass
username = getpass.getuser()

f = open("/home/vdelaluz/git/turbo-umbrella/data/video_ID.txt".format(username), "r")
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

f = open("/home/vdelaluz/public_html/gicc/static/cursos/2020-II/turbo-umbrella/videos.html".format(username), "w")

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
									<span class="symbol"><img src="images/logo.png" alt="" /></span><span class="title">Studiacion</span>
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
							<span class="image right"><img src="images/vidios.jpg" alt="" /></span><h1>Popular Videos</h1>
							<!-- <span class="image main"><img src="images/pic13.jpg" alt="" /></span> -->
						</div>
						<hr />

						<div class="inner">
							<span class="image left"><img src="images/mexico.jpg" alt="" /></span><h2 style="font-size:35px">Mexico</h2>
							<iframe width="560" height="315" src="https://www.youtube.com/embed/{}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
						</div>
						<hr />

						<div class="inner">
							<span class="image left"><img src="images/gringos.jpg" alt="" /></span><h2 style="font-size:35px">United States</h2>
							<iframe width="560" height="315" src="https://www.youtube.com/embed/{}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
						</div>
						<hr />

						<div class="inner">
							<span class="image left"><img src="images/brazil.jpg" alt="" /></span><h2 style="font-size:35px">Brazil</h2>
							<iframe width="560" height="315" src="https://www.youtube.com/embed/{}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
						</div>
						<hr />

						<div class="inner">
							<span class="image left"><img src="images/canada.jpg" alt="" /></span><h2 style="font-size:35px">Canada</h2>
							<iframe width="560" height="315" src="https://www.youtube.com/embed/{}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
						</div>
						<hr />

						<div class="inner">
							<span class="image left"><img src="images/arg.jpg" alt="" /></span><h2 style="font-size:35px">Argentina</h2>
							<iframe width="560" height="315" src="https://www.youtube.com/embed/{}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
						</div>
						<hr />

						<div class="inner">
							<span class="image left"><img src="images/chile.jpg" alt="" /></span><h2 style="font-size:35px">Chile</h2>
							<iframe width="560" height="315" src="https://www.youtube.com/embed/{}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
						</div>
						<hr />

						<div class="inner">
							<span class="image left"><img src="images/colombia.jpg" alt="" /></span><h2 style="font-size:35px">Colombia</h2>
							<iframe width="560" height="315" src="https://www.youtube.com/embed/{}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
						</div>
						<hr />

						<div class="inner">
							<span class="image left"><img src="images/ecuador.jpg" alt="" /></span><h2 style="font-size:35px">Ecuador</h2>
							<iframe width="560" height="315" src="https://www.youtube.com/embed/{}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
						</div>
						<hr />

						<div class="inner">
							<span class="image left"><img src="images/peru.jpg" alt="" /></span><h2 style="font-size:35px">Peru</h2>
							<iframe width="560" height="315" src="https://www.youtube.com/embed/{}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
						</div>
						<hr />

						<div class="inner">
							<span class="image left"><img src="images/venezuela.jpg" alt="" /></span><h2 style="font-size:34px">Venezuela</h2>
							<iframe width="560" height="315" src="https://www.youtube.com/embed/{}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
						</div>

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
'''.format(video_ID_MX, video_ID_US, video_ID_BR, video_ID_CA, video_ID_AR, video_ID_CL, video_ID_CO, video_ID_EC, video_ID_PE, video_ID_VE))




f.close()

