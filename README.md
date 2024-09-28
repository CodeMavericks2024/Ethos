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
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
