<!DOCTYPE html>
<html>
<head>
<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
<title>questions</title>
</head>
<body>

<a href="/">menu</a></br>
<h1>Template</h1>
{{cursor}}</br>section:{{section}}

<H1>Which question would you like to edit.</H2>

    <div id='outer'>
     %for i, x in enumerate(cursor):
   <div id='position'>QUESTION : {{i + 1}} </div>
   
   
    <form method = "POST" action="/update_questions">
    <input type="hidden"  name = 'section' value = "{{section}}">
    <input type="hidden"  name = 'cursor' value = "{{cursor}}">
        <div id="buttons"> 
               
      <input type="checkbox"  name="{{'form_name_'+ str(i)  }}" value="on"><input type="text" size= 80 name="{{'quest_edit_'+ str(i)}}" value='{{x}}'><br/>
          %end    
             
        </div>
    
	<input type="submit"  name="choice" value="remove">::<input type="submit"  name="choice" value="edit"><br/><br/>
	
	 </br> <h3>Choose the location you want to enter the new Section
        If you do not select an option then the question will be added as the last question<h3></br>
        <input type="text box"  name="new_question" value="add new Section here">
        </br>
	<input type="submit"  name="choice" value="add"><br/>
	
	
	
	</form>
</div>

</body>
</html>
