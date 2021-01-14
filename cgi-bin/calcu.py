#!/usr/bin/python3 
print("Content-Type: text/html")    
print()                             
 
import cgi,cgitb
cgitb.enable() #for debugging

form = cgi.FieldStorage()
num1= form.getvalue('fnum')
num2= form.getvalue('snum')
opr=form.getvalue('oprnum')
if opr=="+":
    num3=int(num1)+int(num2)
elif opr=="-":
    num3=int(num1)-int(num2)
elif opr=="*":
    num3=int(num1)*int(num2)
elif opr=="/":
    num3=int(num1)/int(num2)

print("<h1>This is First Number %s</h1>" % (num1))
print("<h1>This is Second Number %s</h1>" % (num2))
print("<h1>Answer is %s</h1>"%(num3)) 
