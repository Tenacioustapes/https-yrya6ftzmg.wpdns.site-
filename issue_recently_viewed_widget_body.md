# 🐛 Issue: "Recently Viewed" Widget Showing Incorrect/Unexpected Behaviour (Sidebar + Pricing)

## Summary

The Recently Viewed feature displays inconsistently across the site.

Some elements appear to be unintended, and others are showing incorrect information (such as pricing).

This issue consolidates all known problems.

## ✅ Sub-Issues / Tasks

### 1. Sidebar Recently Viewed – Possibly Unintended

- Confirm whether the left sidebar Recently Viewed widget is part of the intended design
- If NOT intended: Remove the sidebar widget entirely
- If it is intended: update it to match header behaviour (see below)

### 2. Sidebar Spelling Error

- Fix typo in sidebar heading:
  - "RENCENTLY VIEWED" → "RECENTLY VIEWED"
- (This becomes irrelevant if the sidebar is removed.)

### 3. Pricing Should Not Display Anywhere

- Remove pricing from sidebar Recently Viewed
- Ensure pricing is removed globally from all Recently Viewed widgets
- Confirm default behaviour = no price shown for any product in any Recently Viewed component

### 4. Product List Mismatch (Header vs Sidebar vs Category Sidebar)

- Sidebar Recently Viewed shows products A + B
- Header Recently Viewed shows different items
- Category-menu Recently Viewed (left side of product category pages) shows nothing
- Unify the data source so all intended Recently Viewed components use the same list (or remove the extras)

### 5. Left-Menu Category Recently Viewed – Should It Exist?

- Confirm whether Recently Viewed is intended to appear in category side menus at all
- If NOT intended → remove from category side menus
- If intended → connect to the correct data source used by the header widget

## 🔍 Examples Observed

- PVDF Membrane Butyl Tape appears in sidebar Recently Viewed with price
- PT159 Chromakey Cloth Matt Tape also shows in sidebar with price
- These same items do not appear in category sidebar Recently Viewed
- But appear in the header dropdown Recently Viewed
- Sidebar shows price (incorrect)
- Sidebar spelling wrong

## 📌 Expected Final Behaviour

- Only the intended Recently Viewed component(s) exist (likely just the header dropdown)
- All Recently Viewed components show identical, consistent product history
- No pricing is displayed
- No duplicate or ghost Recently Viewed elements remain
- Spelling is correct everywhere

## Details

**Area:** Widgets / Recently Viewed  
**Concern:** Recently Viewed widget showing inconsistent behavior, pricing, and spelling errors across multiple locations.

**Assigned to:** Jordan FB

## Screenshot

![Recently Viewed Widget Issues - Shows spelling error RENCENTLY and pricing display](https://i.imgur.com/M5kt1Ef.jpeg)

