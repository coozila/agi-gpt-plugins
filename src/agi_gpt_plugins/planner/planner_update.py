import json
import os
from planner_task_manager import task_manager
from planner_memory import load_memory, save_memory

def update_task_status(task_id, progress=None, testing_status=None, due_date=None):
    tasks = load_memory()

    if str(task_id) not in tasks:
        return f"Task with ID {task_id} not found."

    task = tasks[str(task_id)]

    if progress is not None:
        task["progress"] = progress

    if testing_status is not None:
        task["testing_status"] = testing_status

    if due_date is not None:
        task["due_date"] = due_date

    save_memory(tasks)

    return f"Task with ID {task_id} has been updated."

def save_memory(tasks):
    # Save the tasks to memory (JSON)
    current_working_directory = os.getcwd()
    workdir = os.path.join(current_working_directory, "agi-gpt", "agi-gpt_workspace", "tasks.json")
    file_name = workdir

    with open(file_name, "w") as f:
        json.dump(tasks, f)
