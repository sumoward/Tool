<DOCTYPE html>

<html>
  <head>
        <meta charset="utf-8">
      	<title>Login</title>
      	<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">
       <link rel="icon" type="image/png "href="static/image/favicon.ico">
<link href="/static/css/bootstrap.min.css.gz" rel="stylesheet">
<link href="/static/css/bootstrap-responsive.min.css.gz" rel="stylesheet">

  </head>

  <body>

<div class="container">
<div class="hero-unit"> 
<a href="http://www.principalsystems.com/"><img src="static/image/header1_01.gif" class="img-polaroid"></a>
<h3>Welcome - please login to RECAP</h3> 
<form class="form-horizontal" method="post" action="/login">
  User name &nbsp<input type="text" class="input-small"  name="username" >
  Password &nbsp<input type="text" class="input-small" name="password">
  <button type="submit" class="btn-medium">Submit</button>
  {{login_error}}
</form>
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
