from src.repositories.jira_repository import JiraRepository
from atlassian import Jira
class JiraHelper():

    def __init__(self):
        super().__init__()
        self.jira_repo = JiraRepository()
        if self.jira_repo.jira_status() == True:
            self.jira = Jira(
                url=self.jira_repo.get_url(),
                username=self.jira_repo.get_username(),
                password=self.jira_repo.get_api_key(),
                cloud=self.jira_repo.get_cloud()
            )


    def get_all_projects(self):
        projects = self.jira.get_all_projects()
        result = []
        for project in projects:
            dict = {"name": project['name'], "key": project['key']}
            result.append(dict)
        return result

    def get_issues_by_user(self, jira_id):
        issues = self.jira.jql('assignee = ' + jira_id)
        result = []
        for issue in issues['issues']:
            dict = {"issueType": issue['fields']['issuetype']['name'], "summary": issue['fields']['summary'], "status": issue['fields']['status']['name'], "key": issue['key'], "description": issue['fields']['description'], "created_at": issue['fields']['created'], "updated_at": issue['fields']['created']}
            result.append(dict)
        return result

    def get_projects_by_user(self, jira_id):
        issues = self.jira.jql('assignee = ' + jira_id)
        result = {}
        projects = set()
        for issue in issues['issues']:
            projects.add(issue['fields']['project']['name'])
        result['projects'] = list(projects)
        return result

    def get_all_users(self):
        response = self.jira.users_get_all()
        users = []
        for user in response:
            if user['accountType'] == 'atlassian' and user['active'] == True:
                dict = {"jira_id": user['accountId'],  "display_name": user['displayName']}
                users.append(dict)
        return users
