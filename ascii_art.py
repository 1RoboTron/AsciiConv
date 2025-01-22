from PIL import Image, ImageOps

def image_to_ascii(image_path, output_size, invert=True):  
    image = Image.open(image_path)
    image = image.resize(output_size)
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    if invert:
        image = ImageOps.invert(image)
    image = image.convert("L")
    ascii_chars = "@%#*+=-:.,"
    pixels = image.getdata()
    ascii_str = ''.join(ascii_chars[pixel * len(ascii_chars) // 256] for pixel in pixels)
    ascii_art = "\n".join(ascii_str[i:i + output_size[0]] for i in range(0, len(ascii_str), output_size[0]))  
    return ascii_art
