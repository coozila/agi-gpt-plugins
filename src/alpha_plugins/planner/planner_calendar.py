import json
import os

def create_event(event_id=None, event_data: str = None):
    """Create a new event and save it to the calendar"""
    events = load_events()
    events[str(event_id)] = event_data

    current_working_directory = os.getcwd()
    workdir = os.path.join(
        current_working_directory, "alpha", "alpha_workspace", "calendar.json"
    )
    file_name = workdir

    with open(file_name, "w") as f:
        json.dump(events, f)

    return events


def load_events() -> dict:
    """Load the events from the calendar"""
    current_working_directory = os.getcwd()
    workdir = os.path.join(
        current_working_directory, "alpha", "alpha_workspace", "calendar.json"
    )
    file_name = workdir

    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            f.write("{}")

    with open(file_name) as f:
        try:
            events = json.load(f)
            if isinstance(events, list):
                events = {}
        except json.JSONDecodeError:
            events = {}

    return events


def get_event(event_id):
    """Get the details of a specific event"""
    events = load_events()

    if str(event_id) not in events:
        return f"Event with ID {event_id} not found."

    return events[str(event_id)]


def update_event(event_id, event_data: str):
    """Update the details of an existing event"""
    events = load_events()

    if str(event_id) not in events:
        return f"Event with ID {event_id} not found."

    events[str(event_id)] = event_data

    current_working_directory = os.getcwd()
    workdir = os.path.join(
        current_working_directory, "alpha", "alpha_workspace", "calendar.json"
    )
    file_name = workdir

    with open(file_name, "w") as f:
        json.dump(events, f)

    return events


def delete_event(event_id):
    """Delete an event from the calendar"""
    events = load_events()

    if str(event_id) not in events:
        return f"Event with ID {event_id} not found."

    del events[str(event_id)]

    current_working_directory = os.getcwd()
    workdir = os.path.join(
        current_working_directory, "alpha", "alpha_workspace", "calendar.json"
    )
    file_name = workdir

    with open(file_name, "w") as f:
        json.dump(events, f)

    return f"Event with ID {event_id} has been deleted."
