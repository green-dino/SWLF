from flask import Blueprint, render_template, request, redirect, url_for
from .models import CrewMember
from .models import log_meeting_hours


meeting_bp = Blueprint('meeting', __name__)

@meeting_bp.route('/log_meeting_hours', methods=['POST'])
def log_meeting_hours_route():
    crew_members = CrewMember.query.all()
    start_time = request.form['start_time']
    stop_time = request.form['stop_time']
    log_meeting_hours(crew_members, start_time, stop_time)
    return redirect(url_for('meeting.meeting_logs'))

@meeting_bp.route('/meeting_logs')
def meeting_logs():
    # Retrieve meeting logs and display them
    return render_template('meeting_logs.html', crew_members=crew_members)

# Add more routes for meetings
