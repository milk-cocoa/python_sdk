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

    with open(get_dumb_path(), 'w') as dumb_file:
        config_parser.write(dumb_file)


def delete_dumb_file():
    path = get_dumb_path()
    os.remove(path)


class ApiKeys(unittest.TestCase):

    def setUp(self):
        self.mkca_key = MilkCocoaKeys()
        create_dumb_file()

    def tearDown(self):
        delete_dumb_file()

    def test_instance(self):
        self.assertIsNotNone(self.mkca_key)
        self.assertIsInstance(self.mkca_key, MilkCocoaKeys)

    def test_has_good_header(self):
        pass

    def test_has_bad_header(self):
        pass

    def test_has_app_id(self):
        pass

    def test_has_access_key(self):
        pass

    def test_has_secret_key(self):
        pass


if __name__ == '__main__':
    unittest.main()
