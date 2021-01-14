#!/usr/bin/python3 
print("Content-Type: text/html")    
print()                             

import cgi,cgitb
import time
cgitb.enable() #for debugging

form = cgi.FieldStorage()
temp_input = form.getvalue('temp')
ttime = time.ctime()
f = open("temp.txt", "a")
f.write("<style>")
f.write("table, th, td {")
f.write("border: 1px solid black;")
f.write("border-collapse: collapse;}")
f.write("</style>")
f.write("<table>")
f.write("<tr>")
f.write("<td>" +temp_input +"</td>")
f.write("<td>" +ttime+"</td>")
f.write("</tr>")
f.write("</table>")
f.close()

#open and read the file after the appending:
f = open("temp.txt", "r")
print("<p>", f.read() ,"</p>")