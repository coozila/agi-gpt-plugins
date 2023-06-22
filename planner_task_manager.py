import json
import os

current_working_directory = os.getcwd()
workdir = os.path.join(
    current_working_directory, "alpha", "alpha_workspace", "tasks.json"
)
file_name = workdir

def create_task(task_id=None, task_description: str = None, status=False):
    task = {"id": task_id, "description": task_description, "completed": status}
    tasks = load_tasks()
    tasks[str(task_id)] = task

    save_tasks(tasks)

    return tasks


def load_tasks() -> dict:
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            f.write("{}")

    with open(file_name) as f:
        try:
            tasks = json.load(f)
            if isinstance(tasks, list):
                tasks = {}
        except json.JSONDecodeError:
            tasks = {}

    return tasks


def save_tasks(tasks: dict):
    with open(file_name, "w") as f:
        json.dump(tasks, f)


def update_task_status(task_id):
    tasks = load_tasks()

    if str(task_id) not in tasks:
        return f"Task with ID {task_id} not found."

    tasks[str(task_id)]["completed"] = True

    save_tasks(tasks)

    return f"Task with ID {task_id} has been marked as completed."


def assign_priority(task_id, priority):
    tasks = load_tasks()

    if str(task_id) not in tasks:
        return f"Task with ID {task_id} not found."

    tasks[str(task_id)]["priority"] = priority

    save_tasks(tasks)

    return f"Priority {priority} assigned to task with ID {task_id}."


def sort_tasks_by_priority():
    tasks = load_tasks()

    sorted_tasks = sorted(
        tasks.values(),
        key=lambda task: task.get("priority", 0),
        reverse=True
    )

    return sorted_tasks


def display_tasks_by_priority():
    sorted_tasks = sort_tasks_by_priority()

    if not sorted_tasks:
        return "No tasks found."

    output = "Tasks sorted by priority:\n"

    for task in sorted_tasks:
        task_id = task.get("id")
        description = task.get("description")
        priority = task.get("priority", 0)
        output += f"Task ID: {task_id}, Priority: {priority}, Description: {description}\n"

    return output
