#!/bin/bash

# Create a new directory for your Flask app
mkdir my_flask_app
cd my_flask_app

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install Flask
pip install Flask

# Create the folder structure
mkdir app
cd app

mkdir static templates

touch __init__.py
touch routes.py

# Create a basic Flask app in __init__.py
cat <<EOL > __init__.py
from flask import Flask

app = Flask(__name__)

from app import routes
EOL

# Create a simple route in routes.py
cat <<EOL > routes.py
from app import app

@app.route('/')
def index():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run()
EOL

# Go back to the root directory
cd ..

# Create a basic configuration file
touch config.py

# Create a run.py script to run the app
cat <<EOL > run.py
from app import app

if __name__ == '__main__':
    app.run()
EOL

# Initialize the Git repository
git init

# Create a .gitignore file
cat <<EOL > .gitignore
__pycache__
*.pyc
venv/
instance/
*.pyo
*.pyd
*.db
*.log
*.sqlite
*.swp
EOL

# Install and initialize a basic database (SQLite)
pip install Flask-SQLAlchemy

# Create an instance folder for configuration
mkdir instance

# Create a config.py in the instance folder
cat <<EOL > instance/config.py
SECRET_KEY = 'your_secret_key_here'
SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
EOL

# Initialize the database
python
