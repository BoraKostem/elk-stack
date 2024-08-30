import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()
# Replace with your GitLab instance URL and Personal Access Token
GITLAB_URL = 'https://gitlab-url-here.com/'
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

# Set up the headers for authentication
headers = {
    'Private-Token': ACCESS_TOKEN
}

# Fetch all projects
projects_url = f'{GITLAB_URL}/api/v4/projects'
response = requests.get(projects_url, headers=headers)
projects = response.json()

project_data = []  # List to hold project data dictionaries

for project in projects:
    project_info = {
        "project_name": project['name'],
        "creation_time": project['created_at']  # Get creation time of the repository
    }

    # Fetch commits for each project
    commits_url = f'{projects_url}/{project["id"]}/repository/commits'
    commits_response = requests.get(commits_url, headers=headers)
    commits = commits_response.json()
    project_info["commits"] = len(commits)
    if commits:  # Check if there are any commits
        project_info["last_commit_time"] = commits[0]['committed_date']  # Get last commit time

    # Fetch branches for each project
    branches_url = f'{projects_url}/{project["id"]}/repository/branches'
    branches_response = requests.get(branches_url, headers=headers)
    branches = branches_response.json()
    project_info["branches"] = len(branches)

    project_data.append(project_info)

# Write project data to a JSON file
with open('sample_logs/project_data.json', 'w') as json_file:
    json.dump(project_data, json_file, indent=2)