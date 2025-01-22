
import os
import json
import configparser

CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".cache", "ascii-gen")
CONFIG_FILE = os.path.join(CONFIG_DIR, "cache.conf")
LANG_FILE = os.path.join(CONFIG_DIR, "lang.conf")

DEFAULT_LANGUAGE = "en"

def create_default_config():
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

    # Создание cache.conf с дефолтными параметрами
    if not os.path.exists(CONFIG_FILE):
        config = {"LANG": DEFAULT_LANGUAGE}
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f)

    # Создание lang.conf с дефолтными параметрами
    if not os.path.exists(LANG_FILE):
        config = configparser.ConfigParser()
        config['ru'] = {
            'description': 'Говорю заранее, если не указать размеры, будет браться размеры ориг изображения и делиться на 4. Вот тебе пример : [user@unix]$ asciigen ~/Images/image.png -d x2 (то есть вы указываете, что нужно изображение по умолчанию делённое на 4, умножить на 2) [user@unix]$ art ~/Image/image.png 80,20',
            'image_path': 'Путь до картинки',
            'size': 'ШИРИНА,ВЫСОТА(x,y)',
            'divide': 'Умножить или разделить размер (например, x2 или /2)',
            'invert': 'Инвертировать цвета изображения',
            'open': 'Автоматически открыть созданный ASCII-арт',
            'ready': 'Всё готово! Размер ASCII-арта: {width}x{height}'
        }
        config['en'] = {
            'description': 'Please note, if you do not specify sizes, the original image sizes will be taken and divided by 4. Here is an example: [user@unix]$ asciigen ~/Images/image.png -d x2 (meaning you specify that the default image divided by 4 should be multiplied by 2) [user@unix]$ art ~/Image/image.png 80,20',
            'image_path': 'Path to the image',
            'size': 'WIDTH,HEIGHT(x,y)',
            'divide': 'Multiply or divide size (e.g., x2 or /2)',
            'invert': 'Invert image colors',
            'open': 'Automatically open the created ASCII art',
            'ready': 'All done! ASCII art size: {width}x{height}'
        }
        with open(LANG_FILE, "w") as f:
            config.write(f)

def load_language():
    create_default_config()  # Создание Дефолт Конфиг файла ,  если его нет
    if not os.path.exists(CONFIG_FILE):
        return None
    with open(CONFIG_FILE, "r") as f:
        config = json.load(f)
    return config.get("LANG")

def save_language(language):
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
    config = {"LANG": language}
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

def load_language_strings(language):
    if not os.path.exists(LANG_FILE):
        return {}
    config = configparser.ConfigParser()
    config.read(LANG_FILE)
    return {key: config[language][key] for key in config[language]}

