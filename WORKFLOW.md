# Issue Creation Workflow

## Automated Image Embedding

When creating issues, images are **automatically embedded** if they exist. The workflow ensures:

1. ✅ Images are uploaded to Imgur automatically
2. ✅ Images are embedded in the issue body or comments
3. ✅ No manual image URL handling needed

## Creating Issues from Excel

When processing issues from Excel files:

1. **Extract issues** from Excel (using `read_excel.py`)
2. **Identify associated images** (from `extracted_images/` folder)
3. **Create issue** with images automatically embedded (using `create_issue_with_images.py`)

## Manual Issue Creation with Images

### Option 1: Use the automated script
```bash
python create_issue_with_images.py "Title" "Description" "Tenacioustapes/https-yrya6ftzmg.wpdns.site-" image1.png image2.png
```

### Option 2: Add images to existing issue
```bash
python add_images_to_existing_issue.py 3 "Tenacioustapes/https-yrya6ftzmg.wpdns.site-" extracted_images/img1.png
```

## Image Processing

- Images are automatically uploaded to Imgur (anonymous, no account needed)
- Image URLs are embedded using Markdown syntax
- Images appear directly in the GitHub issue
- All images are preserved in the `extracted_images/` folder

## Best Practices

1. **Always include images** when they're mentioned in the Excel file
2. **Use descriptive filenames** for images to make mapping easier
3. **Check image associations** before creating issues
4. **Verify images embedded correctly** after issue creation

