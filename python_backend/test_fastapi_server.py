#!/usr/bin/env python3
"""
Simple test script to verify the FastAPI server endpoints work correctly.
"""

import requests
import json
import sys

def test_health_endpoint():
    """Test the health check endpoint."""
    try:
        response = requests.get("http://127.0.0.1:8000/")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "running"
        print("✓ Health endpoint test passed")
        return True
    except Exception as e:
        print(f"✗ Health endpoint test failed: {e}")
        return False

def test_process_images_endpoint_invalid():
    """Test the process-images endpoint with invalid path."""
    try:
        response = requests.post(
            "http://127.0.0.1:8000/process-images",
            json={"image_paths": ["/nonexistent/path.jpg"]}
        )
        # Should return 404 for nonexistent file
        assert response.status_code == 404
        print("✓ Process images endpoint (invalid path) test passed")
        return True
    except Exception as e:
        print(f"✗ Process images endpoint test failed: {e}")
        return False

def test_extract_colors_endpoint_invalid():
    """Test the extract-colors endpoint with invalid path."""
    try:
        response = requests.post(
            "http://127.0.0.1:8000/extract-colors",
            json={"image_paths": ["/nonexistent/path.jpg"]}
        )
        # Should return 404 for nonexistent file
        assert response.status_code == 404
        print("✓ Extract colors endpoint (invalid path) test passed")
        return True
    except Exception as e:
        print(f"✗ Extract colors endpoint test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("Testing FastAPI Backend Server\n" + "="*40)
    
    all_passed = True
    all_passed &= test_health_endpoint()
    all_passed &= test_process_images_endpoint_invalid()
    all_passed &= test_extract_colors_endpoint_invalid()
    
    print("\n" + "="*40)
    if all_passed:
        print("All tests passed! ✓")
        sys.exit(0)
    else:
        print("Some tests failed! ✗")
        sys.exit(1)

if __name__ == "__main__":
    try:
        import requests
    except ImportError:
        print("Error: requests library is required. Install with: pip install requests")
        sys.exit(1)
    
    main()
