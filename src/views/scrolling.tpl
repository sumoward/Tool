<!doctype html>
<html class="no-js" lang="en">
<head>
<meta charset="utf-8">
<title>Parallax Scrolling</title>

<!-- CSS Code -->
<link rel="stylesheet" href="static/css/style.css">
<link rel="stylesheet" href="static/css/reset.css">
<!-- JS Code -->
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<script src="static/js/script.js"></script>

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
</script>

</head>

<body>
<div id="nav" class="navbar navbar-inverse navbar-fixed-top">
            <div class="navbar-inner">
                <div class="container">
                    <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse"><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span>
                    </button><a class="brand" href="#home">Project name</a>
                    <div class="nav-collapse collapse">
                        <ul class="nav">
                            <li class="active"><a href="#first">Warehouse</a>
                            </li>
                            <li><a href="#second">Staff</a>
                            </li>
                            <li><a href="#third">Products</a>
                            </li>
                            <li><a href="#fourth">Scope</a>
                            </li>
                            <li><a href="#fifth">Go Live</a>
                            </li>
                            <li><a href="/user_interface">START RECAP</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>

        </div>

<!-- div class="box">

<!-- left column-->

<div class="span3">
<div class="well sidebar-nav sidebar-nav-fixed">
<section name="side" id="" data-speed="300" data-type="background">
%include list_features 
</section>
</div>
</div>
<!-- right column-->
<div class="span9">
<!-- Section #1 -->
<section name="first" id="first" data-speed="300" data-type="background">
    <article> 
    <div class="span3 "><img src="..\static\image\postit1.png" alt="64x64"></div>
    <div class="span3 offset3"><img src="..\static\image\postit2.png" alt="64x64"></div>
    <div class="span3 offset2"><img src="..\static\image\postit3.png" alt="64x64"></div>
    <div class="span3 offset3"><img src="..\static\image\postit4.png" alt="64x64"></div> 
   
            </article> 
</section>
<!-- Section #2 -->
<section name="second" id="second" data-speed="300" data-type="background">
     <article> 
    

    <div class="span3 "><img src="..\static\image\postit5.png" alt="64x64"></div> 
    <div class="span3 offset3"><img src="..\static\image\postit6.png" alt="64x64"></div> 
    <div class="span3 offset3"><img src="..\static\image\postit8.png" alt="64x64"></div>    
			 </article> 
		 
</section>

<!-- Section #3 -->
<section name="third" id="third" data-speed="300" data-type="background">

 <article>    
     
    <div class="span3 offset2"><img src="..\static\image\postit9.png" alt="64x64"></div> 
     <div class="span3 offset1"><img src="..\static\image\postit10.png" alt="64x64"></div>
      <div class="span3 offset2"><img src="..\static\image\postit11.png" alt="64x64"></div> 
     
          
      </article> 

	  
</section>
<section name="fourth" id = "fourth" data-speed="300" data-type="background">

<article> 
	
    <div class="span3 offset1"><img src="..\static\image\postit12.png" alt="64x64"></div>
    <div class="span3 offset2"><img src="..\static\image\postit14.png" alt="64x64"></div>
	<div class="span3 offset3"><img src="..\static\image\postit15.png" alt="64x64"></div>

	</article> 

</section>
	<div class="span3 "><img src="..\static\image\postit13.png" alt="64x64"></div>
	<div class="span3 offset3"><img src="..\static\image\postit16.png" alt="64x64"></div>
	<div class="span3 offset1 "><img src="..\static\image\postit17.png" alt="64x64"></div>
	<div class="span3 offset2"><p><a href="/user_interface" class="btn btn-primary btn-large">Start RECAP </a></div>

<section name="fifth" id = "fifth" data-speed="300" data-type="background">

</div>
</section>

</div>


</body>

</html>
