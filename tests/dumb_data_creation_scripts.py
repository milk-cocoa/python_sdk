# -*- coding: utf-8 -*-

import os
try:
    from ConfigParser import ConfigParser as configparser
except ImportError:
    from configparser import ConfigParser as configparser

from milkcocoa.keys_file_api import CREDENTIALS_FOLDER_NAME, SECTION_NAME, OPTIONS

DUMB_OPTIONS_VALUES = ['vuei9dh5mu3', '57P5lBcZny6AlQEn', 'DM66u0smok1BUjHAZlU9T57kBcQUv5OKIFMkvTQ1']

__all__ = [
    'get_dumb_path', 'create_dumb_file', 'delete_dumb_file'
]


def get_dumb_path():
    path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        '../' + os.path.join(CREDENTIALS_FOLDER_NAME, 'keys_dumb.ini')
    )

    return path


def create_dumb_file():
    config_parser = configparser()
    config_parser.add_section(SECTION_NAME)

    for option, dumb_value in zip(OPTIONS, DUMB_OPTIONS_VALUES):
        config_parser.set(SECTION_NAME, option, dumb_value)

    directory_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../' + CREDENTIALS_FOLDER_NAME)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    with open(get_dumb_path(), 'w') as dumb_file:
        config_parser.write(dumb_file)


def delete_dumb_file():
    path = get_dumb_path()
    os.remove(path)
