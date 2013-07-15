<doctype html>
<head>

<title>RECAP</title>
    
        <meta charset="utf-8">
        <META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="icon" type="image/png "href="/static/image/favicon.ico">
        
        <link href="/static/css/bootstrap.min.css.gz" rel="stylesheet">
        <link href="/static/css/bootstrap-responsive.min.css.gz" rel="stylesheet">
        <style type="text/css">            body{padding-top: 60px;padding-bottom: 40px;}        </style>   
        <link rel="stylesheet" href="/static/jsfiles/jquery-ui-1.10.2.custom.min.css.gz" />
                       
  <script src="/static/jsfiles/jquery.min.js.gz"></script>
  <script src="/static/jsfiles/bootstrap.min.js.gz"></script>   
  <script src="/static/jsfiles/jquery-1.9.1.min.js.gz"></script>
  <script src="/static/jsfiles/jquery-ui.js.gz"></script>
  
  <script>
  $(function() {
        $( "#accordion" ).accordion({
            collapsible: true,
            active: false,
            heightStyle: "content",      
        }); 
         $("#accordion").css("display", "block");      
    });
      
  </script>



</head>
<body>
<nav>
%include navbar username=username
</nav>
<div>
%include accordian form1=form1, form2 = form2, username=username
 </div>
</body>
<footer>
%include footer
</footer>
</html>