import json
import os


def generate_report():
    """Generate a report based on the tasks and events"""

    tasks = load_tasks()
    events = load_events()

    report = f"Tasks:\n\n"
    for task_id, task in tasks.items():
        status = "Completed" if task["completed"] else "Pending"
        report += f"Task ID: {task_id}\n"
        report += f"Description: {task['description']}\n"
        report += f"Status: {status}\n\n"

    report += f"Events:\n\n"
    for event_id, event in events.items():
        report += f"Event ID: {event_id}\n"
        report += f"Title: {event['title']}\n"
        report += f"Start Time: {event['start_time']}\n"
        report += f"End Time: {event['end_time']}\n\n"

    return report


def load_tasks() -> dict:
    """Load tasks from JSON"""

    current_working_directory = os.getcwd()
    tasks_file_path = os.path.join(
        current_working_directory, "agi-gpt", "agi-gpt_workspace", "tasks.json"
    )

    if not os.path.exists(tasks_file_path):
        with open(tasks_file_path, "w") as f:
            f.write("{}")

    with open(tasks_file_path) as f:
        try:
            tasks = json.load(f)
            if isinstance(tasks, list):
                tasks = {}
        except json.JSONDecodeError:
            tasks = {}

    return tasks


def load_events() -> dict:
    """Load events from JSON"""

    current_working_directory = os.getcwd()
    events_file_path = os.path.join(
        current_working_directory, "agi-gpt", "agi-gpt_workspace", "events.json"
    )

    if not os.path.exists(events_file_path):
        with open(events_file_path, "w") as f:
            f.write("{}")

    with open(events_file_path) as f:
        try:
            events = json.load(f)
            if isinstance(events, list):
                events = {}
        except json.JSONDecodeError:
            events = {}

    return events
