import json
import os


def check_plan():
    """Check if the plan.md file exists, create it if it doesn't."""

    # Existing implementation for checking and creating the plan.md file
    # ...


def update_plan():
    """Update the plan.md file with an improved plan."""

    # Existing implementation for updating the plan.md file using generate_improved_plan
    # ...


def generate_improved_plan(prompt: str) -> str:
    """Generate an improved plan using ChatCompletion."""

    # Existing implementation for generating an improved plan using ChatCompletion
    # ...


def planner_create_task(task_id=None, task_description: str = None, status=False):
    """Create a new task in the plan."""

    task = {"description": task_description, "completed": status, "progress": 0}
    tasks = planner_load_tasks()
    tasks[str(task_id)] = task
    planner_save_tasks(tasks)

    return tasks


def planner_load_tasks() -> dict:
    """Load tasks from the tasks.json file."""

    current_working_directory = os.getcwd()
    workdir = os.path.join(
        current_working_directory, "alpha", "alpha_workspace", "tasks.json"
    )
    file_name = workdir

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


def planner_save_tasks(tasks: dict):
    """Save tasks to the tasks.json file."""

    current_working_directory = os.getcwd()
    workdir = os.path.join(
        current_working_directory, "alpha", "alpha_workspace", "tasks.json"
    )
    file_name = workdir

    with open(file_name, "w") as f:
        json.dump(tasks, f)


def planner_update_task_status(task_id, progress=None):
    """Update the status of a task, including progress percentage."""

    tasks = planner_load_tasks()

    if str(task_id) not in tasks:
        print(f"Task with ID {task_id} not found.")
        return

    task = tasks[str(task_id)]

    if progress is not None:
        task["progress"] = progress

    task["completed"] = True

    planner_save_tasks(tasks)

    return f"Task with ID {task_id} has been marked as completed."








