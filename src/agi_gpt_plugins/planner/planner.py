import os
import json
from dotenv import load_dotenv


def check_plan():
    current_working_directory = os.getcwd()
    workdir = os.path.join(current_working_directory, "agi-gpt", "agi-gpt_workspace", "plan.json")
    file_name = workdir

    if not os.path.exists(file_name):
        plan = {
            "tasks": [
                {
                    "description": "Create a detailed checklist for the current plan and goals",
                    "completed": False
                },
                {
                    "description": "Review that every new task is completed",
                    "completed": False
                }
            ],
            "notes": [
                "Use the run_planning_cycle command frequently to keep this plan up to date."
            ]
        }
        with open(file_name, "w") as file:
            json.dump(plan, file, indent=4)
        print(f"{file_name} created.")

    with open(file_name, "r") as file:
        return json.load(file)


def update_plan():
    current_working_directory = os.getcwd()
    workdir = os.path.join(current_working_directory, "agi-gpt", "agi-gpt_workspace", "plan.json")
    file_name = workdir

    with open(file_name, "r") as file:
        data = json.load(file)

    response = generate_improved_plan(data)

    with open(file_name, "w") as file:
        json.dump(response, file, indent=4)
    print(f"{file_name} updated.")

    return response


def generate_improved_plan(plan: dict) -> dict:
    import openai

    tasks = load_tasks()

    model = os.getenv('PLANNER_MODEL', os.getenv('FAST_LLM_MODEL', 'gpt-3.5-turbo'))
    max_tokens = os.getenv('PLANNER_TOKEN_LIMIT', os.getenv('FAST_TOKEN_LIMIT', 1500))
    temperature = os.getenv('PLANNER_TEMPERATURE', os.getenv('TEMPERATURE', 0.5))

    # Call the OpenAI API for chat completion
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are an assistant that improves and adds crucial points to plans in JSON format."
            },
            {
                "role": "user",
                "content": json.dumps(plan)
            }
        ],
        max_tokens=int(max_tokens),
        n=1,
        temperature=float(temperature)
    )

    # Extract the improved plan from the response
    improved_plan = response.choices[0].message.content.strip()
    return json.loads(improved_plan)


def create_task(task_id=None, task_description: str = None, status=False):
    task = {"description": task_description, "completed": status}
    tasks = load_tasks()
    tasks[str(task_id)] = task

    current_working_directory = os.getcwd()
    workdir = os.path.join(current_working_directory, "agi-gpt", "agi-gpt_workspace", "tasks.json")
    file_name = workdir

    with open(file_name, "w") as f:
        json.dump(tasks, f, indent=4)

    return tasks


def load_tasks() -> dict:
    current_working_directory = os.getcwd()
    workdir = os.path.join(current_working_directory, "agi-gpt", "agi-gpt_workspace", "tasks.json")
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


def update_task_status(task_id):
    tasks = load_tasks()

    if str(task_id) not in tasks:
        print(f"Task with ID {task_id} not found.")
        return

    tasks[str(task_id)]["completed"] = True

    current_working_directory = os.getcwd()
    workdir = os.path.join(current_working_directory, "agi-gpt", "agi-gpt_workspace", "tasks.json")
    file_name = workdir

    with open(file_name, "w") as f:
        json.dump(tasks, f, indent=4)

    return f"Task with ID {task_id} has been marked as completed."


if __name__ == "__main__":
    load_dotenv()
    # Your code here
