"""
Upload images to Imgur and update GitHub issue with embedded images
"""
import requests
import os
import subprocess
import sys

def upload_to_imgur(image_path):
    """Upload image to Imgur anonymously"""
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
        print(f"Error: {e}")
        return None

def update_issue_with_images(issue_number, image_files, repo):
    """Upload images and update issue with embedded images"""
    print(f"Uploading {len(image_files)} image(s) to Imgur...\n")
    
    image_markdown = []
    for image_file in image_files:
        if os.path.exists(image_file):
            print(f"Uploading {os.path.basename(image_file)}...", end=" ")
            url = upload_to_imgur(image_file)
            if url:
                print("OK")
                image_markdown.append(f"![{os.path.basename(image_file)}]({url})")
            else:
                print("Failed")
        else:
            print(f"File not found: {image_file}")
    
    if image_markdown:
        # Create comment with images
        comment_body = "**Example Images:**\n\n" + "\n\n".join(image_markdown)
        
        # Add comment to issue
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
    issue_number = 2
    repo = "Tenacioustapes/https-yrya6ftzmg.wpdns.site-"
    
    # Images for issue 2
    images = [
        "extracted_images/Sheet1_image_3.png",
        "extracted_images/Sheet1_image_4.png"
    ]
    
    update_issue_with_images(issue_number, images, repo)

