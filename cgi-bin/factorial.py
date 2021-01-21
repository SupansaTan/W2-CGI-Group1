#!/usr/bin/python3 

import cgi,cgitb
from datetime import *
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

def factorial(n):
  total = 1
  for i in range(1,(int(n)+1)):
	  total = total * i
  return total

if __name__ == "__main__":
  form = cgi.FieldStorage()
  num = form.getvalue('fnum')

  print("Content-Type: text/html")
  print("<html>")
  print()
  body += generate_form()

  if num != None:
    start = datetime.now()
    total = factorial(num)
    end = datetime.now()

    # add result to body html
    body += """<h3>Total : {0} </h3>
            <h3>Total time spend : {1} sec </h3>
            """.format(total ,(end-start).total_seconds())

  print(body)