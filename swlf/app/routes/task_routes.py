from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Task

task_bp = Blueprint('task', __name__)


@task_bp.route('/tasks')
def list_tasks():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

# Add more routes for tasks
