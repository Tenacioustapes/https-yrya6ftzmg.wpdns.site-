#!/usr/bin/env python3
"""
Export GitHub issues in a formatted, printable format
"""
import subprocess
import json
import sys
from datetime import datetime

def get_issues(repo, state="open"):
    """Get all issues from GitHub"""
    cmd = [
        "gh", "issue", "list",
        "--repo", repo,
        "--state", state,
        "--limit", "100",
        "--json", "number,title,body,labels,state,url,createdAt,updatedAt,assignees"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if result.returncode != 0:
        print(f"Error: {result.stderr}", file=sys.stderr)
        return []
    
    if not result.stdout:
        return []
    
    return json.loads(result.stdout)

def format_priority(labels):
    """Extract priority from labels"""
    for label in labels:
        if label['name'] in ['P0', 'P1', 'P2']:
            return label['name']
    return "None"

def format_labels(labels):
    """Format labels excluding priority"""
    priority_labels = ['P0', 'P1', 'P2', 'priority-high', 'priority-medium', 'priority-low']
    other_labels = [l['name'] for l in labels if l['name'] not in priority_labels]
    return ", ".join(other_labels) if other_labels else "None"

def format_date(date_str):
    """Format ISO date to readable format"""
    if not date_str:
        return "N/A"
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.strftime("%Y-%m-%d")
    except:
        return date_str

def format_issue(issue):
    """Format a single issue for printing"""
    priority = format_priority(issue['labels'])
    labels = format_labels(issue['labels'])
    assignees = ", ".join([a['login'] for a in issue['assignees']]) if issue['assignees'] else "Unassigned"
    
    output = []
    output.append("=" * 80)
    output.append(f"Issue #{issue['number']}: {issue['title']}")
    output.append("=" * 80)
    output.append(f"Priority: {priority}")
    output.append(f"Status: {issue['state'].upper()}")
    output.append(f"Labels: {labels}")
    output.append(f"Assignees: {assignees}")
    output.append(f"Created: {format_date(issue['createdAt'])}")
    output.append(f"Updated: {format_date(issue['updatedAt'])}")
    output.append(f"URL: {issue['url']}")
    output.append("")
    
    if issue.get('body'):
        body = issue['body'].strip()
        if body:
            output.append("Description:")
            output.append("-" * 80)
            # Truncate very long bodies
            if len(body) > 2000:
                output.append(body[:2000] + "\n... (truncated)")
            else:
                output.append(body)
            output.append("")
    
    output.append("")
    return "\n".join(output)

def main():
    repo = "Tenacioustapes/https-yrya6ftzmg.wpdns.site-"
    
    print("Fetching open issues...")
    issues = get_issues(repo, "open")
    
    if not issues:
        print("No issues found.")
        return
    
    # Sort by priority (P0 first) then by number
    def sort_key(issue):
        priority = format_priority(issue['labels'])
        priority_order = {"P0": 0, "P1": 1, "P2": 2, "None": 3}
        return (priority_order.get(priority, 3), issue['number'])
    
    issues.sort(key=sort_key)
    
    # Generate formatted output
    output = []
    output.append("=" * 80)
    output.append("GITHUB ISSUES - FORMATTED EXPORT")
    output.append("=" * 80)
    output.append(f"Repository: {repo}")
    output.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    output.append(f"Total Issues: {len(issues)}")
    output.append("")
    
    # Summary by priority
    priorities = {}
    for issue in issues:
        p = format_priority(issue['labels'])
        priorities[p] = priorities.get(p, 0) + 1
    
    output.append("Summary by Priority:")
    for p in ["P0", "P1", "P2", "None"]:
        if p in priorities:
            output.append(f"  {p}: {priorities[p]} issues")
    output.append("")
    output.append("=" * 80)
    output.append("")
    
    # Format each issue
    for issue in issues:
        output.append(format_issue(issue))
    
    # Write to file
    filename = "formatted_issues_export.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("\n".join(output))
    
    print(f"\nFormatted issues exported to: {filename}")
    print(f"Total issues: {len(issues)}")
    
    # Also print to console (first 3 issues as preview)
    try:
        print("\n" + "=" * 80)
        print("PREVIEW (first 3 issues):")
        print("=" * 80)
        preview_text = "\n".join(output[:500])  # First ~500 lines as preview
        # Replace any problematic unicode characters for console
        preview_text = preview_text.encode('ascii', 'replace').decode('ascii')
        print(preview_text)
        if len(output) > 500:
            print(f"\n... ({len(output) - 500} more lines in file)")
    except UnicodeEncodeError:
        print("\nPreview skipped due to encoding issues. See file for full output.")

if __name__ == "__main__":
    main()

