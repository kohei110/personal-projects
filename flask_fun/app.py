from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    detail = db.Column(db.String(300), nullable=False)
    due = db.Column(db.DateTime, nullable=False)

@app.route('/')
def landing_page():
    return render_template('landing.html')

@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle user signup form submission
        return redirect(url_for('main_page'))
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)