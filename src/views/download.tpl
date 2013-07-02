<!doctype HTML>
<html>
<head>
<title>Download</title>
<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
<link rel="stylesheet" type="text/css" href="/layoutcss.css">
<link href="http://bootswatch.com/cerulean/bootstrap.css" rel="stylesheet">
<link rel="icon" type="image/png "href="static/image/favicon.ico">





 </head>
 
<body>
<nav>
%include navbar username=username
</nav>
<div class="container">

<div class="hero-unit">
<legend>Select the documents you want to share with the client</legend>
<br/>

<form enctype="multipart/form-data" name="template_download" action="/documentation" method="post" class="form-horizontal input-xxlarge">
<select size="7" name="document_download" multiple="yes" > 
  <option value="0" >ASN & Pallet and Case Label Data Capture Template.xlsx</option>
  <option value="1" >BRC Data Capture Template.xlsx</option>
  <option value="2" >Customer charges.xlsx</option>
  <option value="3" >In-DEX User Profiles Data Capture Template.xlsx</option>
  <option value="4" >In-DEX WMS Functionality Checklist.xls</option>
  <option value="5" >Master Charges.xlsx</option>
  <option value="6" >Product Code Data Capture Template.xlsx</option> 
</select>
<br>
Insert the clients email here<br>
<input type="text" name= "customer" class="input-large search-query"  value = "" ><br><br>
<input type="submit" value="E-Mail" class="btn btn-primary btn-large">
</form>
{{message}}

</div>
</div>

<br/>



<br/>
</body>
<footer>
%include footer
</footer>
</html>