import sys
from PIL import Image
import os

def resize_image(image, max_width=120):
    original_width, original_height = image.size[0], image.size[1]

    # ratio
    ratio = max_width / original_width
    
    # nuove dimensioni
    w_new = int(original_width * ratio)
    h_new = int(original_height * ratio * 0.55)

    resized_image = image.resize((w_new, h_new), Image.Resampling.LANCZOS)

    return resized_image


def image_to_ascii(image, characters):
    pixels = image.getdata()
    ascii_str = ""

    for pixel_value in pixels:
        ascii_str += characters[pixel_value * len(characters) // 256] # i dont know how it works :)

    return ascii_str
    

def main():
    characters: str = " .:-=+*#%@"

    '''
    if len(sys.argv) > 2:
        print(f"only accepted arg: {sys.argv[1]}") 
    '''

    if len(sys.argv) != 2:
        print("Usage: python main.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]

    if not os.path.exists(image_path): 
        print(f"The image {image_path} doesnt exists")

    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        sys.exit(1)

    resized_image = resize_image(image)
    # resized_image = resized_image.convert('L')
    # i passed the converted image directly to the conversion function
    ascii_art = image_to_ascii(resized_image.convert('L'), characters)

    width, height = resized_image.size

    for i in range(0, len(ascii_art), width):
        print(ascii_art[i:i+width])


if __name__ == '__main__':
    main()
