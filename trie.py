# -*- coding: utf-8 -*-

import unittest


class Trie:

    def __init__(self, key, value):
        self.children = []
        self.key = key
        self.value = value

    def insert(self, key, value):
        if len(key) is 1:
            new_node = Trie(key[0], value)
        else:
            new_node = Trie(key[0], None)
            new_node.insert(key[1:], value)

        self.children.append(new_node)

    def retrieve(self, key):
        next_node = filter(lambda x: x.key == key[0],
                           self.children)[0]

        if len(key) is 1:
            return next_node.value
        else:
            return next_node.retrieve(key[1:])

    @classmethod
    def root_node(cls):
        return Trie('', None)


class TrieTest(unittest.TestCase):

    def setUp(self):
        self.tree = Trie.root_node()

    def test_insert(self):
        self.tree.insert('alphonse', 63)
        self.tree.insert('alph', 23)

        self.assertEqual(63, self.tree.retrieve('alphonse'))
        self.assertEqual(23, self.tree.retrieve('alph'))


if __name__ == '__main__':
    unittest.main()
