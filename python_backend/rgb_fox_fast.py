# Import necessary libraries
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image
from typing import Tuple, List

"""
Fast version of rgb_fox that samples pixels for efficiency
"""
from pri import nt

print = nt


def get_prominent_colors(image_path: str, colors: int, sample_size: int = 10000) -> List[Tuple[int, int, int]]:
    """
    Extract prominent colors from an image using KMeans clustering on sampled pixels.
    
    Args:
        image_path: Path to the image file
        colors: Number of colors to extract
        sample_size: Number of pixels to sample (default 10000 for speed)
    
    Returns:
        List of RGB tuples representing the most prominent colors
    """
    print(f"Opening image: {image_path}")
    i = Image.open(image_path).convert("RGB")
    w, h = i.size
    total_pixels = w * h
    
    # Resize image if it's too large to make sampling more efficient
    max_dimension = 800
    if w > max_dimension or h > max_dimension:
        aspect = w / h
        if w > h:
            new_w = max_dimension
            new_h = int(max_dimension / aspect)
        else:
            new_h = max_dimension
            new_w = int(max_dimension * aspect)
        i = i.resize((new_w, new_h), Image.Resampling.LANCZOS)
        w, h = i.size
        total_pixels = w * h
    
    print(f"Image size: {w}x{h} = {total_pixels} pixels")
    
    # Convert to numpy array for efficient processing
    img_array = np.array(i)
    
    # Reshape to 2D array of pixels (each row is RGB)
    pixels = img_array.reshape(-1, 3)
    
    # Sample pixels if we have more than sample_size
    if len(pixels) > sample_size:
        print(f"Sampling {sample_size} pixels from {len(pixels)} total pixels")
        indices = np.random.choice(len(pixels), sample_size, replace=False)
        pixels = pixels[indices]
    
    print(f"Running KMeans with {colors} clusters on {len(pixels)} pixels")
    kmeans = KMeans(n_clusters=colors, random_state=42, n_init=10)
    kmeans.fit(pixels)
    
    # Get cluster centers and their frequencies
    labels = kmeans.labels_
    unique_labels, counts = np.unique(labels, return_counts=True)
    
    # Sort by frequency (most common first)
    sorted_indices = np.argsort(counts)[::-1]
    
    # Get colors sorted by frequency
    sorted_colors = []
    for idx in sorted_indices:
        label = unique_labels[idx]
        # Use cluster center as the representative color
        center = kmeans.cluster_centers_[label]
        color_tuple = tuple(map(int, center))
        sorted_colors.append(color_tuple)
        print(f"Color {len(sorted_colors)}: RGB{color_tuple} (frequency: {counts[idx]}/{len(pixels)})")
    
    return sorted_colors
