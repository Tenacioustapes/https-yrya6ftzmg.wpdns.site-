# 🐛 Issue: Product Appears in Application Guide but Does NOT Appear in Global Search Results

## What's happening

When viewing the Application Guide, the product **M543 – DS General Purpose Tissue** appears correctly in the list.

Clicking it from the Application Guide takes you to the correct product page.

**BUT** when searching for "M543" (or the product name) in the global site search, the product does not appear at all.

Instead, only pages like Application Guide and Home appear.

## Why this is a problem

- The product is published and publicly accessible, so it should exist in the search index.
- Customers searching by product code will not find it.
- Inconsistent behaviour:
  - → Appears in Application Guide
  - → Does NOT appear in global search

This suggests the product is being:
- Excluded from search queries
- OR Not indexed by the search engine
- OR Missing searchable custom fields (SKU field not mapped)
- OR Search is misconfigured to only return WooCommerce products of a specific type/category

## Expected behaviour

- The product should appear when searching M543, its SKU, or its product name.
- Search results should always include all published products.

## Details

**Area:** Search  
**Concern:** Product appears in Application Guide but does not appear in global search results.

**Example:**
- Product M543 shows correctly in the Application Guide and links to its product page.
- However, searching "M543" in the global search returns only pages (Application Guide, Home).
- Product does not appear as a search result despite being published.
- Expected: Product should appear in global search results for SKU, product code, or name.

**Assigned to:** Jordan FB

## Screenshots

**Screenshot 1: Product in Application Guide**
![Product in Application Guide](https://i.imgur.com/BOPdTBp.png)

**Screenshot 2: Product page accessible from Application Guide**
![Product page](https://i.imgur.com/iJRlMV8.png)

**Screenshot 3: Search results showing product is missing**
![Search results missing product](https://i.imgur.com/1evwy5A.png)

