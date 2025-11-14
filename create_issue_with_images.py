"""
Create GitHub issue with automatic image embedding from Excel or image directory
"""
import requests
import os
import subprocess
import sys
import json

def upload_to_imgur(image_path):
    """Upload image to Imgur anonymously and return URL"""
    try:
        url = "https://api.imgur.com/3/image"
        
        with open(image_path, 'rb') as image_file:
            files = {'image': image_file}
            headers = {'Authorization': 'Client-ID 546c25a59c58ad7'}
            
            response = requests.post(url, headers=headers, files=files)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('success'):
                    return data['data']['link']
            return None
    except Exception as e:
        print(f"Error uploading {image_path}: {e}")
        return None

def find_images_for_issue(issue_data, image_dir="extracted_images"):
    """Find images that might be related to an issue"""
    # For now, we'll need to manually map or use a simple approach
    # This can be enhanced based on Excel cell positions or naming
    if not os.path.exists(image_dir):
        return []
    
    # Get all images
    all_images = sorted([f for f in os.listdir(image_dir) 
                         if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))])
    
    # For now, return all images - can be refined based on issue content
    return [os.path.join(image_dir, img) for img in all_images]

def upload_images_and_get_markdown(image_files):
    """Upload images to Imgur and return markdown"""
    if not image_files:
        return ""
    
    print(f"\nUploading {len(image_files)} image(s) to Imgur...")
    
    image_markdown = []
    for image_file in image_files:
        if os.path.exists(image_file):
            filename = os.path.basename(image_file)
            print(f"  Uploading {filename}...", end=" ")
            url = upload_to_imgur(image_file)
            if url:
                print("OK")
                image_markdown.append(f"![{filename}]({url})")
            else:
                print("Failed")
        else:
            print(f"  File not found: {image_file}")
    
    if image_markdown:
        return "\n\n**Images:**\n\n" + "\n\n".join(image_markdown)
    return ""

def create_issue_with_images(title, body, repo, image_files=None, labels=None, assignees=None, state="OPEN"):
    """Create GitHub issue and automatically embed images"""
    
    # Upload images and add to body
    image_markdown = ""
    if image_files:
        image_markdown = upload_images_and_get_markdown(image_files)
    
    # Combine body with images
    full_body = body
    if image_markdown:
        full_body = body + "\n\n" + image_markdown
    
    # Create issue
    cmd = ["gh", "issue", "create", "--repo", repo, "--title", title, "--body", full_body]
    
    if labels:
        if isinstance(labels, list):
            labels = ",".join(labels)
        cmd.extend(["--label", labels])
    
    if assignees:
        if isinstance(assignees, list):
            assignees = ",".join(assignees)
        cmd.extend(["--assignee", assignees])
    
    print(f"\nCreating issue: {title}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        issue_url = result.stdout.strip()
        issue_number = issue_url.split('/')[-1]
        print(f"Success! Issue created: {issue_url}")
        
        # If state is CLOSED, close the issue
        if state.upper() == "CLOSED":
            close_cmd = ["gh", "issue", "close", issue_number, "--repo", repo]
            subprocess.run(close_cmd, capture_output=True)
            print(f"Issue #{issue_number} marked as closed")
        
        return issue_number
    else:
        print(f"Error creating issue: {result.stderr}")
        return None

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) < 4:
        print("Usage: python create_issue_with_images.py <title> <body> <repo> [image1] [image2] ... [--label label1,label2] [--state CLOSED]")
        sys.exit(1)
    
    title = sys.argv[1]
    body = sys.argv[2]
    repo = sys.argv[3]
    
    # Parse arguments
    image_files = []
    labels = None
    assignees = None
    state = "OPEN"
    
    i = 4
    while i < len(sys.argv):
        if sys.argv[i] == "--label":
            labels = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--assignee" or sys.argv[i] == "--assignees":
            assignees = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--state":
            state = sys.argv[i + 1]
            i += 2
        else:
            image_files.append(sys.argv[i])
            i += 1
    
    create_issue_with_images(title, body, repo, image_files if image_files else None, labels, assignees, state)

