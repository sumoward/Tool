<!DOCTYPE html>
<html>
<head>
<title>Section</title>
<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
</head>
<body>

<a href="/">menu</a></br>
<h1>Template</h1>
{{cursor}}

<H1>Which Section would you like to edit.</H2>

    <div id='outer'>
     %for i, x in enumerate(cursor):
   <div id='position'>Location : {{i + 1}} </div>
   
   
    <form method = "POST" action="process_sections">
        <div id="buttons"> 
               
      <input type="checkbox"  name="form_name" value={{i +1}}><input type="text" size= 80 name="{{'section_edit_'+ str(i)}}" value='{{x}}'><br/>
          %end    
             
        </div>
    
	<input type="submit"  name="choice" value="remove">::<input type="submit"  name="choice" value="edit"><br/><br/>
	
	 </br> <h3>Choose the location you want to enter the new Section
        If you do not select an option then the question will be added as the last question<h3></br>
        <input type="text box"  name="new_section" value="add new Section here">
        </br>
	<input type="submit"  name="choice" value="add"><br/>
	
	
	
	</form>
</div>

</body>
</html>
