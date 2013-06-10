<!doctype HTML>
<html>
<head>
<title>Create a new account</title>
</head>

<body>
%if (username != None):
Welcome {{username}}        <a href="/logout">Logout</a> | <a href="/"> Home</a><p>
%end


<form action="/newaccount" method="POST">

{{errors}}
<h2>How many forklifts</h2>


<input type="text" name="title" size="120" value="{{title}}"><br>


<h2>Details of forklifts<h2>
<textarea name="account" cols="120" rows="20">{{account}}</textarea><br>

<input type="submit" value="Submit">

</body>
</html>

