# Quick Reference Guide

## Most Common Commands

### Create an Issue
```bash
gh issue create --title "Your issue title" --body "Description of the issue"
```

### List All Open Issues
```bash
gh issue list
```

### View Issue Details
```bash
gh issue view <NUMBER>
```

### Add Comment to Issue
```bash
gh issue comment <NUMBER> --body "Your comment"
```

### Close an Issue
```bash
gh issue close <NUMBER>
```

### Assign Issues
```bash
# Assign to yourself
gh issue edit <NUMBER> --add-assignee @me

# Assign to specific user(s)
gh issue edit <NUMBER> --add-assignee username1,username2

# Remove assignee
gh issue edit <NUMBER> --remove-assignee username1

# Assign when creating
gh issue create --title "Title" --body "Description" --assignee @me
```

## Including Images

**Quick ways to add images:**

1. **Via Web Interface (Easiest):**
   ```bash
   gh issue create --web
   # Then drag & drop images directly
   ```

2. **Via CLI with Image URL:**
   ```bash
   gh issue create --title "Bug" --body "![Screenshot](https://i.imgur.com/example.png)"
   ```

3. **Add image to comment:**
   ```bash
   gh issue comment 1 --body "![Image](https://image-url.com/img.png)"
   ```

## Example Workflow

1. **Create a new issue:**
   ```bash
   gh issue create --title "Add homepage design" --body "Need to design the homepage layout"
   ```

2. **View it:**
   ```bash
   gh issue list
   ```

3. **Add a comment with image:**
   ```bash
   gh issue comment 1 --body "Here's the mockup: ![Mockup](https://image-url.com/mockup.png)"
   ```

4. **Close when done:**
   ```bash
   gh issue close 1
   ```

## Copilot CLI Quick Start

```bash
# Launch Copilot CLI
copilot

# Then you can ask it things like:
# "Create an issue template for bug reports"
# "List all open issues and summarize them"
# "Help me write a good issue description for..."
```

