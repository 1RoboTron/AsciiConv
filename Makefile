.PHONY: all install uninstall clean

BIN_DIR = /usr/local/bin
SCRIPT_DIR = ./.make

all: asciiconv

asciiconv: clean
	@sh -c $(SCRIPT_DIR)/1.sh || sh -c $(SCRIPT_DIR)/2.sh || (echo "Installing Error!!!." && exit 1)

install: asciiconv
	@mv asciigen $(BIN_DIR)/

uninstall: clean
	@rm -f $(BIN_DIR)/asciiconv

clean:
	@rm -rf build dist __pycache__ asciiconv.spec asciiconv venv
