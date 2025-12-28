# Text Extraction Test Cases

This document describes the test cases for extracting text from menu images using OCR (Optical Character Recognition).

## Overview

The `test_get_text_from_menu.py` script provides comprehensive tests for the menu text extraction functionality implemented in the `SmartMenu` class.

## Prerequisites

Before running the tests, ensure the following dependencies are installed:

```bash
# Install Tesseract OCR engine
brew install tesseract         # macOS
brew install tesseract-lang    # Language packs for macOS
# OR
sudo apt-get install tesseract-ocr tesseract-ocr-spa  # Linux

# Install Python packages
pip3 install pytesseract Pillow pandas matplotlib scikit-learn
```

## Test Cases

The test script includes the following test cases:

### 1. `test_identify_pure()`
Tests the `identify_pure()` function with a single menu image from the sabor-catracha example directory.

**What it tests:**
- Basic OCR functionality
- Text extraction from a single image
- Proper handling of rotated images (180 degrees)
- Spanish language text recognition

**Expected output:**
- Extracted text length
- Preview of extracted text (first 200 characters)

### 2. `test_smart_menu_sabor_catracha()`
Tests the `SmartMenu` class with all images from the sabor-catracha restaurant menu.

**What it tests:**
- Processing multiple menu images
- `SmartMenu.get_html_body()` method
- Batch text extraction
- Result aggregation

**Expected output:**
- Number of images processed
- Text length for each image
- Preview of extracted text from each image

### 3. `test_smart_menu_happypocha()`
Tests the `SmartMenu` class with images from the happypocha restaurant menu.

**What it tests:**
- Processing a different set of menu images
- Consistency of text extraction across different menu formats
- Handling of various image formats (JPEG)

**Expected output:**
- Number of images processed
- Text length for first 3 images
- Preview of extracted text

### 4. `test_associate_prices_to_text()`
Tests the `associate_prices_to_text()` method which extracts menu items with their prices.

**What it tests:**
- Price detection from extracted text
- Association of prices with menu items
- Parsing of menu structure
- Numeric value extraction

**Expected output:**
- Number of images with price data
- Number of price entries per image
- Sample of extracted prices and associated text

## Running the Tests

Navigate to the `python_backend` directory and run:

```bash
cd python_backend
python3 test_get_text_from_menu.py
```

## Test Results

All tests should pass with output similar to:

```
============================================================
Testing Text Extraction from Menu Images
============================================================

=== Testing identify_pure function ===
✓ PASSED

=== Testing SmartMenu with sabor-catracha examples ===
✓ PASSED

=== Testing SmartMenu with happypocha examples ===
✓ PASSED

=== Testing associate_prices_to_text ===
✓ PASSED

============================================================
Test Summary
============================================================
identify_pure: ✓ PASSED
smart_menu_sabor_catracha: ✓ PASSED
smart_menu_happypocha: ✓ PASSED
associate_prices_to_text: ✓ PASSED

Total: 4/4 tests passed
```

## Example Images

The tests use menu images from two example directories:

1. **sabor-catracha**: 5 menu images (0.jpg, 1.jpg, 4.jpg, 7.jpg, 9.jpg)
   - Honduran restaurant menu
   - Spanish language text
   - Includes prices and descriptions

2. **happypocha**: 10 menu images (IMG_1300.jpeg through IMG_1312.jpeg)
   - Korean restaurant menu
   - Mixed language text
   - Various menu sections

## Notes

- OCR accuracy depends on image quality, contrast, and text clarity
- The `identify_pure()` function uses caching via the `@kash` decorator to avoid re-processing the same images
- Spanish language support is enabled via `lang="spa"` parameter in pytesseract
- Images are rotated 180 degrees before processing for optimal text recognition

## Troubleshooting

**Issue**: `ModuleNotFoundError: No module named 'pytesseract'`
- **Solution**: Install pytesseract: `pip3 install pytesseract`

**Issue**: `TesseractNotFoundError`
- **Solution**: Install Tesseract OCR engine (see Prerequisites)

**Issue**: Poor text extraction quality
- **Solution**: Check image quality, ensure proper lighting and contrast
- Try adjusting rotation angle in `identify_pure()` function
- Consider preprocessing images (resize, enhance contrast)

## Future Improvements

Potential enhancements for the test suite:
- Add unit tests with known expected outputs
- Measure OCR accuracy against ground truth
- Test with different image formats and resolutions
- Add performance benchmarks
- Test error handling with corrupted images
