from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

# Import and register blueprints
from .routes import crew_member_bp, task_bp, meeting_bp
app.register_blueprint(crew_member_bp)
app.register_blueprint(task_bp)
app.register_blueprint(meeting_bp)

# Add more app configurations as needed
