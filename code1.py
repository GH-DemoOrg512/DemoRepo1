from urllib.parse import urlparse

def construct_issues_url(jira_url, project_key):
    # Extract username from the Jira URL
    username = extract_username(jira_url)

    # Construct the URL for retrieving issues
    issues_url = f"{jira_url}/rest/api/2/search?jql=project={project_key}"

    return issues_url

def extract_username(jira_url):
    try:
        parsed_url = urlparse(jira_url)
        username = parsed_url.netloc.split('.')[0]
        return username
    except Exception as e:
        print(f"Error extracting username: {e}")
        return None

# Example usage
jira_url = "https://shruthinv88.atlassian.net"
project_key = "YOUR_PROJECT_KEY"

issues_url = construct_issues_url(jira_url, project_key)
print("Issues URL:", issues_url)
