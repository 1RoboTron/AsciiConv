.PHONY: all install uninstall clean
all: asciiconv
asciiconv:
	tar -xf venv.tar.gz && ./venv/bin/python -m PyInstaller --onefile main.py -n asciiconv && mv ./dist/asciiconv ./
install: asciiconv
	@mv asciigen /usr/local/bin/
uninstall: clean
	@rm -f /usr/local/bin/asciiconv
clean:
	@rm -rf build dist __pycache__ asciiconv.spec asciiconv venv
