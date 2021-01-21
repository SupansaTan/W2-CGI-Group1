#!/usr/bin/python3 
import cgi,cgitb
from os import ttyname
import time
cgitb.enable()
body = ""

def generate_form():
    form_body = \
        """
        <title>Factorial</title>
        <body>
          <form name="pyform" method="POST" action="/cgi-bin/factorial.py">
            Number :&emsp;<input type="number" name="fnum"><br><br>
            <input type="submit" name="submit" value="Submit"><br>
          </form>
        """
    return form_body
total = 1

def factorial():
  global t
  global total
  global num
  start = time.time()
  for i in range(1,(int(num)+1)):
	  total = total * i
  end =  time.time()
  t = end-start
  sec(t)
def sec(t):
  global total
  global num
  if t <= 10:
    ans = total
    return ans
  else:
    num = int(num) - 1000
    total=1 
    factorial()
    return num

if __name__ == "__main__":
  print("Content-Type: text/html")
  print("<html>")
  print()
  body += generate_form()
  form = cgi.FieldStorage()
  num = form.getvalue('fnum')
  if num != None:
    g = factorial()
    answer = sec(t)
    # add result to body html
    body += """<h3>Total : {0} </h3>
            <h3>Total time spend : {1} sec </h3>
            <h3>number factorial : {2}  </h3>
            """.format(answer ,t, num)
  print(body)
