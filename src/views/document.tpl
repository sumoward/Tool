<!doctype html>
 
<html lang="en">
<head>

<title>RECAP</title>
 <link href="http://bootswatch.com/cerulean/bootstrap.css" rel="stylesheet">
<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
<link rel="icon" type="image/png "href="static/image/favicon.ico">

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
<footer>
%include footer
</footer>
</html>