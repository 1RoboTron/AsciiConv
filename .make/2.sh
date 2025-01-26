#!/bin/sh
tar -xf venv_alt.tar.xz && ./venv/bin/python -m PyInstaller --onefile main.py -n asciiconv && mv ./dist/asciiconv ./
