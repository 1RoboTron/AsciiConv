import argparse
import os
from PIL import Image
from ascii_art import image_to_ascii
from config import load_language, save_language, load_language_strings
from utils import open_file

def main():
    language = load_language() or 'en'
    save_language(language)  
    lang_strings = load_language_strings(language)

    parser = argparse.ArgumentParser(description=lang_strings.get('description', 'ASCII-art Generator'))
    parser.add_argument('-l', '--lang', type=str, choices=['ru', 'en'], default=language, help='Choose Lang (ru/en)')
    parser.add_argument('image_path', type=str, nargs='?', help=lang_strings.get('image_path', 'Path to Image'))
    parser.add_argument('size', type=str, nargs='?', default=None, help='width,height(x,y)')
    parser.add_argument('-d', '--divide', type=str, default=None, help='Multiply or divide (for example, x3 and /3)')
    parser.add_argument('-inv', '--invert', action='store_false', help='Invert Color of Image')
    parser.add_argument('-op', '--open', action='store_true', help='Automatically open the created art')
    args = parser.parse_args()

    if args.lang:
        save_language(args.lang)

    if args.image_path is None:
        print(lang_strings.get('image_path', 'Path to Image'))
        print("If you need Help, use -h/--help")
        return

    try:
        image = Image.open(args.image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    original_width, original_height = image.size

    # Размеры, тут и получается волшебство
    if args.size:
        width, height = map(float, args.size.split(','))
        width, height = round(width), round(height)
    else:
        width = original_width // 4
        height = original_height // 4

    if args.divide:
        factor = float(args.divide[1:])
        if args.divide.startswith('x'):  # Умножить
            width = round(width * factor)
            height = round(height * factor)
        elif args.divide.startswith('/'):  # Делить
            width = round(width / factor)
            height = round(height / factor)

    ascii_art = image_to_ascii(args.image_path, output_size=(width, height), invert=args.invert)
    output_file = os.path.splitext(os.path.basename(args.image_path))[0] + '.txt'
    output_path = os.path.join(os.getcwd(), output_file)
    with open(output_path, "w") as f:
        f.write(ascii_art)
    print(lang_strings.get('ready', 'All done! ASCII art size: {width}x{height}').format(width=width, height=height))

    if args.open:
        open_file(output_path)

if __name__ == "__main__":
    main()
