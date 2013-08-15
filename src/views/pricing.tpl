<doctype html>
<head>
<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
<link rel="icon" type="image/png "href="static/image/favicon.ico">
<link href="/static/css/bootstrap.min.css.gz" rel="stylesheet">
<link href="/static/css/bootstrap-responsive.min.css.gz" rel="stylesheet">
<title>Pricing</title>

<script src="/static/jsfiles/jquery.min.js.gz"></script>
<meta name="viewport" content="width=device-width, initial-scale=1.0">    
     
        <style>
            body{padding-top: 60px;/* 60px to make the container go all the way to the bottom of the topbar */}
        </style>
       <script src="/static/jsfiles/bootstrap.min.js.gz"></script>      
</head>
<body>
<a href="/pricing_main">price</a>

<ul>
<li><a href="/pricing/1">section1</a></li>
<li><a href="/pricing/2">section2</a></li>
<li><a href="/pricing/3">section3</a></li>
<li><a href="/pricing/4">section4</a></li>
<li><a href="/pricing/5">section5</a></li>


</ul>

<h1>pricing list</h1>
<div class="container">

<!-- Intro -->
<legend><h3>{{pricelist[0]['section_name']}}</h3></legend><br>

<form class="form-condensed table-hover" method = "POST" action="/pricing_calc" enctype="multipart/form-data">
<input type="hidden" name = "section_no"  value ="{{pricelist[0]['section_no']}}">
<table class="table">
<thead><tr><th>Component</th><th>Unit Price</th><th>Quanity</th><th>Price</th></tr><thead>

%for category in pricelist[0]['categories']:
<tbody><tr><td>{{category['category']}}</td><td>{{category['list_price']}}</td><td><input type="text" name = "quantity" class="input-small" value ="{{category['quantity']}}"></td><td>{{category['sub_total']}}</td></tr></tbody>
%end

</table>
<br> <button type="submit" class="btn btn-primary btn-large">Submit</button><br>

<h2>Total In-Dex Warehouse and Supply Chain System Costs = </h2><br>
</form>
</div>
</body>