# -*- coding: utf-8 -*-

import os

try:
    from ConfigParser import ConfigParser as configparser
except ImportError:
    from configparser import configparser


CREDENTIALS_FOLDER_NAME = '.credentials'
CREDENTIALS_FILE_NAME = 'keys.ini'

SECTION_NAME = 'credentials'
OPTIONS = ['app_id', 'key', 'secret']


class MilkCocoaKeys(object):

    def __init__(self):
        self._path_api_key = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            '../' + os.path.join(CREDENTIALS_FOLDER_NAME, CREDENTIALS_FILE_NAME)
        )
        self._config_parser = configparser()

    def _key_file_exists(self):
        import os

        if not os.path.isfile(self._path_api_key):
            raise IOError

    def _read_key_file(self):
        return self._config_parser.read(self._path_api_key)

    def get_credentials(self):
        self._key_file_exists()

        return self._read_key_file()
