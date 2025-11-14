"""
Script to move GitHub issues from 'To triage' to 'Ready' status in Production Website project
Uses GitHub GraphQL API
"""
import subprocess
import json
import sys

def run_gh_api(query):
    """Run GitHub GraphQL query"""
    cmd = ["gh", "api", "graphql", "-f", f"query={query}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None
    return json.loads(result.stdout)

def get_project_info():
    """Get Production Website project information"""
    query = """
    {
      viewer {
        projectsV2(first: 10) {
          nodes {
            id
            title
            fields(first: 20) {
              nodes {
                ... on ProjectV2Field {
                  id
                  name
                }
                ... on ProjectV2SingleSelectField {
                  id
                  name
                  options {
                    id
                    name
                  }
                }
              }
            }
          }
        }
      }
    }
    """
    
    result = run_gh_api(query)
    if not result:
        return None
    
    projects = result.get('data', {}).get('viewer', {}).get('projectsV2', {}).get('nodes', [])
    
    for project in projects:
        if project.get('title') == 'Production Website':
            return project
    
    print("Project 'Production Website' not found")
    return None

def get_issue_items(project_id, issue_numbers):
    """Get project items for specific issues"""
    # We'll need to get items by issue number
    # This requires finding items that link to these issues
    items = []
    for issue_num in issue_numbers:
        query = f"""
        {{
          repository(owner: "Tenacioustapes", name: "https-yrya6ftzmg.wpdns.site-") {{
            issue(number: {issue_num}) {{
              id
              projectItems(first: 10) {{
                nodes {{
                  id
                  project {{
                    id
                  }}
                }}
              }}
            }}
          }}
        }}
        """
        result = run_gh_api(query)
        if result:
            issue_data = result.get('data', {}).get('repository', {}).get('issue')
            if issue_data:
                project_items = issue_data.get('projectItems', {}).get('nodes', [])
                for item in project_items:
                    if item.get('project', {}).get('id') == project_id:
                        items.append({
                            'item_id': item['id'],
                            'issue_number': issue_num
                        })
    return items

def move_item_to_status(project_id, item_id, status_field_id, ready_option_id):
    """Move a project item to Ready status"""
    mutation = f"""
    mutation {{
      updateProjectV2ItemFieldValue(
        input: {{
          projectId: "{project_id}"
          itemId: "{item_id}"
          fieldId: "{status_field_id}"
          value: {{
            singleSelectOptionId: "{ready_option_id}"
          }}
        }}
      ) {{
        projectV2Item {{
          id
        }}
      }}
    }}
    """
    
    result = run_gh_api(mutation)
    return result is not None

def main():
    issue_numbers = [1, 4, 5, 6, 7]
    
    print("Getting project information...")
    project = get_project_info()
    if not project:
        print("Could not find 'Production Website' project")
        print("\nTrying alternative: Use web interface at:")
        print("https://github.com/users/Tenacioustapes/projects")
        return
    
    project_id = project['id']
    print(f"Found project: {project['title']} (ID: {project_id})")
    
    # Find Status field
    status_field = None
    ready_option = None
    
    for field in project.get('fields', {}).get('nodes', []):
        if field.get('name') == 'Status':
            status_field = field
            # Find "Ready" option
            for option in field.get('options', []):
                if option.get('name') == 'Ready':
                    ready_option = option
                    break
            break
    
    if not status_field:
        print("Could not find 'Status' field in project")
        return
    
    if not ready_option:
        print("Could not find 'Ready' option in Status field")
        return
    
    print(f"Found Status field (ID: {status_field['id']})")
    print(f"Found Ready option (ID: {ready_option['id']})")
    
    # Get issue items
    print(f"\nGetting project items for issues: {issue_numbers}")
    items = get_issue_items(project_id, issue_numbers)
    
    if not items:
        print("Could not find project items for these issues")
        print("Make sure the issues are already added to the project")
        return
    
    print(f"Found {len(items)} items to move")
    
    # Move each item
    success_count = 0
    for item in items:
        print(f"Moving issue #{item['issue_number']}...", end=" ")
        if move_item_to_status(project_id, item['item_id'], status_field['id'], ready_option['id']):
            print("OK")
            success_count += 1
        else:
            print("Failed")
    
    print(f"\nSuccessfully moved {success_count}/{len(items)} issues to 'Ready' status")

if __name__ == "__main__":
    main()

