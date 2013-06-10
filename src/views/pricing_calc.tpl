<!doctype HTML>
<html>
<head>
<title>Pricing</title>
</head>
<body>
<h3> The appropriate pricing modifier is : {{pricing_holder[0]}}</h3><br/>
<h3> The currency we are pricing in is  :{{pricing_holder[1]}}</h3><br/>

<h3> The prices for InDex is </h3><br/>	
%for key in pricing_holder[2]:
<div class ='display_field'>{{' '.join(key.split('_'))}}   =    {{'\t' + pricing_holder[2][key]}} <br><div>
%end


</body>
</html>