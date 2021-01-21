#!/usr/bin/python3 

import cgi,cgitb
from datetime import *
import csv
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
                <input type="radio" name="sort" value="ascending">
                <label for="mintomax">Min to Max</label>
                <input type="radio" name="sort" value="descending">
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

    with open('temp.csv', mode='a') as csv_file:
        fieldnames = ['Date', 'Time', 'Temp']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if csv_file == None:
            writer.writeheader()
            writer.writerow({'Date': date_now, 'Time':time_now , 'Temp': temp})
        else:
            writer.writerow({'Date': date_now, 'Time':time_now , 'Temp': temp})

def read_file_max_to_min():
    # part of head table
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

    # read file csv
    temp_logs = []
    with open('temp.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            temp_logs.append(row)
    
    # sort temp descending (max to min)
    temp_sort = sorted(temp_logs, key=lambda x:float(x["temp"]), reverse=True)

    # display date and temp in table
    for obj in temp_sort:

        table_body += \
            """ <tr>
                    <td class="column1">{0}</td>
                    <td class="column2">{1}</td>
                    <td class="column3">{2}</td>
                </tr>
            """.format(obj["date"], obj["time"], obj["temp"])

    return table_body

def read_file_min_to_max():
    # part of head table
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

    # read file csv
    temp_logs = []
    with open('temp.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            temp_logs.append(row)

    # sort temp ascending (min to max)
    temp_sort = sorted(temp_logs, key=lambda x:float(x["temp"]), reverse=False)

    # display date and temp in table
    for temp in temp_sort:

        table_body += \
            """ <tr>
                    <td class="column1">{0}</td>
                    <td class="column2">{1}</td>
                    <td class="column3">{2}</td>
                </tr>
            """.format(temp["date"], temp["time"], temp["temp"])

    return table_body

# run the first time
if __name__ == "__main__":
    
    form = cgi.FieldStorage()
    temp_input = form.getvalue('temp')
    sort_format = form.getvalue('sort')

    if temp_input != None:
        write_file(temp_input)

    print("Content-Type: text/html")
    print("<html>")
    print()
    body += generate_form()

    if sort_format == "ascending":
        body += read_file_min_to_max()
    else:
        body += read_file_max_to_min()

    print(body)