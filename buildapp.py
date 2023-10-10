import os
import subprocess

# Define the directory structure
app_structure = {
    'my_flask_app': {
        'app': {
            '__init__.py': '',
            'routes': {
                '__init__.py': '',
                'crew_member_routes.py': '',
                'task_routes.py': '',
                'meeting_routes.py': '',
            }
        },
        'run.py': ''
    }
}

def create_directory_structure(root, structure):
    for item, value in structure.items():
        if isinstance(value, dict):
            os.makedirs(os.path.join(root, item), exist_ok=True)
            create_directory_structure(os.path.join(root, item), value)
        elif isinstance(value, str):
            with open(os.path.join(root, item), 'w') as f:
                f.write(value)

def install_flake8():
    subprocess.run(["pip3", "install", "flake8"])
    subprocess.run(["flake8", "--install-hook", "git"])

if __name__ == "__main__":
    root_dir = os.getcwd()
    create_directory_structure(root_dir, app_structure)
    install_flake8()
    print("Flask application directory structure created.")

