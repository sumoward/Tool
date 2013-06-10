<!doctype HTML>
<html>
<head>
<title></title>

</head>


The %include statement loads the subtemplate at compile time, so there
is no way to pass a dynamic name. But you can just use the
bottle.template() function to do the same with dynamic template names.

This should work:

from bottle import template
tpl = '''
% t = '/'.join(['home','bla','bla2'])
{{template(t)}}
'''
print template(tpl, template=template)





<body>
<br>
<h3>section</h3> 

<br/>
<br/>
</body>
</html>