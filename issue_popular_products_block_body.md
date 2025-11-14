# 🐛 Issue: "Popular Products" Block Still Showing on Category Parent Pages

## Summary

When clicking on a **parent category menu item** (e.g. **Double Sided Tapes**), a **"Popular Products"** section appears at the top of the category page.

This block shows featured products with "TOP 01 / TOP 02 / TOP 03 / TOP 04" badges.

This section was expected to be **removed from the design**, but it is still displaying.

## Location

- Parent category pages, e.g.:
  - `Double Sided Tapes` (and possibly other top-level tape categories)

## Expected

- No "Popular Products" row/section should appear at the top of parent category pages

**OR**

- If it must exist, it should only appear where explicitly agreed in the design (to be confirmed).

## Actual

- "Popular Products" block appears automatically at the top of the category content.
- Pushes real product listing further down the page.
- Creates confusion about whether these are curated promos vs. normal category results.

## Tasks

- [ ] Confirm whether "Popular Products" is meant to appear at all on category pages.
- [ ] If **not** intended → remove this block entirely from parent category templates.
- [ ] If only intended for specific pages → limit its display to those only.
- [ ] Clear any leftover Elementor/WooCommerce widgets or template parts that auto-inject this section.

## Details

**Area:** Category Pages / Product Display  
**Concern:** "Popular Products" block appearing on parent category pages when it should be removed.

**Assigned to:** Jordan FB

## Screenshot

![Popular Products block on Double Sided Tapes category page](https://i.imgur.com/ou6RONZ.jpeg)

