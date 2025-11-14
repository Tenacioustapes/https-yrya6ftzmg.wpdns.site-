# 🐛 Issue: Valid Product Images Intermittently Fail to Upload (Server Load?)

## Summary

When uploading a **1024 × 1024 PNG** image, the system sometimes shows:

> "The server cannot process the image. This can happen if the server is busy or does not have enough resources to complete the task. Uploading a smaller image may help. Suggested maximum size is 2560 pixels."

This should **not** happen, as the image is well under the stated 2560px limit.

## Behaviour

- **Image:** `t710tbh_new.png`
- **Dimensions:** **1024 × 1024 px**, 96 dpi, 24-bit PNG
- Well within normal upload limits.

**Observed:**

- On first upload attempt, error appears as above.
- After refreshing the page and trying again, **the same file sometimes uploads successfully**.
- This suggests an **intermittent server load / resource issue**, not a genuine size/dimension problem.
- Error message always points to "maximum size 2560px", which is misleading in this case.

## Expected

- Valid images (e.g. 1024 × 1024 PNGs) should upload reliably without errors.
- If the server is out of resources, the error message should clearly indicate a **server/resource issue**, not imply the image is too large.

## Steps to Reproduce

1. Edit a product and go to the image upload area.
2. Upload `t710tbh_new.png` (1024 × 1024 PNG).
3. Observe: upload sometimes fails with the "server cannot process the image" error.
4. Refresh the page and try the **same file** again.
5. Observe: upload may now succeed.

## Suspected Cause

- Intermittent **server load / resource limits**:
  - PHP `memory_limit`, `post_max_size`, `upload_max_filesize`
  - GD/Imagick library running out of memory or timing out
- Error message is generic and misleading (points to size instead of server load).

## Tasks

- [ ] Check server error logs around the time of failed uploads.
- [ ] Confirm PHP memory and upload limits.
- [ ] Verify GD/Imagick configuration and any timeouts.
- [ ] Adjust limits or optimise image processing so 1024px PNGs always succeed.
- [ ] Update error message to differentiate between:
  - image too large vs
  - server/resource failure.

## Details

**Area:** Media / Image Uploads  
**Concern:** Valid product images (1024×1024 PNG) intermittently fail to upload due to server resource issues, with misleading error messages.

**Assigned to:** Jordan FB

## Screenshots

**Screenshot 1: Upload Error Message**
![Upload error showing server cannot process image](https://i.imgur.com/s5bWugb.jpeg)

**Screenshot 2: Image Properties (1024×1024, within limits)**
![Image properties showing 1024x1024 dimensions](https://i.imgur.com/uzczqNK.png)

