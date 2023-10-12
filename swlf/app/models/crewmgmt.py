import datetime

class CrewMember:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.meeting_logs = []

    def get_info(self):
        return f"Name: {self.name}, Email: {self.email}"

    def log_meeting_hours(self, start_time, stop_time):
        if self.name not in [log['member_name'] for log in self.meeting_logs]:
            self.meeting_logs.append({'member_name': self.name, 'meetings': []})
        self.meeting_logs = [{'member_name': log['member_name'], 'meetings': [(start_time, stop_time)] if log['member_name'] == self.name else log['meetings']} for log in self.meeting_logs]

    def get_meeting_logs(self):
        return self.meeting_logs

class ProjectLead(CrewMember):
    def __init__(self, name, email, project_name):
        super().__init__(name, email)
        self.project_name = project_name

    def get_info(self):
        return f"Name: {self.name}, Email: {self.email}, Project Lead for: {self.project_name}"

class ProjectAssistant(CrewMember):
    def __init__(self, name, email, project_name):
        super().__init__(name, email)
        self.project_name = project_name

    def get_info(self):
        return f"Name: {self.name}, Email: {self.email}, Project Assistant for: {self.project_name}"

class Task:
    def __init__(self, task_description):
        self.task_description = task_description
        self.ProjectLead = None
        self.ProjectAssistant = None
        self.current_status = "Not Started"
        self.due_date = datetime
        self.date_completed = datetime
        self.estimated_time = None
        self.actual_time = None

    def mark_as_started(self):
        self.current_status = "In Progress"

    def mark_as_completed(self, date_completed, actual_time):
        self.current_status = "Done"
        self.date_completed = date_completed
        self.actual_time = actual_time

    def update_due_date(self, due_date):
        self.due_date = due_date

    def update_estimated_time(self, estimated_time):
        self.estimated_time = estimated_time

    def assign_person(self, crew_member):
        if isinstance(crew_member, (ProjectLead, ProjectAssistant)):
            if isinstance(crew_member, ProjectLead):
                self.ProjectLead = crew_member
            else:
                self.ProjectAssistant = crew_member
        else:
            print("Only Project Leads & Assistants can be assigned to tasks.")

    def get_task_info(self):
        return f"Task Description: {self.task_description}\n" \
               f"Project Lead: {self.ProjectLead.get_info() if self.ProjectLead else 'None'}\n" \
               f"Project Assistant: {self.ProjectAssistant.get_info() if self.ProjectAssistant else 'None'}\n" \
               f"Current Status: {self.current_status}\n" \
               f"Due Date: {self.due_date}\n" \
               f"Date Completed: {self.date_completed}\n" \
               f"Estimated Time: {self.estimated_time}\n" \
               f"Actual Time: {self.actual_time}\n"

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_task_by_description(self, description):
        for task in self.tasks:
            if task.task_description == description:
                return task
        return None

def log_meeting_hours(meeting_attendees, start_time, stop_time):
    for member in meeting_attendees:
        member.log_meeting_hours(start_time, stop_time)

# Example usage:

crew_member = CrewMember("John Doe", "john@example.com")
project_lead = ProjectLead("Alice Smith", "alice@example.com", "Project A")
project_assistant = ProjectAssistant("Bob Johnson", "bob@example.com", "Project B")

# Assign crew members to a task
task1 = Task("Write a report")
task1.assign_person(project_lead)
task1.assign_person(project_assistant)
task1.update_due_date("2023-12-31")
task1.update_estimated_time(4)
task1.mark_as_started()

# Create a list of crew members present in the meeting
meeting_attendees = [crew_member, project_lead, project_assistant]

# Log meeting hours for each attendee
meeting_start_time = datetime.datetime(2023, 10, 15, 9, 0)
meeting_stop_time = datetime.datetime(2023, 10, 15, 11, 30)
log_meeting_hours(meeting_attendees, meeting_start_time, meeting_stop_time)

# Print meeting logs for each crew member
for member in meeting_attendees:
    print(f"Meeting logs for {member.name}:")
    logs = member.get_meeting_logs()
    for log in logs:
        for meeting_start, meeting_stop in log['meetings']:
            print(f"Start Time: {meeting_start}, Stop Time: {meeting_stop}")
