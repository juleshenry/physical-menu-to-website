import os
import sys

# Add python_backend to path so we can import from it
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'python_backend'))

from css_generator import generate_css_from_images

folder_of_menu_pictures = "folder"
desired_nav_bar_items = "a,b,c,d,e"

class PrintedMenuConverter:

    def __init__(self, pictures_dir):
        self.pictures_dir = pictures_dir
        self.image_paths = self._get_image_paths()
    
    def _get_image_paths(self):
        """Get list of image file paths from the pictures directory"""
        if not os.path.exists(self.pictures_dir):
            return []
        files = os.listdir(self.pictures_dir)
        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
        image_files = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]
        return [os.path.join(os.path.abspath(self.pictures_dir), f) for f in image_files]
    
    def analyze_colors(self):
        """Consumes pictures and chooses top four colors; styles css accordingly"""
        if not self.image_paths:
            print(f"No images found in {self.pictures_dir}")
            return None
        
        # Generate CSS from the menu images
        css_output_path = os.path.join(os.path.dirname(__file__), "web/index.css")
        css_content = generate_css_from_images(self.image_paths, num_colors=4, output_path=css_output_path)
        print(f"Generated CSS with colors from {len(self.image_paths)} menu images")
        print(f"CSS saved to: {css_output_path}")
        return css_content

    def get_text_for_menu(self):
        """Consumes pictures and gets their text"""
        pass

    def convert_text_to_html(self):
        """Consumes menu text and converts it to html"""
        pass

if __name__=='__main__':
    pictures_folder = "python_backend/examples/sabor-catracha"
    pmc = PrintedMenuConverter(pictures_folder)
    
    # Analyze colors and generate CSS
    print(f"\nAnalyzing colors from {len(pmc.image_paths)} images...")
    css = pmc.analyze_colors()
    
    if css:
        print("\n✓ CSS color generation complete!")
        print("The website colors are now based on the menu photos.")