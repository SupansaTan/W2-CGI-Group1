#!/usr/bin/python3 
print("Content-Type: text/html")    
print()                             
 
import cgi,cgitb
cgitb.enable() #for debugging

form = cgi.FieldStorage()
temp_input = form.getvalue('temp')

f = open("temp.txt", "a")
f.write("<br>" + temp_input)
f.close()

#open and read the file after the appending:
f = open("temp.txt", "r")
print("<p>", f.read() ,"</p>")