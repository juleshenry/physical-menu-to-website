"""
CSS Generator Module
Generates CSS styles based on colors extracted from menu images.
"""
from typing import List, Tuple
try:
    from smart_color_fast import SmartColor
except ImportError:
    from smart_color import SmartColor


def rgb_to_hex(rgb: Tuple[int, int, int]) -> str:
    """Convert RGB tuple to hex color string."""
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])


def calculate_luminance(rgb: Tuple[int, int, int]) -> float:
    """Calculate relative luminance for WCAG contrast."""
    r, g, b = [x / 255.0 for x in rgb]
    # Apply gamma correction
    r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
    g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
    b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def get_text_color(bg_rgb: Tuple[int, int, int]) -> str:
    """Determine if white or black text should be used on a background color."""
    luminance = calculate_luminance(bg_rgb)
    # If background is dark, use white text; otherwise use black
    return "#ffffff" if luminance < 0.5 else "#000000"


def generate_css_from_colors(colors: List[Tuple[int, int, int]], output_path: str = None) -> str:
    """
    Generate CSS content using the extracted color palette.
    
    Args:
        colors: List of RGB tuples representing the color palette
        output_path: Optional path to write CSS file
        
    Returns:
        CSS content as string
    """
    if not colors or len(colors) < 4:
        raise ValueError("Need at least 4 colors for theme generation")
    
    # Assign colors to semantic roles
    # Most prominent color for primary elements
    primary_color = colors[0]
    # Second color for secondary elements
    secondary_color = colors[1]
    # Third color for accents
    accent_color = colors[2]
    # Fourth color for backgrounds or borders
    background_color = colors[3]
    
    # Convert to hex
    primary_hex = rgb_to_hex(primary_color)
    secondary_hex = rgb_to_hex(secondary_color)
    accent_hex = rgb_to_hex(accent_color)
    background_hex = rgb_to_hex(background_color)
    
    # Determine appropriate text colors
    primary_text = get_text_color(primary_color)
    secondary_text = get_text_color(secondary_color)
    
    css_content = f"""/* Auto-generated CSS from menu image colors */

:root {{
    --primary-color: {primary_hex};
    --secondary-color: {secondary_hex};
    --accent-color: {accent_hex};
    --background-color: {background_hex};
    --primary-text: {primary_text};
    --secondary-text: {secondary_text};
}}

.preFade {{
    opacity: 0;
    transition-property: opacity;
}}

.fadeIn:not([data-override-initial-global-animation]) {{
    opacity: 1 !important;
}}

/* Navigation bar styling with primary color */
.bg-gray-800 {{
    background-color: var(--primary-color) !important;
    color: var(--primary-text);
}}

/* Secondary elements */
.bg-gray-700 {{
    background-color: var(--secondary-color) !important;
    color: var(--secondary-text);
}}

/* Link hover effects with accent color */
a:hover {{
    color: var(--accent-color) !important;
}}

/* Text color overrides */
.text-white {{
    color: var(--primary-text);
}}

.text-gray-300 {{
    color: var(--primary-text);
    opacity: 0.8;
}}

/* Button and interactive elements */
button {{
    background-color: var(--accent-color);
}}

button:hover {{
    background-color: var(--secondary-color);
}}

@media (max-width: 640px) {{
    .navbar-menu {{
        display: none;
        background-color: var(--primary-color);
    }}
    .navbar-menu.active {{
        display: block;
        background-color: var(--primary-color);
    }}
}}
"""
    
    if output_path:
        with open(output_path, 'w') as f:
            f.write(css_content)
    
    return css_content


def generate_css_from_images(image_paths: List[str], num_colors: int = 4, 
                             output_path: str = None) -> str:
    """
    Extract colors from images and generate CSS.
    
    Args:
        image_paths: List of paths to menu images
        num_colors: Number of colors to extract (default 4)
        output_path: Optional path to write CSS file
        
    Returns:
        Generated CSS content
    """
    # Use SmartColor to extract colors
    sc = SmartColor(image_paths, colors=num_colors)
    colors = sc.global_colors()
    
    return generate_css_from_colors(colors, output_path)


if __name__ == "__main__":
    import os
    import sys
    
    # Example usage
    roo = "examples/sabor-catracha"
    x = os.listdir(roo)
    ips = ["/".join((os.getcwd(), roo, y)) for y in x]
    
    css = generate_css_from_images(ips, output_path="../web/index.css")
    print("Generated CSS:")
    print(css)
