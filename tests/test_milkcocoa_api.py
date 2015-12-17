# -*- coding: utf-8 -*-


import unittest

from milkcocoa.milkcocoa import Milkcocoa
from milkcocoa.keys_file_api import MilkCocoaKeys

from dumb_data_creation_scripts import delete_dumb_file, create_dumb_file


class TestMilkcocoaApi(unittest.TestCase):

    def setUp(self):
        create_dumb_file()
        self.keys = MilkCocoaKeys()

    def tearDown(self):
        delete_dumb_file()

    def test_milkcocoa_instance_connection_no_ssl(self):
        credentials = self.keys.get_credentials()

        milkcocoa = Milkcocoa.connect(app_id=credentials.get('app_id'), useSSL=False)
        self.assertIsNotNone(milkcocoa)
        self.assertIsInstance(milkcocoa, Milkcocoa)

    def test_milkcocoa_instace_connection_with_api_no_ssl(self):
        credentials = self.keys.get_credentials()

        milkcocoa = Milkcocoa.connectWithApiKey(app_id=credentials.get('app_id'),
                                                key=credentials.get('key'),
                                                secret=credentials.get('secret'),
                                                useSSL=False)
        self.assertIsNotNone(milkcocoa)
        self.assertIsInstance(milkcocoa, Milkcocoa)

if __name__ == '__main__':
    unittest.main()
