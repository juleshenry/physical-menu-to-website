#!/usr/bin/env python3
"""
Test script for CSS color generation from menu images.
"""
import os
from smart_color import SmartColor
from css_generator import generate_css_from_images

def main():
    # Get image paths
    roo = "examples/sabor-catracha"
    x = os.listdir(roo)
    ips = ["/".join((os.getcwd(), roo, y)) for y in x]
    
    print(f"Found {len(ips)} images: {[os.path.basename(ip) for ip in ips]}")
    
    # Extract colors
    print("\n=== Extracting colors from images ===")
    sc = SmartColor(ips, colors=4)
    colors = sc.global_colors()
    
    print(f"\nExtracted {len(colors)} colors:")
    for i, color in enumerate(colors, 1):
        hex_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
        print(f"  {i}. RGB{color} -> {hex_color}")
    
    # Generate CSS
    print("\n=== Generating CSS ===")
    css_output_path = os.path.join(os.path.dirname(__file__), "../web/index.css")
    css_content = generate_css_from_images(ips, num_colors=4, output_path=css_output_path)
    
    print(f"\nCSS generated successfully!")
    print(f"Output file: {css_output_path}")
    print(f"\nPreview of generated CSS variables:")
    for line in css_content.split('\n')[2:11]:  # Show the :root section
        print(line)

if __name__ == "__main__":
    main()
