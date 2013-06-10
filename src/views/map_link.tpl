<!DOCTYPE html>
<html>

<head>
<meta charset="utf-8">
<title>Map Link</title>

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






</head>
<body>
   <nav>
%include navbar
</nav>
<h1>Map Link</h1>

<div class="image">


<img src="../static/image/warehouse.jpg" alt="warehouse" usemap = "#warehousemap">

<map name="warehousemap">
  <area shape="rect" coords="64,449,366,662" alt="Sales" href="/">
  <area shape="rect" coords="610,130,912,343" alt="Existing Technology" href="/user_interface">
  <area shape="rect" coords="490,691,792,904" alt="Picking" href="/scoping">
  <area shape="rect" coords="1069,500,1371,713" alt="Loading" href="/scoping">
</map>


</div>


</body>
</html>