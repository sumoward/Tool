<doctype html>
<head>
 
</head>
<body>



  
<div id="accordion" style="display: none;">
<!--set the subtitle compare-->
%comp=""
%for x, sect in enumerate(form1):
%check1 = True
<!-- Section header -->
<h3 id='top' class="{{sect['section_name']}}">{{sect['section_name']}}</h3>

<div class="container">


<!-- Intro -->
<legend><h3>Please fill in the appropriate details</h3></legend><br>

<form class="form-inline" method = "POST" action="/form_end">
<input type="hidden"  name = 'section' value = "{{sect['section_no']}}">



%for key in form2:

<!-- Subhead -->
%if int(str(key['quest_no'])[:-3]) == sect['section_no']:

%if key['subhead'] != comp and key['subhead'] !=None:
<div class="span6"><br><h4>{{key['subhead']}}</h4><br></div>
%comp = key['subhead']
%end:


<!-- Questions -->
<div class="span6"><label>{{key['quest']}}</label></div>
%if key['answer']:
<div class="span4"><input type="text" name= "{{key['quest_no']}}" class="input-large search-query"  value ="{{key['answer']}}" ></div>
%else:
<div class="span4"><input type="text" name= "{{key['quest_no']}}" class="input-large search-query"  value ="" ></div>
%end
%end
%end



<div class="span6"><br><p>Enter any additional information here</p> <br>
%if sect['free_text']:
<textarea name= "free_text" rows="5" cols="30">{{sect['free_text']}}</textarea><br></div><br>
%else:
<textarea name= "free_text" rows="5" cols="30"></textarea><br></div><br>
%end


<div class="span6"><br> <button type="submit" class="btn btn-primary btn-large">Submit</button></div>


</form>
</div>

 
 </body>
</html>