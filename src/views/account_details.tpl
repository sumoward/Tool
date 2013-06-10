<!DOCTYPE html>
<html>
<body>
<a href="/">menu</a>
<h1>Account Details</h1>

<p>This is account {{account_details}}</p>

<h1>Change account name</h1>

<form method = "POST" action="/account_details">
Account Name : <input type="text" name="new_account_name" value = {{account_details}}><br>
<input type="submit" value="Submit">

</form>


</body>
</html>

