# -*- coding: utf-8 -*-

import os

try:
    from ConfigParser import ConfigParser as configparser
except ImportError:
    from configparser import ConfigParser as configparser


CREDENTIALS_FOLDER_NAME = '.credentials'
CREDENTIALS_FILE_NAME = 'keys.ini'

SECTION_NAME = 'credentials'
OPTIONS = ['app_id', 'key', 'secret']

__all__ = [
    'MilkCocoaKeys'
]


class MilkCocoaKeys(object):

    def __init__(self, key_file_name=None):
        self.__file_name = CREDENTIALS_FILE_NAME if not key_file_name else key_file_name
        self._path_api_key = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            '../' + os.path.join(CREDENTIALS_FOLDER_NAME, self.__file_name)
        )
        self._config_parser = configparser()

    def _key_file_exists(self):
        import os

        if not os.path.isfile(self._path_api_key):
            raise IOError('File %s not found' % self._path_api_key)

    def _read_key_file(self):
        self._config_parser.read(self._path_api_key)
        options = self._config_parser.options(SECTION_NAME)
        content = {}

        for option in options:
            content[option] = self._config_parser.get(SECTION_NAME, option)
        return content

    def get_credentials(self):
        self._key_file_exists()

        return self._read_key_file()
