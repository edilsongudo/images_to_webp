from pathlib import Path
from PIL import Image
import os

def convert_to_webp(source):
    """Convert image to webp.

    Args:
        source (pathlib.Path): Path to source image

    Returns:
        pathlib.Path: path to new image
    """
    destination = os.path.splitext(source)[0] + '.webp' 

    image = Image.open(os.path.join('images', source))  # Open image
    image.save(os.path.join('output', destination), format="webp")  # Convert image to webp

    return destination


def main():
    images = os.listdir('images')
    for image in images:
        if os.path.splitext(image)[-1] in ('.png', '.jpeg', '.jpg'):
            webp_path = convert_to_webp(image)
            print(webp_path)

main()