<!doctype html>
<html lang="en">
<head>
 <title>roi</title>
</head>
<body>


 
 ROI
 
<form method = "POST" action="/roi_recalculate">
<input type="hidden"  name = roi_holder value = "{{roi_holder}}">
 
 %for key in roi_holder:

{{key}}
%end



<input type="submit" value="Submit">
</form>
 



</body>
</html>