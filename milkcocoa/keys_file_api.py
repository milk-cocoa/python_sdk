# -*- coding: utf-8 -*-

try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import configparser


class MilkCocoaKeys(object):

    def __init__(self, path_api_key=None):
        self._path_api_key = path_api_key

