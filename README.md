# Flask Cross-Platform Chat Application

This is a cross-platform chat application built using Flask for the backend and PostgreSQL for the database. The app allows users to register using their email and chat with others who are already registered. The application supports deployment with Gunicorn and Nginx, including HTTPS for secure communication.

## Project Structure

The project structure is as follows:

- **app/**: Contains the main application code, including routes, models, and views for the chat functionalities.
- **static/**: Contains static files like CSS, JavaScript, and images for styling and frontend interactivity.
- **templates/**: Contains the HTML files that are rendered as web pages using Flask's `render_template()` method.
- **config.py**: This file contains the configuration settings for the Flask application (e.g., database settings, secret keys).
- **gunicorn_config.py**: This file holds the configuration for Gunicorn, the WSGI HTTP server used to run the app.
- **nginx_config**: The Nginx configuration file, which sets up Nginx as a reverse proxy to serve the app and handle HTTPS requests.
- **Procfile**: This file is used for deployment on platforms like Heroku to specify the commands that should be run to start the app.
- **requirements.txt**: Contains a list of all the Python libraries and dependencies required for the app to function.
- **run.py**: The main entry point of the Flask application, used to run the app locally for testing and development.

## Prerequisites

Before setting up this project, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- PostgreSQL (for database management)
- Gunicorn (for running the app in production)
- Nginx (for reverse proxy and serving HTTPS)

## Installation

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/CodeMavericks2024/Ethos.git

2. Install Dependencies

Install the Python dependencies listed in requirements.txt:

bash

pip install -r requirements.txt

3. Set Up Environment Variables

Edit the config.py file and provide your configuration settings, such as database connection, secret keys, etc.
4. Database Setup

Assuming you're using PostgreSQL, initialize and migrate the database using Flask-Migrate:

bash

flask db init
flask db migrate
flask db upgrade

5. Running the Application Locally

To run the Flask application locally, use the following command:

bash

python run.py

The application will start running on http://127.0.0.1:5000 by default.
Deployment

This app is designed to be deployed using Gunicorn with Nginx as a reverse proxy.
1. Set Up Gunicorn

Configure Gunicorn by running:

bash

gunicorn -c gunicorn_config.py app:app

This will start the Flask app using Gunicorn.
2. Configure Nginx

Configure Nginx by using the provided nginx_config file. This will allow Nginx to act as a reverse proxy for your Gunicorn server, handling HTTPS requests.

Example Nginx configuration:

nginx

server {
    listen 80;
    server_name yourdomain.com;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Redirect all HTTP requests to HTTPS
    listen 443 ssl;
    ssl_certificate /etc/nginx/ssl/yourdomain.com.crt;
    ssl_certificate_key /etc/nginx/ssl/yourdomain.com.key;
}

3. Enabling HTTPS

To enable HTTPS, obtain an SSL certificate (e.g., using Let's Encrypt) and modify the nginx_config file accordingly. This ensures secure communication between the client and server.
4. Final Steps for Deployment

Once Nginx and Gunicorn are configured, restart the services to apply changes:

bash

sudo systemctl restart nginx


**It's Not fully functional but have done backend part. We have done some frontend part but havent integrated with backend If we get chance then we 
can deploy fully function system.
