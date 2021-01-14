#!/usr/bin/python3 
print("Content-Type: text/html") 
print()                              
 
import cgi,cgitb
cgitb.enable()

form = cgi.FieldStorage()
name = form.getvalue('fname')
print("<h1>Hello, %s</h1>" % (name))