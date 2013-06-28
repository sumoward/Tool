<!DOCTYPE html>
<html>
 <head> 
        <meta charset="utf-8">
      	<title>Welcome</title>
      	<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
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
</body>
</html>
