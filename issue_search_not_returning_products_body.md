# 🐛 Issue: Search Does Not Return Products by SKU or General Terms

## Summary

The global search/autocomplete does **not** return products even when:

- The exact **SKU** is entered
- The product is **published** and **in stock**
- The product clearly exists in the WooCommerce product catalog

## Example

- **SKU:** T710TBH
- **Product:** Double Sided Foamed Acrylic – Bonding Tape
- **Search term entered:** `t710tbh`
- **Result:** **"No results found"**

Meanwhile, the product is visible in the admin product list with SKU correctly set to `T710TBH`.

## Expected

- Typing a product SKU (e.g. `T710TBH`) should return the matching product.
- General product terms (e.g. part of the product name) should also return the product.
- Search should include **WooCommerce products + their SKU fields**, not just pages/posts.

## Actual

- Search returns **no results** for valid SKUs.
- Search appears to only return certain pages (e.g. Application Guide, Home) and ignores products.
- This affects both autocomplete dropdown and full search results.

## Possible Causes (for developer)

- Search is configured to index **pages only**, not products.
- The SKU field is not included in the searchable fields.
- The search plugin (or theme search override) may be excluding product post type.
- Search index needs rebuilding after migration/import.

## Tasks

- [ ] Confirm which post types are being searched (pages vs products).
- [ ] Ensure WooCommerce products are included in search results.
- [ ] Include SKU field in search index so users can search by product code.
- [ ] Rebuild/refresh search index if required.
- [ ] Test multiple products (including T710TBH) to confirm SKUs and names return results as expected.

## Details

**Area:** Global Search  
**Concern:** Search does not return products when searching by SKU or product name.

**Example:**
- Product "Double Sided Foamed Acrylic – Bonding Tape" has SKU **T710TBH** and is published/in stock.
- Searching "t710tbh" shows "No results found".
- Expected: search includes WooCommerce products and SKU fields so products can be found by code or name.

**Assigned to:** Jordan FB

## Screenshots

**Screenshot 1: Product in Admin with SKU T710TBH**
![Product in admin showing SKU T710TBH](https://i.imgur.com/JrlAqdP.png)

**Screenshot 2: Search Result Showing "No results found"**
![Search showing no results for t710tbh](https://i.imgur.com/sWk1q91.png)

