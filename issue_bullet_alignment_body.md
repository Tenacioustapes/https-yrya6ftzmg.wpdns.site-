# 🐛 Issue: Bullet Point Text Alignment Incorrect in Features Section

## Summary

Bullet points in the Features section are rendering with incorrect indentation.

The second line of wrapped text is misaligned, starting under the bullet icon instead of beneath the first word.

## What's happening

- Multi-line bullet points are indented inconsistently.
- The second line of each bullet appears too far left.
- This causes the text to misalign vertically and makes the list difficult to read.

## Expected behaviour

- Wrapped lines should align directly under the first word of the bullet point text (standard HTML list formatting).
- The bullet icon should not affect indentation.
- CSS should apply proper list-style-position and padding so indentation is consistent.

## Visual Reference

**Actual (incorrect):**
- Second line sits under the bullet icon
- Uneven alignment across bullets

**Expected (correct):**
- Second line aligns under the first text word, not the bullet
- Clean and readable structure

## Possible cause

CSS override on:
- `ul li::marker`
- `padding-left`
- `text-indent`
- `list-style-position: inside` (likely incorrect)
- Theme or WooCommerce product template altering default list indentation.

## Details

**Area:** Styling – Product Page  
**Concern:** Bullet point alignment is incorrect for multi-line items.

**Example:**
- In the Features list, wrapped text lines start beneath the bullet icon instead of beneath the first text word.
- This creates uneven indentation across all list items.
- Expected: Wrapped lines align directly under the first word, following standard HTML list formatting.
- Likely caused by CSS on `ul li` or `list-style-position`.

**Assigned to:** Jordan FB

## Screenshot

![Bullet Point Alignment Issue](https://i.imgur.com/zkxwlLS.png)

