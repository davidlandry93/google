# -*- coding: utf-8 -*-

import unittest
import sort


class TestSort(unittest.TestCase):

    def setUp(self):
        self.list = [1, 6, 3, 4, 7, 1, 5, 12, 15, 16, 134]

    def test_mergesort(self):
        sorted_list = sort.merge_sort(self.list)

        self.assertTrue(self.in_order(sorted_list))

    def test_merge_sorted_lists(self):
        returned_list = sort.merge_sorted_lists([1, 2, 5, 6, 6],
                                                [1, 4, 5])

        self.assertEqual([1, 1, 2, 4, 5, 5, 6, 6], returned_list)

    def test_quicksort(self):
        sort.quick_sort(self.list)
        self.assertTrue(self.in_order(self.list))

    def in_order(self, numbers):
        accumulator = True
        for i in range(0, len(numbers) - 1):
            accumulator = accumulator and numbers[i] <= numbers[i+1]

        return accumulator


if __name__ == '__main__':
    unittest.main()
