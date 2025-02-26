from flask import Flask, render_template, request, redirect, session, url_for
from odeta import database

db = database('my_database.db')
table = db('my_table')

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'satish' and password == '1234':
            session['username'] = username
            return redirect(url_for('home'))
        else:
            error = 'Invalid User name or Password.'
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/add', methods=["GET", "POST"])
def add():
    if 'username' in session:
        if request.method == 'POST':
            new_entry = {
                "receiver_name": request.form.get('receiver_name'),
                "amount": request.form.get('amount'),
                "date": request.form.get('date')
            }
            response = table.put(new_entry)
            print(response)  # Debugging statement
            return redirect(url_for('add'))  # Redirect to /add to display updated data
        data_all = table.fetchall()  # Retrieve all data from the table
        print(data_all)  # Debugging statement
        return render_template('add.html', data=data_all)  # Pass data to the template
    return redirect(url_for('login'))

@app.route('/content')
def content():
    if 'username' in session:
        return render_template('content.html')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
