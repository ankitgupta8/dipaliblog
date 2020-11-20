from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')



def write_to_csv(data):
    with open("database.csv", mode="a") as db:
        email = data['email']
        name = data['name']
        phone = data['phone']
        message = data['message']
        # db.write(f"\n{email}, {subject}, {message}")
        csv_write = csv.writer(
            db, quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([name, email, phone, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('thankyou.html', post=data)
    else:
        return render_template('index.html')

    return 'Form Submitted Successfully !! '



@app.route('/<page_name>')
def page(page_name):
    return render_template(page_name)


