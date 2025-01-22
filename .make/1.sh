#!/bin/sh
tar -xf venv.tar.gz && ./venv/bin/python -m PyInstaller --onefile main.py -n asciiconv && mv ./dist/asciiconv ./
