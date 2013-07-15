<!DOCTYPE html>
<html>
<head>

<title>Answers</title>
<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">

<link rel="icon" type="image/png "href="static/image/favicon.ico">
<link href="/static/css/bootstrap.min.css.gz" rel="stylesheet">
<link href="/static/css/bootstrap-responsive.min.css.gz" rel="stylesheet">


<script src="/static/jsfiles/jquery.min.js.gz"></script>
<meta name="viewport" content="width=device-width, initial-scale=1.0">    
     
        <style>
            body{padding-top: 60px;/* 60px to make the container go all the way to the bottom of the topbar */}
        </style>
       <script src="/static/jsfiles/bootstrap.min.js.gz"></script> 
       
       <script src="/static/jsfiles/scripts.js.gz"></script>
       <script src="/static/jsfiles/jquery.localscroll-1.2.7-min.js.gz"></script>
       <script src="/static/jsfiles/jquery.scrollTo-1.4.3.1-min.js.gz"></script>
</head>

<body>
 <nav>
%include navbar username=username
</nav>

<div class="span12">
%for sect in form1:
%if sect['section_no'] < 13:
%page="user_interface"
%else:
%page="scoping"
%end
		<div class="span12"><legend><a href="/{{page}}#{{sect['section_name']}}"><h1>{{sect['section_name']}}</h1></a></legend></div>
		
	<div class="span12">	
	
				
%for key in form2:

%if int(str(key['quest_no'])[:-3]) == sect['section_no']:



	<div class="span6"><strong>{{key['quest']}}</strong></div>

	<div class="span6">{{key['answer']}}</div>


 %end
 
%end
	
	</div>
	
 <div class="span6"><strong>Additional Information(if supplied): </strong></div><br>
 %if sect['free_text']:
 <div class="span6">{{sect['free_text']}}</div>
 %end
 %end
 </div>
 
</body>
</html>




