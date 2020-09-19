# python server.py

# ROUTE:
#  cd C:\Users\guillermo.alcazar\Dropbox\Python\Server

# ACTIVATE ENV:
# Set-ExecutionPolicy -ExecutionPolicy unrestricted -Scope CurrentUser
# Server\Scripts\activate

# ACTIVATE SERV
#  DEBUG OF
#     $env:FLASK_APP = "server.py"
#  DEBUG ON
#     $env:FLASK_ENV = "development"
#  flask run

import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('./index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(f'{page_name}.html')


def write_to_file(data):
    with open('C:/Users/guillermo.alcazar/Dropbox/Python/Server/database.txt', mode='a') as database:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        file = database.write(f'\n {name}, {email}, {message}')


def write_to_csv(data):
    with open('C:/Users/guillermo.alcazar/Dropbox/Python/Server/database.csv', newline='', mode='a') as database2:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(
            database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_file(data)
        write_to_csv(data)
        return redirect('/thank_you')
    else:
        return'something went wrong'
