# -*- coding: utf-8 -*-

import unittest

from milkcocoa.keys_file_api import MilkCocoaKeys


class ApiKeys(unittest.TestCase):

    def setUp(self):
        self.mkca_key = MilkCocoaKeys()

    def tearDown(self):
        pass

    def test_instance(self):
        self.assertIsNotNone(self.mkca_key)
        self.assertIsInstance(self.mkca_key, MilkCocoaKeys)

    def test_file_exists(self):
        pass

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
