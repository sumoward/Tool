<!DOCTYPE html>
<html>
 <head> 
        <meta charset="utf-8">
      	<title>Welcome</title>
      	<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
      	<link rel="icon" type="image/png "href="static/image/favicon.ico">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">
        <link href="http://bootswatch.com/cerulean/bootstrap.css" rel="stylesheet">
        <style type="text/css">
            body{padding-top: 60px;padding-bottom: 40px;}
        </style>
        <link href="http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/2.3.0/css/bootstrap-responsive.css" rel="stylesheet">
        <!--[if lt IE 9]>
            <script src="http://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.6.1/html5shiv.js"></script>
        <![endif]-->
 </head>
 <body>      
<div class="container">
<div class="hero-unit">  

<img src="static/image/header1_01.gif" class="img-polaroid">

    <h1>Welcome {{username}}</h1>
<ul>
<li><a href="/">Start Recap Introduction</a></li>
<li>
<a href="/logout">Logout</a>
</li>
<li>
<a href="/user_interface">Sales</a>
</li>
<li>
<a href="/scoping">Scoping</a>
</li>
<li>
<a href="/professional_services">Professional Services</a>
</li>

%if (username == 'joe' or 'brian' or 'phil'):
<li>
<a href="/signup">Register new customer</a>
</li>
<li>
<a href="/">Admin</a>
</li>

%end
</ul>
</div>
</div>


    <!-- google analytics -->
   <script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-42099327-1', 'principalwms.com');
  ga('send', 'pageview');

</script> 

<footer>
%include footer
</footer>
</body>

</html>
