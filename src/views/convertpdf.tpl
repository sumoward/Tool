<!doctype HTML>
<html>
<head>
<title></title>


       <link href="http://bootswatch.com/cerulean/bootstrap.css"
        rel="stylesheet">
       <META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
        <link href="http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/2.3.0/css/bootstrap-responsive.css"
</head>

<nav>
%include navbar username=username
</nav>


<body>

<div class="container">
<div class="hero-unit">
<form  action="/convertpdf" method="POST" class="form-inline">
  <fieldset>
    <legend>Document creation, Please select your template</legend>
    <label class="checkbox">
      <input type="checkbox" name = "template" value ="{{template}}"> {{template}}
    </label>
    <button type="submit" class="btn">Submit</button>
  </fieldset>
</form>
<div class="hero-unit">

<form class="form-inline">
 <div class="span3">Title</div>  <div class="span4"><input type="text" class="input-large" value="{{company_data['Title']}}"></div><br>
  <div class="span3">First Name</div>  <div class="span4"><input type="text" class="input-large" value="{{company_data['First_Name']}}"></div><br>
  <div class="span3">Last Name</div>  <div class="span4"><input type="text" class="input-large" value="{{company_data['Last_Name']}}"></div><br>
  <div class="span3">Company Name</div>  <div class="span4"><input type="text" class="input-large" value="{{company_data['Company_Name']}}"></div><br>
  <div class="span3">Email</div>  <div class="span4"><input type="text" class="input-large" value="{{company_data['Email_Address']}}"></div><br>
  <div class="span3">Home Phone</div>  <div class="span4"><input type="text" class="input-large" value="{{company_data['Home_Phone']}}"></div><br>
  <div class="span3">Word Phone</div>  <div class="span4"><input type="text" class="input-large" value="{{company_data['Work_Phone']}}"></div><br>
  <div class="span3">Address Line 1</div>  <div class="span4"><input type="text" class="input-large" value="{{company_data['Address_Line_1']}}"></div><br>
  <div class="span3">Address Line 2</div>  <div class="span4"><input type="text" class="input-large" value="{{company_data['Address_Line_2']}}"></div><br>
  <div class="span3">Country or Region</div>  <div class="span4"><input type="text" class="input-large" value="{{company_data['Country_or_Region']}}"></div><br>
  <div class="span3">City</div>  <div class="span4"><input type="text" class="input-large" value="{{company_data['City']}}"></div><br>
  <div class="span3">State</div>  <div class="span4"><input type="text" class="input-large" value="{{company_data['State']}}"></div><br>
 
 
 
  <button type="submit" class="btn">Confirm</button>
</form>
</div>

% if message:
<h3>{{message}}</h3>
%end

</div></div>
<br/>
</body>
<footer>
%include footer
</footer>
</html>