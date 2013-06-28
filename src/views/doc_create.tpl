<!DOCTYPE html>
<html>

<head>
<meta charset="utf-8">
<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
<title>generate customer document</title>
<link rel="icon" type="image/png "href="static/image/favicon.ico">
<link href="http://bootswatch.com/cerulean/bootstrap.css" rel="stylesheet">
</head>

<body>
  <nav>
%include navbar username=username
</nav>


<form class="" method = "POST" action="/doc_create">
  <fieldset>
    <legend>Document</legend>
    <label>section name</label>
    <input type="text" value="{{section}}" name = 'section'>
    <span class="help-block">Example block-level help text here.</span>
    <textarea rows="40" cols="20" name ="text_box" >{{text_box}}</textarea>
    <button type="submit" class="btn">Submit</button>
  </fieldset>
</form>




<h1>{{section}}</h1>

<p>{{text_box}}</p>

</body>
<footer>
%include footer
</footer>
</html>