import subprocess
import platform

def open_file(file_path):
    if platform.system() == 'Darwin':  # macOS
        subprocess.call(['open', file_path])
    elif platform.system() == 'Windows':  # Windows
        os.startfile(file_path)
    else:  # Linux
        subprocess.call(['xdg-open', file_path])
#  Sorry TempleOS None

