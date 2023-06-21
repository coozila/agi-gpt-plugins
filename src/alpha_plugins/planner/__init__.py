from typing import Any, Dict, List, Optional, Tuple, TypedDict, TypeVar

from alpha_plugin_template import AlphaPluginTemplate

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


from .planner import (
    check_plan,
    create_task,
    load_tasks,
    update_plan,
    update_task_status,
)
from .planner_prioritization import prioritize_tasks
from .planner_filter import filter_tasks
from .planner_update import update_task
from .planner_tracking import create_task_tracking
from .planner_environmental_impact_assessment import assess_environmental_impact
from .planner_version_control import manage_version_control
from .planner_visualization import visualize_steps

def initialize_plugins() -> AlphaPluginTemplate:
    prompt = AlphaPluginTemplate("Planner", "Manage tasks and plans")

    prompt.add_command(
        "check_plan",
        "Check the progress of a plan",
        {"plan_id": "<int>"},
        check_plan,
    )

    prompt.add_command(
        "update_plan",
        "Update the progress of a plan",
        {"plan_id": "<int>", "progress": "<float>"},
        update_plan,
    )

    prompt.add_command(
        "create_task",
        "Create a new task",
        {
            "task_id": "<int>",
            "task_description": "<str>",
            "status": "<bool> (optional)",
        },
        create_task,
    )

    prompt.add_command(
        "update_task_status",
        "Update the status of a task",
        {"task_id": "<int>"},
        update_task_status,
    )

    prompt.add_command(
        "assign_priority",
        "Assign priority to a task",
        {"task_id": "<int>", "priority": "<int>"},
        assign_priority,
    )

    prompt.add_command(
        "sort_tasks_by_priority",
        "Sort tasks by priority",
        {},
        sort_tasks_by_priority,
    )

    prompt.add_command(
        "display_tasks_by_priority",
        "Display tasks sorted by priority",
        {},
        display_tasks_by_priority,
    )

    prompt.add_command(
        "prioritize_tasks",
        "Prioritize tasks",
        {"task_ids": "<List[int]>", "priority": "<int>"},
        prioritize_tasks,
    )

    prompt.add_command(
        "filter_tasks",
        "Filter tasks based on status",
        {"status": "<bool>"},
        filter_tasks,
    )

    prompt.add_command(
        "update_task",
        "Update a task",
        {
            "task_id": "<int>",
            "new_description": "<str>",
            "new_due_date": "<str>",
        },
        update_task,
    )

    prompt.add_command(
        "create_task_tracking",
        "Create a task tracking record",
        {
            "task_id": "<int>",
            "status": "<str>",
            "progress": "<float>",
            "due_date": "<str>",
        },
        create_task_tracking,
    )

    prompt.add_command(
        "assess_environmental_impact",
        "Assess the environmental impact of the tasks",
        {},
        assess_environmental_impact,
    )

    prompt.add_command(
        "manage_version_control",
        "Manage version control for tasks",
        {},
        manage_version_control,
    )

    prompt.add_command(
        "visualize_steps",
        "Visualize the steps of a task",
        {"task_id": "<int>"},
        visualize_steps,
    )

    return prompt

