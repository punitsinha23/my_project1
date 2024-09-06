from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3
from form import RegistrationForm, loginForm

app = Flask(__name__)
app.secret_key = 'abcd' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


JOBS = [
    {'id': 1, 'title': 'Data Analyst', 'location': 'Bengaluru, India', 'salary': 'Rs. 10,00,000'},
    {'id': 2, 'title': 'Data Scientist', 'location': 'Delhi, India', 'salary': 'Rs. 15,00,000'},
    {'id': 3, 'title': 'Frontend Engineer', 'location': 'Remote', 'salary': 'Rs. 12,00,000'},
    {'id': 4, 'title': 'Backend Engineer', 'location': 'San Francisco, USA', 'salary': '$120,000'},
    {'id': 5, 'title': 'Machine Learning Engineer', 'location': 'Bengaluru, India', 'salary': 'Rs. 18,00,000'},
    {'id': 6, 'title': 'Product Manager', 'location': 'New York, USA', 'salary': '$130,000'},
    {'id': 7, 'title': 'UX/UI Designer', 'location': 'Berlin, Germany', 'salary': '€70,000'},
    {'id': 8, 'title': 'DevOps Engineer', 'location': 'Remote', 'salary': 'Rs. 14,00,000'},
    {'id': 9, 'title': 'Full Stack Developer', 'location': 'Toronto, Canada', 'salary': 'CAD 90,000'},
    {'id': 10, 'title': 'Cybersecurity Analyst', 'location': 'Sydney, Australia', 'salary': 'AUD 100,000'},
    {'id': 11, 'title': 'AI Researcher', 'location': 'London, UK', 'salary': '£85,000'},
    {'id': 12, 'title': 'Systems Architect', 'location': 'Bengaluru, India', 'salary': 'Rs. 20,00,000'},
    {'id': 13, 'title': 'Cloud Engineer', 'location': 'San Francisco, USA', 'salary': '$140,000'},
    {'id': 14, 'title': 'Network Administrator', 'location': 'Tokyo, Japan', 'salary': '¥8,000,000'},
    {'id': 15, 'title': 'Mobile App Developer', 'location': 'Remote', 'salary': 'Rs. 13,00,000'},
    {'id': 16, 'title': 'Business Analyst', 'location': 'Mumbai, India', 'salary': 'Rs. 9,00,000'},
    {'id': 17, 'title': 'Data Engineer', 'location': 'Seattle, USA', 'salary': '$115,000'},
    {'id': 18, 'title': 'IT Support Specialist', 'location': 'Dublin, Ireland', 'salary': '€60,000'},
    {'id': 19, 'title': 'Technical Writer', 'location': 'Remote', 'salary': 'Rs. 8,00,000'},
    {'id': 20, 'title': 'Quality Assurance Engineer', 'location': 'Singapore', 'salary': 'SGD 85,000'}
]

# Initialize the database and create the users table if it doesn't exist
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Route for the signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        try:
            cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', 
                           (username, email, password))
            conn.commit()
            flash('Signup successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username or email already exists!', 'danger')
            return redirect(url_for('signup'))
        finally:
            conn.close()

    return render_template('signup.html')

@app.route('/register' , methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)
    
# Route for the login page (stub for demonstration)
@app.route('/login')
def login():
    form = loginForm()
    return render_template('login.html', title='login', form=form)

# Route for the homepage
@app.route("/")
def home():
    return render_template("home.html", jobs=JOBS)

# API route to list jobs as JSON
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

# Route for the about page
@app.route('/about')
def about():
    return render_template("about.html")

# Initialize the database and run the app
if __name__ == "__main__":
    init_db()  # Initialize the database
    app.run(host='0.0.0.0', debug=True)
