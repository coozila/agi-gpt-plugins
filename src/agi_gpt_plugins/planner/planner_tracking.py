import json
import os
from planner_memory import load_memory, save_memory

def create_task(task_id=None, title=None, description=None, steps=None, quality_parameters=None, progress=None, testing_status=None, due_date=None):
    task = {
        "title": title,
        "description": description,
        "steps": steps,
        "quality_parameters": quality_parameters,
        "progress": progress,
        "testing_status": testing_status,
        "due_date": due_date
    }

    tasks = load_memory()
    tasks[str(task_id)] = task

    save_memory(tasks)

    return tasks

def load_tasks() -> dict:
    tasks = load_memory()
    return tasks

def save_memory(tasks):
    # Save the tasks to memory (JSON)
    current_working_directory = os.getcwd()
    workdir = os.path.join(current_working_directory, "agi-gpt", "agi-gpt_workspace", "tasks.json")
    file_name = workdir

    with open(file_name, "w") as f:
        json.dump(tasks, f)
