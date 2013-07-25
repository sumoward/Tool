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
<h1>pricing list</h1>
<div class="container">

<!-- Intro -->
<legend><h3>Please fill in the appropriate quantity</h3></legend><br>

<form class="form-inline" method = "POST" action="/pricing">
<table class="table">
<thead><tr><th>Component</th><th>Unit Price</th><th>Quanity</th><th>Price</th></tr><thead>
%for key, value in pricelist.items():

<tbody><tr><td>{{key}}</td><td>{{value}}</td><td><input type="text" name= "{{key}}" class="input-small search-query"  value ="{{quantity[key]}}"></td><td>{{index_costs[key]}}<td></tr></tbody>

%end
</table>
<br> <button type="submit" class="btn btn-primary btn-large">Submit</button><br>

<h2>Total In-Dex Warehouse and Supply Chain System Costs = {{total_index}}</h2><br>
</form>
</div>
</body>