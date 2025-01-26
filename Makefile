.PHONY: all install uninstall clean

BIN_DIR = /usr/local/bin
SCRIPT_DIR = ./.make

all: asciiconv

asciiconv: clean 
	@python3 -m venv venv && source venv/bin/activate
	@pip install PyInstaller Pillow
	@python3 -m PyInstaller main.py --onefile
	@mv ./dist/main ./asciiconv
install: asciiconv
	@mv asciiconv $(BIN_DIR)/

uninstall: clean
	@rm -f $(BIN_DIR)/asciiconv

clean:
	@rm -rf build dist __pycache__ main.spec asciiconv venv
