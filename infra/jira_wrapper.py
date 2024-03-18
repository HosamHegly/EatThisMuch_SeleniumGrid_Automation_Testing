import os
from dotenv import load_dotenv
from jira import JIRA

import config
import json
import Utils

# Load environment variables

def connect_jira():
    from pathlib import Path

    env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
    load_dotenv(env_path)

    # Retrieve environment variables
    token = os.getenv("token")
    jira_url = os.getenv("server")
    jira_user = os.getenv("user")

    return JIRA(basic_auth=(jira_user, token), options={"server": jira_url})


class JiraClient:
    def __init__(self):
        self.auth_jira = connect_jira()

    def create_issue(self, summary, description, project_key="NEW", issue_type="Bug"):
        issue_dict = {
            'project': {'key': project_key},
            'summary': f'Failed test: {summary}',
            'description': description,
            'issuetype': {'name': issue_type},
        }
        new_issue = self.auth_jira.create_issue(fields=issue_dict)
        return new_issue.key

