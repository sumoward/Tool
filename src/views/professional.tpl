<doctype html>
<head>
<title>Pricing</title>
     <meta charset="utf-8">
        <META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="icon" type="image/png "href="/static/image/favicon.ico">      
        <link href="/static/css/bootstrap.min.css.gz" rel="stylesheet">
        <link href="/static/css/bootstrap-responsive.min.css.gz" rel="stylesheet">
        <style type="text/css">body{padding-top: 60px;padding-bottom: 40px;}</style>   
        <link rel="stylesheet" href="/static/jsfiles/jquery-ui-1.10.2.custom.min.css.gz" />                       
  <script src="/static/jsfiles/jquery.min.js.gz"></script>
  <script src="/static/jsfiles/bootstrap.min.js.gz"></script>   
  <script src="/static/jsfiles/jquery-1.9.1.min.js.gz"></script>
  <script src="/static/jsfiles/jquery-ui.js.gz"></script>
 <script src="/static/jsfiles/bootstrap.min.js.gz"></script> 
   
</head>
<body>
<nav>
%include navbar username=username
</nav>
<div class="box">
<h2>Professional Services</h2>
To ascertain a credible day count requires Principal Systems personnel to come on site and perform a detailed scoping exercise to review existing operations, to ascertain the required level of process re-engineering to optimize processes and the level of integration required to interface to existing IT systems.   Below are the typically tasks that are required and estimated day count

%for x in range(3):

<div class="span4">

<form class="form-condensed table-hover" method = "POST" action="/professional" enctype="multipart/form-data">
<input type="hidden" name = "section_no"  value ="{{day_count[x]['section_no']}}">
<table class="table table-condensed">
<thead><tr><th><legend><h4>{{day_count[x]['name']}}</h4></legend></th></tr><tr><th>Description</th><th>Days</th></tr><thead>
%for day in day_count[x]['categories']:

<tbody><tr><td>{{day['category']}}</td><td><input type="text" name = "quantity" class="input-small" value ="{{day['no_days']}}"></td></tr>

%end
<tr><td><h4>Total </h4</td><td></td><td></td><td><p class = "text-right">{{day_count[x]['overall_total']}}</p></td></tr></tbody>
</table>
<br><button type="submit" class="btn btn-primary btn-large">Submit</button><br>

</form>

</div>
%end

</div>
</body>