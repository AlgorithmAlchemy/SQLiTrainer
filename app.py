from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  # Убедитесь, что шаблон называется home.html


@app.route('/login')
def login():
    return render_template('login.html')  # Путь к странице логина


if __name__ == '__main__':
    app.run(debug=True)

