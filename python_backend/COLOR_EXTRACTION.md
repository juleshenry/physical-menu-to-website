# Color Extraction and CSS Generation

This module automatically extracts colors from menu photos and generates CSS stylesheets with those colors.

## How It Works

1. **Color Extraction**: Uses K-Means clustering to identify the 4 most prominent colors in menu images
2. **Smart Sampling**: Processes a sample of pixels for efficiency (10,000 pixels per image)
3. **CSS Generation**: Creates CSS variables and styles based on the extracted color palette
4. **Automatic Text Color**: Determines whether white or black text should be used based on background luminance

## Files

- `rgb_fox_fast.py` - Optimized color extraction using pixel sampling
- `smart_color_fast.py` - Aggregates colors across multiple images
- `css_generator.py` - Generates CSS from color palette
- `test_color_css.py` - Test script for color extraction

## Usage

### Command Line

```bash
cd python_backend
python3 physical-menu-to-html.py
```

### Programmatic

```python
from css_generator import generate_css_from_images

# Extract colors and generate CSS from menu images
image_paths = ["menu1.jpg", "menu2.jpg"]
css = generate_css_from_images(image_paths, num_colors=4, output_path="output.css")
```

### As Part of Menu Conversion

```python
from physical_menu_to_html import PrintedMenuConverter

pmc = PrintedMenuConverter("path/to/menu/photos")
pmc.analyze_colors()  # Generates CSS at web/index.css
```

## Generated CSS

The CSS includes:

- **CSS Variables** in `:root` for easy theming:
  - `--primary-color`: Most prominent color (navigation bars)
  - `--secondary-color`: Second color (secondary elements)
  - `--accent-color`: Third color (hover effects, buttons)
  - `--background-color`: Fourth color (backgrounds)
  - `--primary-text`: Computed text color for primary elements
  - `--secondary-text`: Computed text color for secondary elements

- **Style Overrides** for Tailwind CSS classes to use the extracted colors

## Example

For a menu with colors:
- Dark brown/black: `#0f0100`
- Tan/beige: `#c7c1a9`
- Dark gray: `#3c373d`
- Medium gray: `#76757d`

The generated CSS will:
- Use dark brown for navigation bars with white text
- Use tan for secondary sections with dark text
- Use dark gray for hover effects
- Use medium gray for backgrounds

## Performance

- **Fast**: Processes 5 images (~13MP total) in ~2 minutes
- **Efficient**: Samples 10,000 pixels per image instead of processing all pixels
- **Scalable**: Can handle any number of images
