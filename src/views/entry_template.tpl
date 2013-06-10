<!doctype HTML>
<html
<head>
<title>
Account
</title>
</head>
<body>
%if (username != None):
Welcome {{username}}        <a href="/logout">Logout</a> | 
%end
<br/>
<p>
{{account}}
<br/>
% for value in account:
	<br/>
	{{value}}
%end
</p>
<<br/>
<p>
The representative handling the account is :{{username}}
</p>
</body>
</html>


