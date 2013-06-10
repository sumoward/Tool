<!doctype HTML>
<html>
<head>
<title>roi1</title>
<link rel="stylesheet" type="text/css" href="/layoutcss.css">
</head>
<body>

roi1 is here<br/>

{{roi1_holder}}
%for key in roi1_holder:

{{' '.join(key.split('_'))}} :: {{roi1_holder[key]}}<br>

%end


<br/>
</body>
</html>