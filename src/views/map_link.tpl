<!DOCTYPE html>
<html>
<head>
<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
<meta charset="utf-8">
<title>Map Link</title>

<link rel="icon" type="image/png "href="static/image/favicon.ico">
<link href="/static/css/bootstrap.min.css.gz" rel="stylesheet">
<link href="/static/css/bootstrap-responsive.min.css.gz" rel="stylesheet">

<script src="/static/jsfiles/jquery-1.9.1.min.js.gz"></script>

<script src="..static/jsfiles/script.js"></script>
<meta name="viewport" content="width=device-width, initial-scale=1.0">    
     
        <style>
            body{padding-top: 60px;/* 60px to make the container go all the way to the bottom of the topbar */}
        </style>
       <script src="/static/jsfiles/bootstrap.min.js.gz"></script> 

</head>
<body>
   <nav>
%include navbar username=username
</nav>

<div class="image">
<img src="../static/image/warehouse.jpg" alt="warehouse" usemap = "#warehousemap" height="1000" width="750">

<map name="warehousemap">
  <area shape="rect" coords="90, 270, 520, 550" alt="scoping" href="/scoping">
  <area shape="rect" coords="420, 130, 716, 250" alt="user interface" href="/user_interface">
  <area shape="rect" coords="560, 330, 970, 540" alt="professional services" href="/professional_services">
  
</map>


</div>
<footer>
%include footer
</footer>

</body>
</html>