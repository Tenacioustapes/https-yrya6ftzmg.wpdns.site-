# Tenacious Web Issue Tracker

This repository serves as an issue tracker for the upcoming website project.

## 🛠️ Tools Setup

### GitHub CLI (gh)
GitHub CLI is already installed and authenticated! You can use it to manage issues directly from the command line.

**Repository:** https://github.com/Tenacioustapes/https-yrya6ftzmg.wpdns.site-

### GitHub Copilot CLI
GitHub Copilot CLI is installed for AI-powered coding assistance.

**Note:** Copilot CLI requires Node.js v22+. You currently have v20.11.0. Consider upgrading if you encounter issues.

## 📋 Common GitHub CLI Commands for Issue Tracking

### View Issues
```bash
# List all open issues
gh issue list

# List all issues (open and closed)
gh issue list --state all

# View a specific issue
gh issue view <issue-number>
```

### Create Issues
```bash
# Create a new issue interactively
gh issue create

# Create an issue with title and body
gh issue create --title "Issue Title" --body "Issue description"

# Create an issue with a label
gh issue create --title "Bug: Something broken" --body "Description" --label bug

# Create an issue and assign it
gh issue create --title "Issue Title" --body "Description" --assignee @me

# Create an issue with label and assignee
gh issue create --title "Bug" --body "Description" --label bug --assignee @me,developer1

# Create an issue from a file (useful for including images via markdown)
gh issue create --title "Issue Title" --body-file issue-body.md
```

### Including Images in Issues

**Yes, you can include images!** Here are the methods:

#### Method 1: Using External Image Hosting (CLI)
1. Upload your image to an image hosting service (Imgur, ImgBB, etc.)
2. Get the direct URL to the image
3. Include it in your issue using Markdown:

```bash
gh issue create --title "Bug with Screenshot" --body "Here's the issue: ![Screenshot](https://i.imgur.com/example.png)"
```

#### Method 2: Using GitHub's Web Interface (Easiest)
1. Create the issue via web: `gh issue create --web`
2. Drag and drop images directly into the issue body
3. GitHub automatically uploads and embeds them

#### Method 3: Using a Body File with Markdown
Create a file `issue-body.md`:
```markdown
## Description
Here's the issue I'm seeing.

![Screenshot](https://your-image-url.com/image.png)

More details here...
```

Then create the issue:
```bash
gh issue create --title "Issue Title" --body-file issue-body.md
```

#### Method 4: Adding Images to Comments
```bash
gh issue comment <NUMBER> --body "Here's a screenshot: ![Image](https://image-url.com/img.png)"
```

#### Method 5: Automated Image Embedding (Recommended)
Use the provided Python scripts to automatically upload and embed images:

**Create new issue with images:**
```bash
python create_issue_with_images.py "Issue Title" "Issue description" "Tenacioustapes/repo-name" image1.png image2.png
```

**Add images to existing issue:**
```bash
python add_images_to_existing_issue.py <issue_number> "Tenacioustapes/repo-name" image1.png image2.png
```

These scripts automatically:
- Upload images to Imgur
- Generate markdown with embedded image URLs
- Add images to the issue

**Note:** Images are automatically embedded when creating issues from Excel files using the workflow scripts.

### Manage Issues
```bash
# Close an issue
gh issue close <issue-number>

# Reopen an issue
gh issue reopen <issue-number>

# Add a comment to an issue
gh issue comment <issue-number> --body "Your comment here"

# Add labels to an issue
gh issue edit <issue-number> --add-label "enhancement,priority-high"

# Assign an issue
gh issue edit <issue-number> --add-assignee @me

# Assign multiple people
gh issue edit <issue-number> --add-assignee @me,username1,username2

# Remove an assignee
gh issue edit <issue-number> --remove-assignee username1
```

### Search and Filter
```bash
# List issues by label
gh issue list --label "bug"

# List issues assigned to you
gh issue list --assignee @me

# List issues by author
gh issue list --author Tenacioustapes
```

## 🤖 Using GitHub Copilot CLI

### Launch Copilot CLI
```bash
copilot
```

### First Time Setup
1. Launch `copilot` in this directory
2. If not logged in, use `/login` command
3. Authenticate with your GitHub account

### Copilot CLI Commands
- `/login` - Authenticate with GitHub
- `/model` - Choose AI model (default: Claude Sonnet 4.5)
- `/feedback` - Submit feedback
- `/banner` - Show the animated banner

### Using Copilot CLI for Issue Management
You can ask Copilot CLI to help with:
- Creating issue templates
- Analyzing issues
- Generating issue reports
- Writing issue descriptions

## 📝 Issue Labels (Recommended)

Consider creating these labels for better organization:
- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Documentation improvements
- `priority-high` - High priority
- `priority-medium` - Medium priority
- `priority-low` - Low priority
- `in-progress` - Currently being worked on
- `blocked` - Waiting on something else

### Create Labels via CLI
```bash
gh label create bug --description "Something isn't working" --color "d73a4a"
gh label create enhancement --description "New feature or request" --color "a2eeef"
gh label create documentation --description "Documentation improvements" --color "0075ca"
gh label create "priority-high" --description "High priority" --color "b60205"
gh label create "priority-medium" --description "Medium priority" --color "fbca04"
gh label create "priority-low" --description "Low priority" --color "0e8a16"
gh label create "in-progress" --description "Currently being worked on" --color "1d76db"
gh label create blocked --description "Waiting on something else" --color "e99695"
```

## 🚀 Quick Start

1. **Create your first issue:**
   ```bash
   gh issue create --title "Website Planning" --body "Initial planning for the website"
   ```

2. **View all issues:**
   ```bash
   gh issue list
   ```

3. **Get help:**
   ```bash
   gh issue --help
   gh --help
   ```

## 📚 Resources

- [GitHub CLI Documentation](https://cli.github.com/manual/)
- [GitHub Copilot CLI](https://github.com/github/copilot-cli)
- [GitHub Issues Guide](https://docs.github.com/en/issues)

