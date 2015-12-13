# -*- coding: utf-8 -*-

import unittest
import os
try:
    from ConfigParser import ConfigParser as configparser
except ImportError:
    from configparser import configparser

from milkcocoa.keys_file_api import MilkCocoaKeys
from milkcocoa.keys_file_api import CREDENTIALS_FOLDER_NAME, SECTION_NAME, OPTIONS


DUMB_OPTIONS_VALUES = ['vuei9dh5mu3', '57P5lBcZny6AlQEn', 'DM66u0smok1BUjHAZlU9T57kBcQUv5OKIFMkvTQ1']


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


class ApiKeys(unittest.TestCase):

    def setUp(self):
        create_dumb_file()
        self.mkca_key = MilkCocoaKeys(key_file_name='keys_dumb.ini')

    def tearDown(self):
        delete_dumb_file()

    def test_instance(self):
        self.assertIsNotNone(self.mkca_key)
        self.assertIsInstance(self.mkca_key, MilkCocoaKeys)

    def test_has_app_id(self):
        credentials = self.mkca_key.get_credentials()
        self.assertIn('app_id', credentials)

    def test_has_access_key(self):
        credentials = self.mkca_key.get_credentials()
        self.assertIn('key', credentials)

    def test_has_secret_key(self):
        credentials = self.mkca_key.get_credentials()
        self.assertIn('secret', credentials)


if __name__ == '__main__':
    unittest.main()
