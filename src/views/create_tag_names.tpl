<!DOCTYPE html>
<html>
<body>
<a href="/">menu</a>
<h1>A List of existing tags</h1>
<form method = "POST" action="/create_tag_names">
<p>The existing tags are:</p>{{tag_array}}<br><br>
%for i,x in enumerate(tag_array):
<input type="checkbox"  name="tag_name_remove" value={{x}}>{{x}}<br/>

%end

<input type="submit"  name="choice" value="remove"><br/>


<h1>Enter a new tag here</h1>
New Tag : <input type="text" name="new_tag_name" value = ''><br>
<input type="submit"  name="choice" value="add"><br/>

</form>


</body>
</html>

