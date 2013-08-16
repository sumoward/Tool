<doctype html>
<head>

<title>Pricing</title>

  <META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="icon" type="image/png "href="/static/image/favicon.ico">
        
        <link href="/static/css/bootstrap.min.css.gz" rel="stylesheet">
        <link href="/static/css/bootstrap-responsive.min.css.gz" rel="stylesheet">
        <style type="text/css">            body{padding-top: 60px;padding-bottom: 40px;}</style>   
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
<div class="container">
%include buttons
<table class="table table-condensed">
<thead><tr><th><legend><h4>Principal Systems Indicative Pricing</h4></legend></th></tr><tr><th>Section No</th><th>Section name</th><th><p class = "text-right">Section Total</p></th</tr><thead>
%for section in pricelist:
<tbody><tr><td>{{section['section_no']}}</td><td><a href ="/pricing/{{section['section_no']}}">{{section['section_name']}}</a></td><td><p class = "text-right">{{section['section_total']}}</p></td></tr>
%end
<tr><td></td><td></td><td></td></tr>
<tr><td><h4>Total cost for InDex</h4</td><td></td><td><p class = "text-right">{{overall_total}}</p></td></tr></tbody>
</table>


<h1> annual maintenance </h1>

Standard Maintenance 			20% of Software Value 
24 X 7 Critical Maintenance 	30% of Software Value

</div>
</body>