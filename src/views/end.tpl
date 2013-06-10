<!doctype HTML>
<html>
<head>
<title>end</title>
</head>
<body>
<br/>
%for key in form:
<div>{{' '.join(key.split('_'))}} : {{form[key]}}<br><div>
%end
<br/>




</body>
</html>