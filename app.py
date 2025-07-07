# app.py
from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('ec1.html', ip=get_ip())

@app.route('/image')
def image():
    return render_template('ec2.html', ip=get_ip())

@app.route('/register')
def register():
    return render_template('ec3.html', ip=get_ip())

def get_ip():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return IPAddr
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
