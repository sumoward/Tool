<!DOCTYPE html>
<html>
<head>
<title>Tags</title>
<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
</head>
<body>

<a href="/">menu</a></br>
<h1>Tags</h1>

{{tags}}<br/>{{section}}

<H1>Which tags would you like to edit.</H2>
	<form method = "POST" action="process_tags">
	<input type="hidden" name = "section" value = "{{section}}">
	
	%for i, x in enumerate(tags):
	
	
	<br/><input type="checkbox"  name="quest_no" value="{{x['quest_no']}}">QUESTION{{' '  + str(i + 1)}}	{{x['quest']}}</br><br/>
	
	
	%for i, each in enumerate(range(len(x['tags']))):
	
	
	Tag:<input type="checkbox"  name="tag_no" value="[{{x['quest_no']}},'{{x['tags'][i]}}']">{{x['tags'][i]}}<br/>
	%end 
	%end  
	<br/>

    
	<input type="submit"  name="choice" value="remove"><br/>
	
	Select the appropriate tags for this question(if any)</br>
  <select size="3" name="tags" multiple="yes" > 
  <option value="ROI" >ROI</option>
  <option value="tag1" >Tag1</option>
  <option value="tag2" >Tag2</option>
  <option value="tag3" >Tag3</option>
</select>

          </br><br/>
        <input type="submit"  name="choice" value="add"><br/>
	
	
	
	</form>
</div>
<footer>
%include footer
</footer>
</body>
</html>
