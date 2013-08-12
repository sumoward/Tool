<doctype html>
<head>

<link rel="icon" type="image/png "href="static/image/favicon.ico">
<link href="/static/css/bootstrap.min.css.gz" rel="stylesheet">
<link href="/static/css/bootstrap-responsive.min.css.gz" rel="stylesheet">
<title>Best Practice</title>

<script src="/static/jsfiles/jquery.min.js.gz"></script>
<meta name="viewport" content="width=device-width, initial-scale=1.0">    
     
        <style>
            body{padding-top: 60px;/* 60px to make the container go all the way to the bottom of the topbar */}
        </style>
       <script src="/static/jsfiles/bootstrap.min.js.gz"></script>      
</head>
<body>
<div class="container">
<div class="span8">

<div class="hero-unit">
<a href="http://www.principalsystems.com/"><img src="static/image/header1_01.gif" class="img-polaroid"></a>
<h3>Principal Systems Guide to WMS best practice</h3>
Our latest guide to the top 10 practices in Warehouse management.

It is compiled by our consultants.

this is an image
<img src="static/img/joe_image.jpg" class="img-polaroid">

In this  guide, you will learn:
blah
blah
blah

Start generating more leads for your business with great content. Download the free ebook to the right to get started!
</div>
</div>

<div class="span3">

<!-- Intro -->
<legend>If you would like us to email it to to you. Please fill in the details below.</legend><br>

<form class="form-condensed table-hover" method = "POST" action="/best_practice">

<label>First name</label><input type="text" class="input-large search-query" name ='form0'><br>
<label>Last name</label><input type="text" class="input-large search-query" name ='form1'><br>
<label>E-mail</label><input type="text" class="input-large search-query" name ='form2'><br>
<label>Company Name</label><input type="text" class="input-large search-query" name ='form3'><br>
<label>Phone</label><input type="text" class="input-large search-query" name ='form4'><br>

<br> <button type="submit" class="btn btn-warning btn-large">Download Now</button><br>

% if message != "Please fill in the details above so that we may send you your information":
{{message}}
%end

</form>
</div>
</div>
<footer>
%include footer
</footer>

</body>