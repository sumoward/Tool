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

<form enctype="multipart/form-data" name="document_download" action="/documentation" method="post" class="form-horizontal input-xxlarge">

<label class="checkbox" name="document_download">
    <input name="document_download" type="checkbox" value="0"> <a href="https://docs.google.com/spreadsheet/ccc?key=0AvtA3_n0IgBedFBpZElfYW8yZldvbHVxM29tR3kwRlE#gid=0">ASN & Pallet and Case Label Data Capture Template.xlsx</a><br>
    <input name="document_download" type="checkbox" value="1"><a href="https://docs.google.com/spreadsheet/ccc?key=0AvtA3_n0IgBedDBDQ08tNjRZLUdFbjI0WUVFMW4tVWc#gid=0">BRC Data Capture Template.xlsx</a><br>
    <input name="document_download" type="checkbox" value="2"><a href="https://docs.google.com/spreadsheet/ccc?key=0AvtA3_n0IgBedEdMS2wwODZYOEc4V05YS3FZRWdjN2c#gid=0">Customer charges.xlsx</a><br>
    <input name="document_download" type="checkbox" value="3"><a href="https://docs.google.com/spreadsheet/ccc?key=0AvtA3_n0IgBedDh4d1hlM0RMbC04cElZZlFCbGR1UGc#gid=0">In-DEX User Profiles Data Capture Template.xlsx</a><br>
    <input name="document_download" type="checkbox" value="4"><a href="https://docs.google.com/spreadsheet/ccc?key=0AvtA3_n0IgBedDViM3Z4czk5d29wM3ZsT3g3NWdEWVE#gid=0">In-DEX WMS Functionality Checklist.xls</a><br>
    <input name="document_download" type="checkbox" value="5"><a href="https://docs.google.com/spreadsheet/ccc?key=0AvtA3_n0IgBedGU1N0FDVWFPa0JTXzJOc0dJeEg5NUE#gid=0">Master Charges.xlsx</a><br>
    <input name="document_download" type="checkbox" value="6"><a href="https://docs.google.com/spreadsheet/ccc?key=0AvtA3_n0IgBedGs5MWVudVd3TVhPTzZLNWFqb2MtWnc#gid=0">Product Code Data Capture Template.xlsx</a><br>
    </label>


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
<a href="https://docs.google.com/spreadsheet/ccc?key=0AvtA3_n0IgBedFBpZElfYW8yZldvbHVxM29tR3kwRlE#gid=0">ASN & Pallet and Case Label Data Capture Template.xlsx</a>
%include footer
</footer>
</html>