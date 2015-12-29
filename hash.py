# -*- coding: utf-8 -*-

import unittest
import hashlib


class HashTable:

    def __init__(self, size):
        self.table = [[]] * size

    def put(self, key, value):
        hash = self.hash(key)
        table_row = self.table[hash]

        if any(map(lambda x: x[0] is key, table_row)):
            raise KeyError

        self.table[hash].append((key, value))

    def exists(self, key):
        hash = self.hash(key)

        if len(self.table[hash]) is not 0:
            return any(map(lambda x: x[0] is key, self.table[hash]))

        return False

    def get(self, key):
        hash = self.hash(key)

        for element_key, value in self.table[hash]:
            if key is element_key:
                return value

        raise KeyError()

    def hash(self, key):
        hash_object = hashlib.md5(key)

        return int(hash_object.hexdigest(), 16) % len(self.table)


class HashTableTest(unittest.TestCase):

    def setUp(self):
        self.table = HashTable(31)

    def test_hash(self):
        test_set = ['toto', 'totoro', 'miyazaki', 'endeavour', 'google']

        for e in test_set:
            hash = self.table.hash(e)
            self.assertGreaterEqual(hash, 0)
            self.assertLess(hash, len(self.table.table))

    def test_put(self):
        self.table.put('toto', None)

        self.assertTrue(self.table.exists('toto'))

    def test_same_key_twice(self):
        self.table.put('toto', None)
        with self.assertRaises(KeyError):
            self.table.put('toto', None)

    def test_get(self):
        self.table.put('toto', 13)

        got_value = self.table.get('toto')

        self.assertEqual(13, got_value)


if __name__ == '__main__':
    unittest.main()
