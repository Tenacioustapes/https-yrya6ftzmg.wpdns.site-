# Assigning Issues Without GitHub Accounts

GitHub's assignee dropdown only works for GitHub users. However, you can track who should work on issues without requiring GitHub accounts.

## Alternative Methods

### Option 1: Use Labels (Recommended)
Create custom labels for each team member:

```bash
# Create labels for team members
gh label create "assigned-erin" --description "Assigned to Erin" --color "0e8a16"
gh label create "assigned-developer" --description "Assigned to Developer" --color "1d76db"
gh label create "assigned-client" --description "Assigned to Client" --color "fbca04"
```

Then use labels when creating/editing issues:
```bash
gh issue create --title "Title" --body "Description" --label "assigned-erin"
gh issue edit <NUMBER> --add-label "assigned-erin"
```

### Option 2: Use Issue Title/Description
Include the assignee name in the title or description:

```bash
gh issue create --title "[Erin] Fix mobile layout" --body "Assigned to: Erin\n\nDescription here..."
```

### Option 3: Use Custom Format in Body
Create a standard format in the issue body:

```markdown
## Assignment
**Assigned to:** Erin
**Priority:** High
**Due Date:** 2025-01-15

## Description
Issue details here...
```

### Option 4: Use Comments
Add a comment with assignment info:

```bash
gh issue comment <NUMBER> --body "**Assigned to:** Erin\n**Status:** In Progress"
```

## Automated Script with Non-GitHub Assignees

You can modify the issue creation script to support "assignees" that aren't GitHub users by using labels or custom body format.

## Best Practice Workflow

1. **Create label-based assignment system:**
   ```bash
   gh label create "team-erin" --color "0e8a16"
   gh label create "team-developer" --color "1d76db"
   gh label create "team-client" --color "fbca04"
   ```

2. **Use labels + mention in description:**
   ```bash
   gh issue create \
     --title "Fix mobile layout" \
     --body "**Assigned to:** Erin\n\nDescription..." \
     --label "team-erin"
   ```

3. **Filter by label to see who's assigned:**
   ```bash
   gh issue list --label "team-erin"
   ```

## Benefits of Label Approach

- ✅ No GitHub account required
- ✅ Easy to filter/search issues by person
- ✅ Can see all issues assigned to someone
- ✅ Works with GitHub's existing label system
- ✅ Can combine with other labels (bug, priority, etc.)

