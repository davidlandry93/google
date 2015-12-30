# -*- coding: utf-8 -*-

import unittest


class RedBlack:

    BLACK = True
    RED = False

    def __init__(self, color, value):
        self.color = color
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.isLeaf():
            if value < self.value:
                self.left = RedBlack(not self.color, value)
            else:
                self.right = RedBlack(not self.color, value)
        else:
            if value < self.value:
                self.left = RedBlack(not self.color, value)
            else:
                self.right = RedBlack(not self.color, value)

    def exists(self, value):
        if self.value is value:
            return True
        elif self.isLeaf():
            return False
        elif self.value > value:
            self.left.exists(value)
        elif self.value < value:
            self.right.exists(value)
        else:
            raise Exception()

    def isLeaf(self):
        return self.left is None and self.right is None

    @classmethod
    def root_node(cls, value):
        return RedBlack(RedBlack.BLACK, value)


class RedBlackTest(unittest.TestCase):

    def setUp(self):
        self.tree = RedBlack.root_node(1)

    def test_insert(self):
        self.tree.insert(13)

        self.assertTrue(self.tree.exists(13))


if __name__ == '__main__':
    unittest.main()
