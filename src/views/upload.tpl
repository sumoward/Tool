<!doctype HTML>
<html>
<head>
<title></title>
<link rel="stylesheet" type="text/css" href="/layoutcss.css">
 <link href="http://bootswatch.com/cerulean/bootstrap.css" rel="stylesheet">
</head>

<nav>
%include navbar
</nav>


<body>
<div class="container">

<div class="hero-unit">
<br/>

    <h3>Please upload your documentation here</h3>   
<div> 
<form enctype="multipart/form-data" action="/saved_file" method="post">
<input type="file" name="uploadField" class="btn btn-primary " />
<input type="submit" value="Upload" class="btn btn-primary btn-large">
</form>


<br/>
</div>
</div>


<br/>
</body>
<footer>
%include footer
</footer>
</html>