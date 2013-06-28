<!doctype html>
 
<html lang="en">
<head>

<title>RECAP</title>
 <link href="http://bootswatch.com/cerulean/bootstrap.css" rel="stylesheet">
<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">

</head>

<body>
<nav>
%include navbar
</nav>


  <div id="document">  
%for sect in form1:
	<h1><legend>{{sect['section_no']}}::{{sect['section_name']}}<legend></h1>
	
	
	<div class="container">

<div class="hero-unit">
	%for key in form2:
%if int(str(key['quest_no'])[:-3]) == sect['section_no']:
{{key['quest_no']}}::{{key['quest']}}:::{{key['answer']}}<br>
 %end

%end


FREE TEXT = {{sect['free_text']}}
 </div>
</div>
%end

</div>
    
	

</body>
<footer>
%include footer
</footer>
</html>