<!DOCTYPE html>
<html>
<head>
<title>quest</title>
</head>
<body>
<a href="/process_sections">edit sections</a></br>
<h1>Questions</h1>

{{cursor}}</br>
{{section}}

<H1>Edit the question you would like to change</H2>

 <div id='outer'>
 
 
   <form method = "POST" action="/update_questions">
    <input type="hidden" name = cursor value = "{{cursor}}">
   	<input type="hidden" name = section value = "{{section}}">
    
  
     %for i, x in enumerate(cursor):
   <div id='position'>Location : {{i + 1}} </div>

          <div id="buttons">  
                	
           <input type="checkbox"  name="{{'form_name_' + str(i)}}" value="on"  >{{x}}
            
                                %end  
                  
        </div>
        
        
        <input type="submit"  name="choice" value="remove"><br/>
        </br> <h3>Choose the location you want to enter the new data at and type in your new question
        If you do not select an option then the question will be added as the last question<h3></br>
        <input type="text box"  name="new_question" value="add new question here">
        </br>
        
        
Select the appropriate tags for this question(if any)</br>
  <select size="4" name="tags" multiple="yes" > 
  <option value="ROI" >ROI</option>
  <option value="tag1" >Tag1</option>
  <option value="tag2" >Tag2</option>
  <option value="tag3" >Tag3</option>
</select>
</div>
          </br>
        <input type="submit"  name="choice" value="add"><br/>
     </form>
</div>
</body>
</html>
