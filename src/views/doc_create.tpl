<!DOCTYPE html>
<html>

<head>
<meta charset="utf-8">
<link href="http://bootswatch.com/cerulean/bootstrap.css" rel="stylesheet">
</head>


<body>



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
</html>