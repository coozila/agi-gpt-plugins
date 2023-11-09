from typing import Any, Dict, List, Optional, Tuple, TypedDict, TypeVar

from agi-gpt_plugin_template import agi-gptPluginTemplate

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
from .planner_task_manager import task_manager

PromptGenerator = TypeVar("PromptGenerator")


class Message(TypedDict):
    role: str
    content: str


class PlannerPlugin(agi-gptPluginTemplate):
    """
    This is a task planner system plugin for agi-gpt which 
    adds the task planning commands to the prompt.
    """

    def __init__(self):
        super().__init__()
        self._name = "agi-gpt-Planner-Plugin"
        self._version = "0.1.1"
        self._description = "This is a simple task planner module for agi-gpt. It adds the run_planning_cycle " \
                            "command along with other task related commands. Creates a plan.md file and tasks.json " \
                            "to manage the workloads. For help and discussion: " \
                            "https://discord.com/channels/1092243196446249134/1098737397094694922/threads/1102780261604790393"

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:
        prompt.add_command(
            "check_plan",
            "Read the plan.md with the next goals to achieve",
            {},
            check_plan,
        )

        prompt.add_command(
            "run_planning_cycle",
            "Improves the current plan.md and updates it with progress",
            {},
            update_plan,
        )

        prompt.add_command(
            "create_task",
            "creates a task with a task id, description and a completed status of False ",
            {
                "task_id": "<int>",
                "task_description": "<The task that must be performed>",
            },
            create_task,
        )

        prompt.add_command(
            "load_tasks",
            "Checks out the task ids, their descriptionsand a completed status",
            {},
            load_tasks,
        )

        prompt.add_command(
            "mark_task_completed",
            "Updates the status of a task and marks it as completed",
            {"task_id": "<int>"},
            update_task_status,
        )

        prompt.add_command(
            "prioritize_tasks",
            "Prioritizes the tasks based on certain criteria",
            {},
            prioritize_tasks,
        )

        prompt.add_command(
            "filter_tasks",
            "Filter tasks based on progress, testing status, or date",
            {},
            filter_tasks,
        )

        prompt.add_command(
            "update_task",
            "Update the progress percentage, testing status, and date of a task",
            {
                "task_id": "<int>",
                "progress": "<float>",
                "testing_status": "<str>",
                "date": "<str>",
            },
            update_task,
        )

        prompt.add_command(
            "create_task_tracking",
            "Enhance the create_task function to include additional fields for tracking tasks",
            {
                "task_id": "<int>",
                "task_title": "<str>",
                "task_description": "<str>",
                "quality_parameters": "<str>",
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


