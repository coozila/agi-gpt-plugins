import json
import os

def perform_environmental_impact_assessment(plan):
    # Perform the environmental impact assessment
    # Analyze the potential environmental consequences
    # Consider factors such as resource consumption, energy usage, emissions, and waste generation
    # Generate a report or score based on the assessment

    # Define and populate the assessment_report variable
    assessment_report = "Assessment report goes here"

    # Return the assessment report or score
    return assessment_report

def save_environmental_impact_assessment(plan_id, assessment_report):
    assessments = load_environmental_impact_assessments()
    assessments[str(plan_id)] = assessment_report
    save_environmental_impact_assessments(assessments)

def load_environmental_impact_assessments():
    current_working_directory = os.getcwd()
    workdir = os.path.join(current_working_directory, "alpha", "alpha_workspace", "environmental_assessments.json")
    file_name = workdir

    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            f.write("{}")

    with open(file_name) as f:
        try:
            assessments = json.load(f)
            if isinstance(assessments, list):
                assessments = {}
        except json.JSONDecodeError:
            assessments = {}

    return assessments

def save_environmental_impact_assessments(assessments):
    current_working_directory = os.getcwd()
    workdir = os.path.join(current_working_directory, "alpha", "alpha_workspace", "environmental_assessments.json")
    file_name = workdir

    with open(file_name, "w") as f:
        json.dump(assessments, f)
