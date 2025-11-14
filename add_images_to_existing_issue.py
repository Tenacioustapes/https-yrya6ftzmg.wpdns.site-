"""
Add images to an existing GitHub issue
"""
import requests
import os
import subprocess
import sys

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

def add_images_to_issue(issue_number, image_files, repo, comment_prefix="**Images:**"):
    """Upload images and add them as a comment to an existing issue"""
    if not image_files:
        print("No images provided")
        return False
    
    print(f"Uploading {len(image_files)} image(s) to Imgur...\n")
    
    image_markdown = []
    for image_file in image_files:
        if os.path.exists(image_file):
            filename = os.path.basename(image_file)
            print(f"Uploading {filename}...", end=" ")
            url = upload_to_imgur(image_file)
            if url:
                print("OK")
                image_markdown.append(f"![{filename}]({url})")
            else:
                print("Failed")
        else:
            print(f"File not found: {image_file}")
    
    if image_markdown:
        comment_body = f"{comment_prefix}\n\n" + "\n\n".join(image_markdown)
        
        cmd = [
            "gh", "issue", "comment", str(issue_number),
            "--repo", repo,
            "--body", comment_body
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"\nSuccess! Images added to issue #{issue_number}")
            return True
        else:
            print(f"\nError adding comment: {result.stderr}")
            return False
    
    return False

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python add_images_to_existing_issue.py <issue_number> <repo> <image1> [image2] ...")
        print("Example: python add_images_to_existing_issue.py 3 Tenacioustapes/repo-name extracted_images/img1.png extracted_images/img2.png")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    repo = sys.argv[2]
    image_files = sys.argv[3:]
    
    add_images_to_issue(issue_number, image_files, repo)

