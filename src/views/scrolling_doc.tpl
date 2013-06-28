<!DOCTYPE html>
<html>
<head>
<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
<link rel="icon" type="image/png "href="static/image/favicon.ico">
<!-- CSS Code -->
<link rel="stylesheet" href="static/css/style.css">
<link rel="stylesheet" href="static/css/reset.css">
<!-- JS Code -->
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<script src="..static/js/script.js"></script>

 <meta name="viewport" content="width=device-width, initial-scale=1.0">
      
       <link href="http://bootswatch.com/cerulean/bootstrap.css" rel="stylesheet">
        <style>
            body{padding-top: 60px;/* 60px to make the container go all the way to the bottom of the topbar */}
        </style>
        <link href="http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/2.3.0/css/bootstrap-responsive.css" rel="stylesheet">
        <!--[if lt IE 9]>
            <script src="http://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.6.1/html5shiv.js"></script>
        <![endif]-->


<script src="static/jquery.localscroll-1.2.7-min.js" type="text/javascript"></script> 
<script src="static/jquery.scrollTo-1.4.3.1-min.js" type="text/javascript"></script> 

<script type="text/javascript">
$(document).ready(function() {
   $('#nav').localScroll({duration:800});
});

</head>

<body>
 <nav>
%include navbar username=username
</nav>


%for sect in form1:
	<section id="document" data-speed="10" data-type="background">
		
		
		<div class="span12"><legend><h1>{{sect['section_name']}}</h1></legend></div>
		
	<div class="span12">	
	
				
%for key in form2:

%if int(str(key['quest_no'])[:-3]) == sect['section_no']:



	<div class="span6"><strong>{{key['quest']}}</strong></div>

	<div class="span6">{{key['answer']}}</div>


 %end
%end
	
	</div>
	
  </section>
 %end
 <footer>
%include footer
</footer>
 
 
</body>
</html>




