# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('ec1.html')

@app.route('/image')
def image():
    return render_template('ec2.html')

@app.route('/register')
def register():
    return render_template('ec3.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
