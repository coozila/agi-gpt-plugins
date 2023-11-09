import json
import os

MEMORY_FILE_PATH = os.path.join(os.getcwd(), "agi-gpt", "agi-gpt_workspace", "planner_memory.json")

def load_memory():
    if not os.path.exists(MEMORY_FILE_PATH):
        with open(MEMORY_FILE_PATH, "w") as f:
            f.write("{}")

    with open(MEMORY_FILE_PATH) as f:
        try:
            memory = json.load(f)
            if isinstance(memory, list):
                memory = {}
        except json.JSONDecodeError:
            memory = {}

    return memory

def save_memory(memory):
    with open(MEMORY_FILE_PATH, "w") as f:
        json.dump(memory, f)
