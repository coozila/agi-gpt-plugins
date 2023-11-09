import json
import os
import datetime

def create_version(version_data):
    versions = load_versions()
    version_id = generate_version_id()
    versions[version_id] = version_data
    save_versions(versions)
    return version_id

def load_versions():
    current_working_directory = os.getcwd()
    workdir = os.path.join(current_working_directory, "agi-gpt", "agi-gpt_workspace", "versions.json")
    file_name = workdir

    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            f.write("{}")

    with open(file_name) as f:
        try:
            versions = json.load(f)
            if isinstance(versions, list):
                versions = {}
        except json.JSONDecodeError:
            versions = {}

    return versions

def save_versions(versions):
    current_working_directory = os.getcwd()
    workdir = os.path.join(current_working_directory, "agi-gpt", "agi-gpt_workspace", "versions.json")
    file_name = workdir

    with open(file_name, "w") as f:
        json.dump(versions, f)

def generate_version_id():
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    return f"v{timestamp}"

def get_latest_version():
    versions = load_versions()
    if versions:
        latest_version = max(versions.keys())
        return latest_version
    return None

def get_version_details(version_id):
    versions = load_versions()
    if version_id in versions:
        return versions[version_id]
    return None

def release_version(version_id):
    versions = load_versions()
    if version_id in versions:
        versions[version_id]["released"] = True
        save_versions(versions)
        return f"Version {version_id} released successfully."
    return f"Version {version_id} not found."

def rollback_to_version(version_id):
    versions = load_versions()
    if version_id in versions:
        versions[version_id]["rolled_back"] = True
        save_versions(versions)
        return f"Rolled back to version {version_id} successfully."
    return f"Version {version_id} not found."

def list_versions():
    versions = load_versions()
    return list(versions.keys())
