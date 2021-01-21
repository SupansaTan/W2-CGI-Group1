#!/usr/bin/python3 
print("Content-Type: text/html")    
print()                             
print("<html>")
print("<!doctype html>")
print("""
<head>
  <title>Test</title>
</head>
<body>
  <form name="pyform" method="POST" action="/cgi-bin/plus.py">
  Num1:&emsp;<input type="number" name="fnum"/><br/><br/>
    <input type="submit" name="submit" value="Submit"/><br/>
  </form>
</body>
""")
import cgi,cgitb
cgitb.enable() #for debugging

form = cgi.FieldStorage()
num= form.getvalue('fnum')
fac = 1
 
for i in range(1, int(num) + 1):
	fac = fac * i
print("<h1>Answer is %s</h1>"%(fac)) 
print("</html>")