# -*- coding: utf-8 -*-


import unittest

from milkcocoa.milkcocoa import DataStore, Milkcocoa
from milkcocoa.keys_file_api import MilkCocoaKeys

from dumb_data_creation_scripts import delete_dumb_file, create_dumb_file


class TestDatastore(unittest.TestCase):

    def setUp(self):
        create_dumb_file()
        self.keys = MilkCocoaKeys(key_file_name='keys_dumb.ini')

    def tearDown(self):
        delete_dumb_file()

    def test_datastore_instance(self):
        credentials = self.keys.get_credentials()

        milkcocoa = Milkcocoa.connect(app_id=credentials.get('app_id'), useSSL=False)
        datastore = milkcocoa.datastore('dumb_python')

        self.assertIsNotNone(datastore)
        self.assertIsInstance(datastore, DataStore)
