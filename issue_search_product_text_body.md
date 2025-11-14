# 🐛 Issue: Search Result Shows Strange "(Product)" Text Under Listing

## What's happening

When searching for a product (e.g., "PT159"), the autocomplete search dropdown displays a strange line of text:

```
(Product)
```

This appears under the product description and looks like:
- A leftover taxonomy label
- A debug field
- An internal post type
- Or a misconfigured Elementor/WooCommerce meta field

This text is **not intended for customers** and looks unprofessional.

## Why it's an issue

- Confuses users because it provides no value
- The formatting is inconsistent with the rest of the UI
- Likely exposing internal post type slug or taxonomy name
- Reduces trust in the search feature

## Expected behaviour

Autocomplete results should only show:
- Product image
- Product title
- Short description (if needed)

There should be **no internal labels** or metadata visible.

## Details

**Area:** Search / Autocomplete  
**Concern:** Autocomplete result displays unintended "(Product)" text.

**Example:**
- When searching for "PT159", the dropdown shows a line "(Product)" beneath the description.
- This appears to be internal metadata (post type, taxonomy, or template leftover).
- Should not be visible to users.
- Expected: Only product image, title, and description in results.

**Assigned to:** Jordan FB

## Screenshot

![Search Result Showing (Product) Text](https://i.imgur.com/FNtSyiQ.png)

