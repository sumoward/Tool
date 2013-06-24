<!DOCTYPE html>

<html>
  <head>
        <meta charset="utf-8">
        <title>Sign UP</title>
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
	<legend>
    Already a user? <a href="/login">Login</a><p>
    <legend>
    <h2>Signup</h2>
    <form method="post">  
    Username<input type="text" name="username" value="{{username}}"> 
    Password<input type="password" name="password" value="">
    Verify Password <input type="password" name="verify" value="">
    <button type="submit" class="btn-medium">Submit</button>
    </form>
</div>
</div>
 </body>

</html>
