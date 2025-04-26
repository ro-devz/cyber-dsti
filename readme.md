# Educational Microsoft Phishing Demo

This is an educational Flask application designed to demonstrate how phishing pages work for security awareness training. This application should only be used in authorized educational contexts.

## Setup Instructions

### Local Development

1. Clone this repository:
   ```
   git clone [your-repository-url]
   cd [repository-name]
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Access the application at `http://127.0.0.1:5000/`

### Deployment to Render

1. Create a new Git repository and push this code to it.

2. Sign up for or log in to [Render](https://render.com/).

3. From the Render dashboard, click "New" and select "Web Service".

4. Connect your Git repository.

5. Configure the service:
    - Name: Choose a name for your service
    - Environment: Python
    - Build Command: `pip install -r requirements.txt`
    - Start Command: `gunicorn app:app`

6. Click "Create Web Service".

7. Render will automatically build and deploy your application.

## Educational Use Only

This application is intended strictly for educational purposes to demonstrate phishing techniques in a controlled environment. It should only be used with proper authorization and as part of security awareness training. Any other use may violate terms of service for hosting providers and potentially laws regarding unauthorized access.