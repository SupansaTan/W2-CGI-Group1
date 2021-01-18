#!/usr/bin/python3 

import cgi,cgitb
from datetime import *
cgitb.enable()
body = ""

def generate_form():
    form_body = \
        """
        <link rel="stylesheet" href="/css/temp.css">
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
        <title>Temperature</title>
        <body>
        <div class="form-container">
            <h2>What is the temperature now ?</h2>
            <form name="pyform" method="POST" action="/cgi-bin/temp.py">
                <input type="number" step="0.01" name="temp">
                <input type="radio" name="test" value="1">
                <label for="mintomax">Min to Max</label>
                <input type="radio" name="test" value="2">
                <label for="maxtomin">Max to Min</label>
                <input type="submit" id="submit_btn" name="submit" value="Submit">
            </form>
        </div>
        """
    return form_body

def write_file(temp):
    now = datetime.now()
    date_now = now.strftime("%d/%m/%Y")
    time_now = now.strftime("%H:%M:%S")

    f = open("temp.txt", "a+")
    f.write(date_now + "," + time_now + "," + str(temp) + "\n")
    f.close()

def read_file1():
    f = open("temp.txt", "r")
    read = f.readlines()
    
    # part of head table (topics)
    table_body = \
        """
        <div class="table-container">
            <table id="temp-table">
                <tr>
                    <th class="column1">Date</th>
                    <th class="column2">Time</th>
                    <th class="column3">Temperature</th>
                </tr>
        """

    # sort temp
    temp_logs = []
    f = open("temp.txt", "r")
    read = f.readlines()
    for i in range(len(read)):
        split_values = read[i].split(",")
        date = split_values[0]
        time = split_values[1]
        temp = split_values[2]
        temp_obj = {"date":date, "time":time, "temp":float(temp)}
        temp_logs.append(temp_obj)
    
        temp_sort = sorted(temp_logs, key=lambda x:x["temp"], reverse=True)

    #display 
    for obj in temp_sort:

        table_body += \
            """ <tr>
                    <td class="column1">{0}</td>
                    <td class="column2">{1}</td>
                    <td class="column3">{2}</td>
                </tr>
            """.format(obj["date"], obj["time"], obj["temp"])

    return table_body

def read_file2():
    f = open("temp.txt", "r")
    read = f.readlines()
    
    # part of head table (topics)
    table_body = \
        """
        <div class="table-container">
            <table id="temp-table">
                <tr>
                    <th class="column1">Date</th>
                    <th class="column2">Time</th>
                    <th class="column3">Temperature</th>
                </tr>
        """

    # sort temp
    temp_logs = []
    f = open("temp.txt", "r")
    read = f.readlines()
    for i in range(len(read)):
        split_values = read[i].split(",")
        date = split_values[0]
        time = split_values[1]
        temp = split_values[2]
        temp_obj = {"date":date, "time":time, "temp":float(temp)}
        temp_logs.append(temp_obj)
    
        temp_sort = sorted(temp_logs, key=lambda x:x["temp"], reverse=False)

    #display 
    for obj in temp_sort:

        table_body += \
            """ <tr>
                    <td class="column1">{0}</td>
                    <td class="column2">{1}</td>
                    <td class="column3">{2}</td>
                </tr>
            """.format(obj["date"], obj["time"], obj["temp"])

    return table_body

# run the first time
if __name__ == "__main__":
    
    form = cgi.FieldStorage()
    temp_input = form.getvalue('temp')
    test=form.getvalue('test')
    if temp_input != None:
        write_file(temp_input)

    print("Content-Type: text/html")
    print("<html>")
    print()
    body += generate_form()
    if test=="1":
        body += read_file2()
            
    else:
        body += read_file1()
        
            
    print(body)