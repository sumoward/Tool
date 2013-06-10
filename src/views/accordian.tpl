<!doctype html>
 
<html lang="en">
<head>

  <meta charset="utf-8" />
  <title>jQuery UI Accordion - Default functionality</title>
  <link rel="stylesheet" href="/static/jquery-ui-1.10.2.custom.min.css.gz" />
  <script src="http://code.jquery.com/jquery-1.9.1.js"></script>
  <script src="http://code.jquery.com/ui/1.10.2/jquery-ui.js"></script>
  
  <script>
  $(function() {
        $( "#accordion" ).accordion({
            collapsible: true,
            active: false,
            heightStyle: "content"
        });
    });
  </script>
  

   <meta charset="utf-8">
        
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">
        <link href="http://bootswatch.com/cerulean/bootstrap.css"
        rel="stylesheet">
       
        <link href="http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/2.3.0/css/bootstrap-responsive.css"
        rel="stylesheet">
        <!--[if lt IE 9]>
            <script src="http://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.6.1/html5shiv.js"></script>
        <![endif]-->

</head>
<body>
  
<div id="accordion">

%for x, sect in enumerate(form1):
%check1 = True
<!-- Section header -->
<h3 id='top'>{{sect['section_no']}}::{{sect['section_name']}}</h3>

<div class="container">
<div class="hero-unit">

<!-- Intro -->

%if sect['intro'] != 'None' and  check1 == True:
<legend>Intro:{{sect['intro']}}:intro</legend><br>
%check1 = False
%end


<form class="form-inline" method = "POST" action="/form_end">
<input type="hidden"  name = 'section' value = "{{sect['section_no']}}">

%check2 = True
%for key in form2:

<!-- Subhead -->
%if int(str(key['quest_no'])[:-3]) == sect['section_no']:

%if key['subhead'] != None and check2 == True:
<div class="span6"><br><h4>:test:{{key['subhead']}}::</h4><br></div>
%check2 = False
%end

<!-- Questions -->
<div class="span6"><label>{{key['quest_no']}}::{{key['quest']}}</label></div>

<div class="span4"><input type="text" name= "{{key['quest_no']}}" class="input-large search-query"  value ="{{key['answer']}}" ></div>

%end


%end



<div class="span6"><br><p>Enter any additional information here</p> <br><textarea name= "free_text"rows="3">{{sect['free_text']}}</textarea><br></div>
<br>


<div class="span6"><br> <button type="submit" class="btn btn-primary btn-large">Submit</button></div>


</form>
</div>
</div>

 </body>
</html>