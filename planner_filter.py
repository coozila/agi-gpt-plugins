import datetime
import json
import os
from planner_task_manager import task_manager
from planner_memory import load_memory, save_memory

def filter_tasks_by_progress(completed=False):
    tasks = load_memory()
    filtered_tasks = [task for task in tasks.values() if task["completed"] == completed]
    return filtered_tasks

def filter_tasks_by_testing_status(testing_status):
    tasks = load_memory()
    filtered_tasks = [task for task in tasks.values() if task.get("testing_status") == testing_status]
    return filtered_tasks

def filter_tasks_by_date(start_date=None, end_date=None):
    tasks = load_memory()
    filtered_tasks = []
    
    for task in tasks.values():
        if "due_date" in task:
            due_date = datetime.datetime.strptime(task["due_date"], "%Y-%m-%d").date()
            
            if start_date and due_date < start_date:
                continue
            if end_date and due_date > end_date:
                continue
                
        filtered_tasks.append(task)
    
    return filtered_tasks

def save_filtered_tasks(filtered_tasks):
    save_memory(filtered_tasks)
