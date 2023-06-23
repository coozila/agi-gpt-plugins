class ProjectNode:
    def __init__(self, order_number, title, description, tools):
        self.order_number = order_number
        self.title = title
        self.description = description
        self.tools = tools
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def planner_build_project_tree():
    """Build the project tree structure."""
    # Logic for building the project tree
    # ...


def planner_display_project_tree(project_node, indent=0):
    """Display the project tree structure."""
    # Logic for displaying the project tree
    # ...


def planner_execute_project(project_node):
    """Execute the project based on the project tree structure."""
    # Logic for executing the project
    # ...


def planner_assign_tasks_to_agents(project_node):
    """Assign tasks to specialized agents based on the project tree structure."""
    # Logic for assigning tasks to agents
    # ...


def planner_report_to_user(project_node):
    """Generate a report for the user based on the project tree structure."""
    # Logic for generating a report for the user
    # ...
