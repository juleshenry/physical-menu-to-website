from collections import Counter
import os, sys
import rgb_fox_fast as rgbf

"""
Fast version of SmartColor using optimized pixel sampling
"""
from pri import nt

print = nt


class SmartColor:
    COLORS: int = 4

    def __init__(s, image_paths, colors: int = 4):
        s.color_counter = Counter()
        s.image_paths = image_paths
        s.colors = colors

    def identify(s, image_path):
        # Extract #number of colors from the image, default is 4, the number for themes
        colors = rgbf.get_prominent_colors(image_path, s.colors)
        return Counter(colors)

    def global_colors(s):
        # Aggregate counters...
        if not hasattr(s, "g_c"):
            for image_path in s.image_paths:
                color_count = s.identify(image_path)
                print("counter for ", image_path, color_count)
                s.color_counter.update(color_count)
            s.g_c = [f[0] for f in s.color_counter.most_common(s.colors)]
        return s.g_c
