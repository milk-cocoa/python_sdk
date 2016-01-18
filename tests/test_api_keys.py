# -*- coding: utf-8 -*-

import unittest

from milkcocoa.keys_file_api import MilkCocoaKeys
from milkcocoa.keys_file_api import OPTIONS

from dumb_data_creation_scripts import create_dumb_file, delete_dumb_file


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

    def test_read_key_file(self):
        content = self.mkca_key._read_key_file()
        self.assertIsNotNone(content)

        for option in OPTIONS:
            self.assertIn(option, content)

    def test_file_not_exists(self):
        self.mkca_key._path_api_key = 'dumb'

        with self.assertRaises(IOError):
            self.mkca_key._key_file_exists()


if __name__ == '__main__':
    unittest.main()
