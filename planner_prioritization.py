import json
from alpha_plugins.planner.planner_task_manager import task_manager

def assign_priority(task_id, priority):
    """Assign a priority to a task"""
    tasks = task_manager.load_tasks()

    if str(task_id) not in tasks:
        return f"Task with ID {task_id} not found."

    tasks[str(task_id)]["priority"] = priority

    task_manager.save_tasks(tasks)

    return f"Priority {priority} assigned to task with ID {task_id}."


def sort_tasks_by_priority():
    """Sort tasks based on their priority"""
    tasks = task_manager.load_tasks()

    sorted_tasks = sorted(
        tasks.values(),
        key=lambda task: task.get("priority", 0),
        reverse=True
    )

    return sorted_tasks


def display_tasks_by_priority():
    """Display tasks sorted by their priority"""
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
