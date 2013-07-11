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
<legend>{{template}}</legend>
<form  action="/convertpdf" method="POST" class="form-horizontal">
  
<label class="control-label">Title   </label>         <input type="text" name= 'title' class="input-large" value="{{company_data['Title']}}"><br>
<label class="control-label">First Name </label>      <input type="text" name= 'first_name' class="input-large" value="{{company_data['First_Name']}}"><br>
<label class="control-label">Last Name </label>       <input type="text" name= 'last_name' class="input-large" value="{{company_data['Last_Name']}}"><br>
<label class="control-label">Company Name </label>     <input type="text" name= 'company_name' class="input-large" value="{{company_data['Company_Name']}}"><br>
<label class="control-label">Email </label>            <input type="text" name= 'email' class="input-large" value="{{company_data['Email_Address']}}"><br>
<label class="control-label">Home Phone </label>       <input type="text" name= 'home_phone' class="input-large" value="{{company_data['Home_Phone']}}"><br>
<label class="control-label">Work Phone </label>       <input type="text" name= 'work_phone'class="input-large" value="{{company_data['Work_Phone']}}"><br>
<label class="control-label">Address Line 1 </label>   <input type="text" name= 'addr_1' class="input-large" value="{{company_data['Address_Line_1']}}"><br>
<label class="control-label">Address Line 2 </label>   <input type="text" name= 'addr_2' class="input-large" value="{{company_data['Address_Line_2']}}"><br>
<label class="control-label">Country or Region </label> <input type="text" name= 'country' class="input-large" value="{{company_data['Country_or_Region']}}"><br>
<label class="control-label">City  </label>            <input type="text" name="city" class="input-large" value="{{company_data['City']}}"><br>
<label class="control-label">State  </label>           <input type="text" name= "state" class="input-large" value="{{company_data['State']}}"><br>
 
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