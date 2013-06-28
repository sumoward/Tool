<!DOCTYPE html>
<html>
<head>
<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
<title>Questions</title>
</head>
<body>

<a href="/">menu</a></br>
<h1>Template</h1>
{{cursor}}

<H1>Which section would you like to edit.</H2>

    <div id='outer'>
     %for i, x in enumerate(cursor):
   <div id='position'>Location : {{i + 1}} </div>
   
   
    <form method = "POST" action="process_questions">
        <div id="buttons"> 
               
      <input type="checkbox"  name="form_name" value={{i +1}}>{{x}}<br/>
          %end    
          <input type="submit"  name="choice" value="Select Section"><br/>   
        </div>
   
	</form>
</div>
<footer>
%include footer
</footer>
</body>
</html>
