<!doctype HTML>
<html>
<head>
<title>Create pdf</title>


       
        
       <META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
<link rel="icon" type="image/png "href="static/image/favicon.ico">
<link href="/static/css/bootstrap.min.css.gz" rel="stylesheet">
<link href="/static/css/bootstrap-responsive.min.css.gz" rel="stylesheet">


<script src="/static/jsfiles/jquery.min.js.gz"></script>
<meta name="viewport" content="width=device-width, initial-scale=1.0">    
     
        <style>
            body{padding-top: 60px;/* 60px to make the container go all the way to the bottom of the topbar */}
        </style>
<script src="/static/jsfiles/bootstrap.min.js.gz"></script> 
        
        
        
        
        
        
        
        
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