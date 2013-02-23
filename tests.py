#!/usr/local/bin/python
'''
Created on Dec 30, 2012

@author: ld
'''
import unittest
import cassandrawrite

class FakeValue(object):
    def __init__(self, values=None, plugin=None, plugin_instance=None,
                 host=None, type=None, type_instance=None, time=None):
        self.values = values or [2, 1]
        self.plugin = plugin or 'fake-plugin'
        self.plugin_instance = plugin_instance or 'fake-plugininstance'
        self.host = host or 'fake-host'
        self.type = type or 'fake-type'
        self.type_instance = type_instance or 'fake-type-i'
        self.time = time or 18124124124


class Test(unittest.TestCase):

    def test_single_value(self):
        vl = FakeValue()
        cassandrawrite.write(vl)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()