import datetime

class CrewManagementSystem:
    def __init__(self):
        self.crew_members = {}
        self.task_list = TaskList()
        self.project_lead = None
        self.project_assistant = None

    def run(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice (1-10): ")
            if choice == '1':
                self.create_person("Crew Member")
            elif choice == '2':
                self.create_person("Project Lead")
            elif choice == '3':
                self.create_person("Project Assistant")
            elif choice == '4':
                self.create_task()
            elif choice == '5':
                self.assign_person_to_task()
            elif choice == '6':
                self.start_task()
            elif choice == '7':
                self.mark_task_as_completed()
            elif choice == '8':
                self.log_meeting_hours()
            elif choice == '9':
                self.view_meeting_logs()
            elif choice == '10':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 10.")

    def create_person(self, person_type):
        name = input(f"Enter {person_type}'s name: ")
        email = input(f"Enter {person_type}'s email: ")
        if person_type == "Crew Member":
            self.crew_members[name] = CrewMember(name, email)
        elif person_type == "Project Lead":
            project_name = input(f"Enter {person_type}'s project name: ")
            self.project_lead = ProjectLead(name, email, project_name)
        else:
            project_name = input(f"Enter {person_type}'s project name: ")
            self.project_assistant = ProjectAssistant(name, email, project_name)
        print(f"{person_type} created successfully!")

    def create_task(self):
        description = input("Enter Task Description: ")
        task = Task(description)
        self.task_list.add_task(task)
        print("Task created successfully!")

    def assign_person_to_task(self):
        description = input("Enter Task Description: ")
        task = self.task_list.get_task_by_description(description)
        if task:
            person_name = input("Enter the person's name (Crew Member, Project Lead, or Project Assistant): ")
            if person_name in self.crew_members:
                task.assign_person(self.crew_members[person_name])
            elif person_name == "Project Lead":
                task.assign_person(self.project_lead)
            elif person_name == "Project Assistant":
                task.assign_person(self.project_assistant)
            else:
                print("Invalid input. Please enter a valid person's name.")
        else:
            print("Task not found.")

    def start_task(self):
        description = input("Enter Task Description: ")
        task = self.task_list.get_task_by_description(description)
        if task:
            task.mark_as_started()
            print("Task marked as In Progress.")
        else:
            print("Task not found.")

    def mark_task_as_completed(self):
        description = input("Enter Task Description: ")
        task = self.task_list.get_task_by_description(description)
        if task:
            date_completed = input("Enter Date Completed (YYYY-MM-DD): ")
            actual_time = input("Enter Actual Time (hours): ")
            task.mark_as_completed(date_completed, actual_time)
            print("Task marked as Completed.")
        else:
            print("Task not found.")

    def log_meeting_hours(self):
        start_time = input("Enter Meeting Start Time (YYYY-MM-DD HH:MM): ")
        stop_time = input("Enter Meeting Stop Time (YYYY-MM-DD HH:MM): ")
        meeting_start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M")
        meeting_stop_time = datetime.datetime.strptime(stop_time, "%Y-%m-%d %H:%M")
        members = [self.project_lead, self.project_assistant] + list(self.crew_members.values())
        log_meeting_hours(members, meeting_start_time, meeting_stop_time)
        print("Meeting hours logged successfully!")

    def view_meeting_logs(self):
        for person in [self.project_lead, self.project_assistant] + list(self.crew_members.values()):
            print(f"Meeting logs for {person.name}:")
            logs = person.get_meeting_logs()
            for log in logs:
                for meeting_start, meeting_stop in log['meetings']:
                    print(f"Start Time: {meeting_start}, Stop Time: {meeting_stop}")

    def print_menu(self):
        print("\nMain Menu:")
        print("1. Create Crew Member")
        print("2. Create Project Lead")
        print("3. Create Project Assistant")
        print("4. Create Task")
        print("5. Assign Person to Task")
        print("6. Start Task")
        print("7. Mark Task as Completed")
        print("8. Log Meeting Hours")
        print("9. View Meeting Logs")
        print("10. Exit")

if __name__ == "__main__":
    system = CrewManagementSystem()
    system.run()
