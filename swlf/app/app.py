from flask import Flask, render_template, request, redirect, url_for
from models.swlf import CrewMember


app = Flask(__name__)

crew_members = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_crew_member', methods=['POST'])
def add_crew_member():
    name = request.form.get('name')
    email = request.form.get('email')
    crew_member = CrewMember(name, email)
    crew_members.append(crew_member)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
