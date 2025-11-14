# Adding Collaborators (Assignees) to Repository

To make someone (like Erin) available as an assignee in the dropdown, they need to be added as a collaborator to the repository.

## Steps to Add Erin as Collaborator

### Option 1: Via GitHub Web Interface (Easiest)

1. Go to your repository: https://github.com/Tenacioustapes/https-yrya6ftzmg.wpdns.site-
2. Click **Settings** (top right of the repository page)
3. Click **Collaborators** in the left sidebar
4. Click **Add people** button
5. Enter Erin's GitHub username or email
6. Select permission level:
   - **Read** - Can view issues and comment
   - **Triage** - Can manage issues and pull requests
   - **Write** - Can push code and manage issues
   - **Maintain** - Can manage repository settings
   - **Admin** - Full access
7. Click **Add [username] to this repository**

### Option 2: Via GitHub CLI

```bash
# Add Erin as a collaborator (replace 'ErinGitHubUsername' with actual username)
gh api repos/Tenacioustapes/https-yrya6ftzmg.wpdns.site-/collaborators/ErinGitHubUsername -X PUT

# Set permission level (optional, defaults to 'push')
gh api repos/Tenacioustapes/https-yrya6ftzmg.wpdns.site-/collaborators/ErinGitHubUsername \
  -X PUT -f permission=push
```

**Permission levels:**
- `pull` - Read access
- `triage` - Triage access (can manage issues)
- `push` - Write access
- `maintain` - Maintain access
- `admin` - Admin access

### Option 3: Invite via Email

If Erin doesn't have a GitHub account yet:
1. They need to create a GitHub account first at https://github.com/signup
2. Then follow Option 1 or 2 above

## After Adding Collaborator

Once Erin is added as a collaborator, you can assign issues to them:

```bash
# Assign issue to Erin (using her GitHub username)
gh issue edit <NUMBER> --add-assignee ErinGitHubUsername

# Or when creating
gh issue create --title "Title" --body "Description" --assignee ErinGitHubUsername
```

## Check Current Collaborators

```bash
# List all collaborators
gh api repos/Tenacioustapes/https-yrya6ftzmg.wpdns.site-/collaborators

# Check assignable users
gh repo view Tenacioustapes/https-yrya6ftzmg.wpdns.site- --json assignableUsers
```

## Notes

- **GitHub username required**: You'll need Erin's exact GitHub username (not just "Erin")
- **Permission level**: For issue assignment, "Read" or "Triage" permission is sufficient
- **Organization vs Personal**: If this is an organization repo, you might need to add Erin to the organization first

