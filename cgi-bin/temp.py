#!/usr/bin/python3 
print("Content-Type: text/html")
print("<html>")
print()

import cgi,cgitb
from datetime import *
cgitb.enable()
body = ""
                        
# get value : form
form = cgi.FieldStorage()
temp_input = form.getvalue('temp')

# date & time
now = datetime.now()
date_now = now.strftime("%d/%m/%Y")
time_now = now.strftime("%H:%M:%S")


# write file
f = open("temp.txt", "a+")
f.write(date_now + "," + time_now + "," + str(temp_input) + "\n")
f.close()

# open and read the file after the appending:
f = open("temp.txt", "r")
read_file = f.readlines()
 
body += """
        <link rel="stylesheet" href="/temp.css">
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
        <title>Temperature</title>
        <body>
        <div class="table-container">
            <table id="temp-table">
                <tr>
                    <th class="column1">Date</th>
                    <th class="column2">Time</th>
                    <th class="column3">Temperature</th>
                </tr>
        """

for i in range(len(read_file)):
    split_values = read_file[i].split(",")
    date = split_values[0]
    time = split_values[1]
    temp = split_values[2]

    body += """ <tr><td class="column1">{0}</td>
                <td class="column2">{1}</td>
                <td class="column3">{2}</td>
                </tr>
            """.format(date, time, temp)
     
print(body) 
print("</table></div></body></html>")