# 🐛 Issue: Sidebar Shows Incorrect Product Category Filters for Current Page

## Summary

When viewing certain **single-sided tape** related pages (e.g. tag page **"SS Joining, Sealing & Repair"**), the left-hand sidebar **Product Categories** menu shows categories that don't match the user's current context.

## Example

- User is effectively in a **Single Sided** context
- Sidebar still shows **Double Sided Tapes**, **Safety Tapes**, **Other Products** etc.
- In some cases, a user can click a single-sided category but the sidebar continues to show **double-sided filters**, which is confusing.

This makes it unclear which range the user is actually filtering and browsing.

## Expected

- Sidebar filters should match the **current range or context**.
- If user is in a **Single Sided** context:
  - Only relevant single-sided categories/filters should be shown.
- Cross-range filters (e.g. Double Sided when browsing Single Sided) should not appear unless explicitly required by design.

## Actual

- Sidebar displays a **global product category tree** (Single Sided, Double Sided, Safety, Other Products) regardless of the user's current range/tag.
- Users can be on a Single Sided-related page while still seeing Double Sided filters in the sidebar.
- This creates the impression that they're filtering single-sided products, but the UI suggests multiple ranges at once.

## Tasks

- [ ] Confirm intended behaviour for sidebar filters on:
  - Tag pages (e.g. "SS Joining, Sealing & Repair")
  - Single Sided vs Double Sided vs Safety ranges
- [ ] Update sidebar widget/template logic so that category filters:
  - Reflect only the relevant range/context
  - Or clearly distinguish cross-range navigation if that's desired
- [ ] Test with several Single Sided and Double Sided pages to ensure filters always match the current page context.

## Details

**Area:** Sidebar – Product Categories / Filters  
**Concern:** Sidebar shows product categories and filters that do not match the current range/context.

**Example:**
- On the "SS Joining, Sealing & Repair" page (Single Sided context), the left sidebar shows categories for Single Sided, Double Sided, Safety Tapes and Other Products all together.
- A user who clicks Single Sided Tapes still sees Double Sided options in the sidebar, which should not appear there.
- Expected: sidebar filters reflect only the relevant range (e.g. Single Sided) for the current page, or are clearly separated.

**Assigned to:** Jordan FB

## Screenshot

![Sidebar showing incorrect category filters on SS Joining, Sealing & Repair page](https://i.imgur.com/57sFDsE.jpeg)

