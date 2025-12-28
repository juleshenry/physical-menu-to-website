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
pip3 install -r requirements.txt
```

Or install manually:
```bash
pip3 install pytesseract Pillow pandas matplotlib scikit-learn fastapi uvicorn
```

## FastAPI Server

The backend now runs as a FastAPI server that is spawned automatically by the Electron application.

### Running the Server Standalone

You can also run the FastAPI server independently for testing:

```bash
cd python_backend
python3 fastapi_server.py --port 8000
```

The server provides the following endpoints:
- `GET /` - Health check endpoint
- `POST /process-images` - Process menu images to extract text
- `POST /extract-colors` - Extract prominent colors from images

## Testing

To run the text extraction tests:

```bash
cd python_backend
python3 test_get_text_from_menu.py
```

For detailed information about the test cases, see [TEST_README.md](TEST_README.md).