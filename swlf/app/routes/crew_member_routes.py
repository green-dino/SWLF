from flask import Blueprint, render_template, request, redirect, url_for
from .models import CrewMember

crew_member_bp = Blueprint('crew_member', __name__)

@crew_member_bp.route('/crew_members')
def list_crew_members():
    crew_members = CrewMember.query.all()
    return render_template('crew_members.html', crew_members=crew_members)

# Add more routes for crew members
