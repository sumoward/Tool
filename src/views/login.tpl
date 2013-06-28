<!DOCTYPE html>

<html>
  <head>
        <meta charset="utf-8">
      	<title>Login</title>
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
<img src="static/image/header1_01.gif" class="img-polaroid">
<h3>Welcome - please login to RECAP</h3> 
<form class="form-inline" method="post" action="/login">
  User name &nbsp<input type="text" class="input-small"  name="username" >
  Password &nbsp<input type="text" class="input-small" name="password">
  <button type="submit" class="btn-medium">Submit</button>
  {{login_error}}
</form>
   </div>
   </div> 
    
  </body>

</html>
