<!DOCTYPE html>
<html>
<head>
<title>Tags</title>
</head>
<body>

<a href="/">menu</a></br>
<h1>Template</h1>
{{cursor}}


<H1>To edit a questions Tags choose a section below to retrieve its associated questions</H2>

    <div id='outer'>
    <form method = "POST" action="process_tags">
     %for i, x in enumerate(cursor):
  SECTION : {{i + 1}}    
    
        <input type="checkbox"  name="form_name" value={{i +1}}>{{x['section_string']}}<br/><br/>
    
    
	%for i, each in enumerate(range(len(x['section_tag']))):
		
	Tag:<input type="checkbox"  name="tag_no" value="[{{x['section']}},'{{x['section_tag'][i]}}']">{{x['section_tag'][i]}}<br/><br/> 
			         
           %end 
          %end   <br/>   <br/>  
          <br/>  <input type="submit"  name="choice" value="Select Section">  <input type="submit"  name="choice" value="remove section tags"><br/> <br/>   
        
        
         <br/>  
        Select the appropriate tags for this section(if any)</br>
  <select size="3" name="tags" multiple="yes" > 
  <option value="ROI" >ROI</option>
  <option value="tag1" >Tag1</option>
  <option value="tag2" >Tag2</option>
  <option value="tag3" >Tag3</option>
</select>

          </br><br/>
        <input type="submit"  name="choice" value="add section tag"><br/>
        
        
   
	</form>
</div>

</body>
</html>
