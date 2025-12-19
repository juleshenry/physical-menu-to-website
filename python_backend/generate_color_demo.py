#!/usr/bin/env python3
"""
Generate a visual HTML demo showing the extracted colors from menu images.
"""
import os
from smart_color_fast import SmartColor
from css_generator import rgb_to_hex, get_text_color

def generate_color_demo_html(image_paths, output_path="color_demo.html"):
    """Generate an HTML page showing the extracted colors."""
    
    # Extract colors
    sc = SmartColor(image_paths, colors=4)
    colors = sc.global_colors()
    
    # Color names
    color_names = ["Primary", "Secondary", "Accent", "Background"]
    
    # Generate HTML
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Extracted Menu Colors Demo</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            margin-bottom: 10px;
        }
        .subtitle {
            color: #666;
            margin-bottom: 40px;
        }
        .color-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }
        .color-card {
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .color-preview {
            height: 150px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            font-weight: bold;
        }
        .color-info {
            padding: 15px;
            background: white;
        }
        .color-name {
            font-weight: bold;
            margin-bottom: 5px;
            color: #333;
        }
        .color-value {
            font-family: monospace;
            color: #666;
            font-size: 14px;
        }
        .demo-section {
            margin-top: 40px;
            padding: 30px;
            border-radius: 8px;
        }
        .demo-section h2 {
            margin-top: 0;
        }
        .button-demo {
            margin-top: 20px;
        }
        .btn {
            padding: 12px 24px;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
            margin-right: 10px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎨 Menu Color Palette</h1>
        <p class="subtitle">Colors automatically extracted from your menu photos</p>
        
        <div class="color-grid">
"""
    
    # Add color cards
    for i, (color, name) in enumerate(zip(colors, color_names)):
        hex_color = rgb_to_hex(color)
        text_color = get_text_color(color)
        
        html += f"""            <div class="color-card">
                <div class="color-preview" style="background-color: {hex_color}; color: {text_color};">
                    {name}
                </div>
                <div class="color-info">
                    <div class="color-name">{name} Color</div>
                    <div class="color-value">RGB: {color[0]}, {color[1]}, {color[2]}</div>
                    <div class="color-value">HEX: {hex_color}</div>
                </div>
            </div>
"""
    
    # Add demo sections
    primary_hex = rgb_to_hex(colors[0])
    primary_text = get_text_color(colors[0])
    secondary_hex = rgb_to_hex(colors[1])
    secondary_text = get_text_color(colors[1])
    accent_hex = rgb_to_hex(colors[2])
    accent_text = get_text_color(colors[2])
    
    html += f"""        </div>
        
        <div class="demo-section" style="background-color: {primary_hex}; color: {primary_text};">
            <h2>Navigation Bar Example</h2>
            <p>This is how your navigation bar will look with the primary color ({primary_hex})</p>
        </div>
        
        <div class="demo-section" style="background-color: {secondary_hex}; color: {secondary_text};">
            <h2>Content Section Example</h2>
            <p>Secondary sections use the second most prominent color ({secondary_hex})</p>
        </div>
        
        <div class="button-demo">
            <h2>Interactive Elements</h2>
            <button class="btn" style="background-color: {accent_hex}; color: {accent_text};">
                Accent Button
            </button>
            <button class="btn" style="background-color: {primary_hex}; color: {primary_text};">
                Primary Button
            </button>
            <button class="btn" style="background-color: {secondary_hex}; color: {secondary_text};">
                Secondary Button
            </button>
        </div>
        
        <div style="margin-top: 40px; padding: 20px; background: #f9f9f9; border-radius: 8px;">
            <h3>📋 Usage</h3>
            <p>These colors have been extracted from <strong>{len(image_paths)}</strong> menu images and applied to:</p>
            <ul>
                <li><code>web/index.css</code> - CSS variables and styles</li>
                <li>Navigation bars, buttons, and interactive elements</li>
                <li>Background colors and text colors with proper contrast</li>
            </ul>
            <p>The CSS uses modern CSS variables for easy customization:</p>
            <pre style="background: white; padding: 15px; border-radius: 4px; overflow-x: auto;">
--primary-color: {primary_hex};
--secondary-color: {secondary_hex};
--accent-color: {accent_hex};</pre>
        </div>
    </div>
</body>
</html>"""
    
    with open(output_path, 'w') as f:
        f.write(html)
    
    print(f"\n✓ Color demo generated: {output_path}")
    print(f"  Open this file in a browser to see the extracted colors in action!")
    return output_path

if __name__ == "__main__":
    # Get image paths
    roo = "examples/sabor-catracha"
    x = os.listdir(roo)
    ips = ["/".join((os.getcwd(), roo, y)) for y in x]
    
    # Generate demo
    demo_path = generate_color_demo_html(ips, output_path="../web/color_demo.html")
