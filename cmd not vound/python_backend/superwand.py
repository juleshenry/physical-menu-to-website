from PIL import Image, ImageDraw, ImageFont
from collections import Counter
import os, sys
from rgb_fox import get_prominent_colors

"""
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,**:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:***:`:,:`:,:`:,:`:,:`:,*********`:,:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:***:`:,:`:,:`:,:`:,:`:************,:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:***:`:,:`:,:`:,:`:,:`*************,:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`**************:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:*****:,**:*****:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:****`:,**:,****:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:***:`:,:`:,:`:,:`:,:****`:,**:,:`:,:`:,:`:,:`:,:`:,:`***`********:,
`:,:***:`:,:`:,:`:,:`:,:*****:,**:,:`:,:`:,:`:,:`:,:`:,:`*************,
`:,:***:`:,:`:,:`:,:`:,:`********:,:`:,:`:,:`:,:`:,:`:,:`**************
`:,:***:`:,:`:,:`:,:`:,:`*********,:`:,:`:,:`:,:`:,:`:,:`**************
`:,:***:`:,:`:,:`:,:`:,:`:**********`:,:`:,:`:,:`:,:`:,:`*****,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,***********,:`:,:`:,:`:,:`:,:`****:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`**********:`:,:`:,:`:,:`:,:`****:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`:,********:`:,:`:,:`:,:`:,:`****:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`:,**:,*****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`:,**:,:****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:****`:,**:,:****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:****`:,**:,:****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:*****:,**:,*****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:***************:`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`**************:`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:************,:`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,**********:,:`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`:,**:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,****:`:,:`:,:`:,:`:,:`:,:`:,**:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:*****:`:,:`:,:`:,:`:,:`:,:`:,**:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
*******:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
*******:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
******,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,'
"""
from pri import nt

print = nt


def create_folder(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        # If it doesn't exist, create it
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created successfully.")
    else:
        print(f"Folder '{folder_path}' already exists.")


def get_prominent_colors_colorgram(image_path, number=64):
    from colorgram import extract

    # Extract #number of colors from the image, default is 4, the number for themes
    colors = extract(image_path, number)
    # Count the occurrences of each color
    color_counter = Counter((color.rgb.r, color.rgb.g, color.rgb.b) for color in colors)
    # Get the four most common colors
    prominent_colors = color_counter.most_common(number)
    return [pc[0] for pc in prominent_colors]


def make_theme_splash(ct, folder="themes_jpgs", colors=""):
    square_size, header_height = 32, 30

    # ct:= {str_theme1: [(r,g,b,), ...]}
    for t, t_colors in ct.items():
        # Calculate the width of the image
        print(t, t_colors)
        img_width = square_size * len(t_colors)

        # Create a new blank image with header
        img = Image.new(
            "RGB", (img_width, square_size + header_height), color=(255, 255, 255)
        )

        # Draw the header with centered text
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        text_width, text_height = font.getlength(t), 12
        text_x = (img_width - text_width) // 2
        text_y = (header_height - text_height) // 2
        draw.text((text_x, text_y), t, fill=(0, 0, 0), font=font)

        # Draw squares with the specified colors
        draw = ImageDraw.Draw(img)
        for i, color in enumerate(t_colors):
            draw.rectangle(
                [
                    (i * square_size, header_height),
                    ((i + 1) * square_size, header_height + square_size),
                ],
                fill=color,
            )

        # Display the image
        if not os.path.exists(f"{folder}"):
            create_folder(folder)
        img.save(f"{folder}/{t}_color_map.jpg")


def counter_to_color_theme(ix, c):
    return {ix: list(c.keys())}


if __name__ == "__main__":
    roo = "examples/sabor-catracha"
    ips = ["/".join((os.getcwd(), roo, y,)) for y in os.listdir(roo)]
    _p_ = {"colors": 32}
    pcs = []
    for ix, i in enumerate(ips):
        pcs = get_prominent_colors(i, **_p_)
        make_theme_splash({str(ix): pcs}, folder="_newest_tests", **_p_)
