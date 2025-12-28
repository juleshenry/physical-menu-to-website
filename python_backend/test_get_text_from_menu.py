#!/usr/bin/env python3
"""
Test script for extracting text from menu images using SmartMenu class.
This script tests the OCR functionality on example menu images.
"""
import os
import sys
import traceback
from smart_menu import SmartMenu, identify_pure
from PIL import Image


def test_identify_pure():
    """Test the identify_pure function with a single image"""
    print("\n=== Testing identify_pure function ===")
    
    # Test with sabor-catracha examples
    example_dir = "examples/sabor-catracha"
    if os.path.exists(example_dir):
        images = [f for f in os.listdir(example_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
        if images:
            test_image = os.path.join(example_dir, images[0])
            print(f"\nTesting with image: {test_image}")
            try:
                text = identify_pure(test_image)
                print(f"Extracted text length: {len(text)} characters")
                print(f"First 200 characters: {text[:200]}...")
                return True
            except Exception as e:
                print(f"Error: {e}")
                return False
    return False


def test_smart_menu_sabor_catracha():
    """Test SmartMenu with sabor-catracha example images"""
    print("\n=== Testing SmartMenu with sabor-catracha examples ===")
    
    example_dir = "examples/sabor-catracha"
    if not os.path.exists(example_dir):
        print(f"Directory {example_dir} does not exist")
        return False
    
    # Get list of image files
    images = [f for f in os.listdir(example_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
    image_paths = [os.path.join(example_dir, img) for img in images]
    
    if not image_paths:
        print(f"No images found in {example_dir}")
        return False
    
    print(f"Found {len(image_paths)} images: {images}")
    
    try:
        # Create SmartMenu instance
        sm = SmartMenu(image_paths)
        
        # Extract text from images
        print("\nExtracting text from images...")
        body = sm.get_html_body()
        
        # Display results
        print(f"\nSuccessfully processed {len(body)} images")
        for filename, text in body.items():
            print(f"\n--- {filename} ---")
            print(f"Text length: {len(text)} characters")
            print(f"First 150 characters: {text[:150]}...")
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        return False


def test_smart_menu_happypocha():
    """Test SmartMenu with happypocha example images"""
    print("\n=== Testing SmartMenu with happypocha examples ===")
    
    example_dir = "examples/happypocha"
    if not os.path.exists(example_dir):
        print(f"Directory {example_dir} does not exist")
        return False
    
    # Get list of image files
    images = [f for f in os.listdir(example_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
    image_paths = [os.path.join(example_dir, img) for img in images]
    
    if not image_paths:
        print(f"No images found in {example_dir}")
        return False
    
    print(f"Found {len(image_paths)} images: {images[:5]}...")  # Show first 5
    
    try:
        # Create SmartMenu instance
        sm = SmartMenu(image_paths)
        
        # Extract text from images
        print("\nExtracting text from images...")
        body = sm.get_html_body()
        
        # Display results
        print(f"\nSuccessfully processed {len(body)} images")
        for filename, text in list(body.items())[:3]:  # Show first 3
            print(f"\n--- {filename} ---")
            print(f"Text length: {len(text)} characters")
            print(f"First 150 characters: {text[:150]}...")
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        return False


def test_associate_prices_to_text():
    """Test the associate_prices_to_text method"""
    print("\n=== Testing associate_prices_to_text ===")
    
    example_dir = "examples/sabor-catracha"
    if not os.path.exists(example_dir):
        print(f"Directory {example_dir} does not exist")
        return False
    
    images = [f for f in os.listdir(example_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
    image_paths = [os.path.join(example_dir, img) for img in images[:2]]  # Test with first 2 images
    
    if not image_paths:
        print(f"No images found in {example_dir}")
        return False
    
    try:
        sm = SmartMenu(image_paths)
        sm.get_html_body()
        
        print("\nAttempting to extract prices from text...")
        file_price_text = sm.associate_prices_to_text()
        
        print(f"\nExtracted price data from {len(file_price_text)} images")
        for filename, price_dict in file_price_text.items():
            print(f"\n--- {filename} ---")
            print(f"Found {len(price_dict)} price entries")
            # Show first few entries
            for price, text in list(price_dict.items())[:3]:
                print(f"  ${price}: {text[:50]}...")
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        return False


def main():
    """Run all test cases"""
    print("=" * 60)
    print("Testing Text Extraction from Menu Images")
    print("=" * 60)
    
    # Change to the script's directory to ensure relative paths work correctly
    script_dir = os.path.dirname(os.path.abspath(__file__))
    original_dir = os.getcwd()
    os.chdir(script_dir)
    
    try:
        results = {
            "identify_pure": test_identify_pure(),
            "smart_menu_sabor_catracha": test_smart_menu_sabor_catracha(),
            "smart_menu_happypocha": test_smart_menu_happypocha(),
            "associate_prices_to_text": test_associate_prices_to_text(),
        }
        
        # Summary
        print("\n" + "=" * 60)
        print("Test Summary")
        print("=" * 60)
        for test_name, passed in results.items():
            status = "✓ PASSED" if passed else "✗ FAILED"
            print(f"{test_name}: {status}")
        
        total_tests = len(results)
        passed_tests = sum(results.values())
        print(f"\nTotal: {passed_tests}/{total_tests} tests passed")
        
        return 0 if all(results.values()) else 1
    finally:
        # Restore the original working directory
        os.chdir(original_dir)


if __name__ == "__main__":
    sys.exit(main())
