from flask import Flask, request, render_template_string, redirect
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='contactuser',
        password='contactpass',
        database='contactdb'
    )

@app.route('/', methods=['GET'])
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM contacts ORDER BY id DESC')
    contacts = cursor.fetchall()
    cursor.close()
    conn.close()

    html = '''
    <h1>Contact Manager</h1>
    <form action="/add" method="post">
      Name: <input type="text" name="name" required><br><br>
      Email: <input type="email" name="email" required><br><br>
      Phone: <input type="text" name="phone" required><br><br>
      <input type="submit" value="Add Contact">
    </form>
    <h2>Contacts</h2>
    <ul>
    {% for contact in contacts %}
      <li>{{ contact.name }} | {{ contact.email }} | {{ contact.phone }}</li>
    {% endfor %}
    </ul>
    '''
    return render_template_string(html, contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contacts (name, email, phone) VALUES (%s, %s, %s)', (name, email, phone))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
