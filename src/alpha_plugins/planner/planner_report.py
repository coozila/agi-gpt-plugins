import json
import os

def check_plan_status():
    """Check the status of the plan and return it as a string."""
    
    # Existing implementation to check the plan.md file and load its contents
    # ...
    
    # Generate the plan status report
    plan_status = "Plan Status:\n"
    plan_status += "----------------\n"
    # Include relevant information about the plan's status here
    # You can retrieve information from the plan.md file or any other source
    
    return plan_status


def generate_task_report(task_id):
    """Generate a report for a specific task in the plan."""
    
    tasks = planner_load_tasks()
    
    if str(task_id) not in tasks:
        return f"Task with ID {task_id} not found."
    
    task = tasks[str(task_id)]
    
    task_report = f"Task Report - ID: {task_id}\n"
    task_report += "----------------\n"
    task_report += f"Description: {task['description']}\n"
    task_report += f"Completed: {task['completed']}\n"
    task_report += f"Progress: {task['progress']}%\n"
    
    return task_report


def generate_overall_report():
    """Generate an overall report for all tasks in the plan."""
    
    tasks = planner_load_tasks()
    
    overall_report = "Overall Report\n"
    overall_report += "----------------\n"
    
    if not tasks:
        overall_report += "No tasks found."
    else:
        for task_id, task in tasks.items():
            overall_report += f"Task ID: {task_id}\n"
            overall_report += f"Description: {task['description']}\n"
            overall_report += f"Completed: {task['completed']}\n"
            overall_report += f"Progress: {task['progress']}%\n"
            overall_report += "\n"
    
    return overall_report


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

