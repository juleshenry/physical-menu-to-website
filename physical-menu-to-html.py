folder_of_menu_pictures = "folder"
desired_nav_bar_items = "a,b,c,d,e"

class PrintedMenuConverter:

    def __init__(self, pictures_dir):
        self.pictures_dir = pictures_dir
    
    
    def analyze_colors(self):
        """Consumes pictures and chooses top four colors; styles css accordingly"""
        pass

    def get_text_for_menu(self):
        """Consumes pictures and gets their text"""
        pass

    def convert_text_to_html(self):
        """Consumes menu text and converts it to html"""
        pass

if __name__=='__main__':
    pictures_folder = "examples/example"
    pmc = PrintedMenuConverter(pictures_folder)