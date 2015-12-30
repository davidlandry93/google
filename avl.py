# -*- coding: utf-8 -*-

import unittest


class AvlTree:

    def __init__(self):
        self.root = AvlNode(None)

    def insert(self, value):
        self.root = self.root.insert(value)

    def traverse_in_order(self):
        return self.root.traverse_in_order()

    def traverse_pre_order(self):
        return self.root.traverse_pre_order()

    def height(self):
        return self.root.height()


class AvlNode:

    def __init__(self, value):
        self.value = value

        if value is None:
            self.left = None
            self.right = None
        else:
            self.left = AvlNode(None)
            self.right = AvlNode(None)

    def insert(self, value):
        if self.value is None:
            self.value = value
            self.left = AvlNode(None)
            self.right = AvlNode(None)
        else:
            if value <= self.value:
                self.left.insert(value)
            else:
                self.right.insert(value)

        return self.rebalance_if_necessary()

    def traverse_in_order(self):
        if self.value is None:
            return []
        else:
            return (self.left.traverse_in_order() +
                    [self.value] +
                    self.right.traverse_in_order())

    def traverse_pre_order(self):
        if self.value is None:
            return []
        else:
            return ([self.value] +
                    self.left.traverse_pre_order() +
                    self.right.traverse_pre_order())

    def height(self):
        if self.value is None:
            return 0
        else:
            return 1 + max((self.left.height(), self.right.height()))

    def rebalance_if_necessary(self):
        if self.is_unbalanced():
            if self.left.height() > self.right.height():
                if self.left.left.height() > self.left.right.height():
                    # left left.
                    return self.rotate_right()
                else:
                    # left right.
                    pass
            else:
                if self.right.right.height() > self.right.left.height():
                    # right right.
                    return self.rotate_left()
                else:
                    # right left.
                    pass
        else:
            return self

    def is_unbalanced(self):
        return abs(self.right.height() - self.left.height()) > 1

    def rotate_left(self):
        new_root = self.right
        self.right = self.right.left
        new_root.left = self

        return new_root

    def rotate_right(self):
        new_root = self.left
        self.left = new_root.right
        new_root.right = self

        return new_root


class AvlTreeTest(unittest.TestCase):

    def setUp(self):
        self.tree = AvlTree()

    def test_insert_one(self):
        self.tree.insert(2)

        self.assertEqual([2], self.tree.traverse_in_order())

    def test_insert_many(self):
        self.tree.insert(2)
        self.tree.insert(1)
        self.tree.insert(3)

        self.assertEqual([1,2,3], self.tree.traverse_in_order())

    def test_height(self):
        self.tree.insert(3)
        self.tree.insert(4)

        self.assertEqual(2, self.tree.height())

    def test_right_right(self):
        self.tree.insert(1)
        self.tree.insert(2)
        self.tree.insert(3)

        self.assertEqual([2,1,3], self.tree.traverse_pre_order())

    def test_left_left(self):
        self.tree.insert(3)
        self.tree.insert(2)
        self.tree.insert(1)

        self.assertEqual([2,1,3], self.tree.traverse_pre_order())


if __name__ == '__main__':
    unittest.main()
