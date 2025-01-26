#!/bin/sh
tar -xf venv.tar.xz && ./venv/bin/python -m PyInstaller --onefile main.py -n asciiconv && mv ./dist/asciiconv ./
