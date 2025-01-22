#!/bin/bash

if make -f Makefile then
else
    if make -f Makefile_alt; then
    else
        echo "Ошибка при скачивании. Завершение работы."
        exit 1
    fi
fi

