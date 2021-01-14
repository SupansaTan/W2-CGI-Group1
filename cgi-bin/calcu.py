#!/usr/bin/python3 
print("Content-Type: text/html")    
print()                             
 
import cgi,cgitb
cgitb.enable() #for debugging

form = cgi.FieldStorage()
num1 = form.getvalue('fnum')
num2 = form.getvalue('snum')
opr = form.getvalue('oprnum')

if opr == "+":
    total = int(num1)+int(num2)
elif opr == "-":
    total = int(num1)-int(num2)
elif opr == "*":
    total = int(num1)*int(num2)
elif opr == "/":
    total = int(num1)/int(num2)

f = open("total.txt", "w+")
f.write("num1 : " + num1 + "<br>")
f.write("operator : " + opr + "<br>")
f.write("num2 : " + num2 + "<br>")
f.write("total : " + str(total))
f.close()

#open and read the file after the appending:
f = open("total.txt", "r")
print("<h1>", f.read() ,"</h1>")