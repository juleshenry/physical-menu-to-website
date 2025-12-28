# Python Backend

## Install

### macOS
```bash
brew install tesseract
brew install tesseract-lang
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get install tesseract-ocr tesseract-ocr-spa
```

### Python Dependencies
```bash
pip3 install pytesseract Pillow pandas matplotlib scikit-learn
```

## Testing

To run the text extraction tests:

```bash
cd python_backend
python3 test_get_text_from_menu.py
```

For detailed information about the test cases, see [TEST_README.md](TEST_README.md).