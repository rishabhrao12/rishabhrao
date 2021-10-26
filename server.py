from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_database_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save database'
    else:
        return 'something went wrong'


def write_to_database_file(data):
    with open('filedatabase.txt', mode='a') as file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file.write(f"\n{email},{subject},{message}")


def write_to_database_csv(data):
    with open('csvdatabase.csv', newline='', mode='a') as file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(file, delimiter=',', lineterminator='\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
