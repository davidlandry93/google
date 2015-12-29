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
        sort.quick_sort(0, len(self.list), self.list)

        self.assertTrue(self.in_order(self.list))

    def test_partition(self):
        pivot_index = sort.partition(0, len(self.list), self.list)

        for e in self.list[0:pivot_index]:
            self.assertGreaterEqual(self.list[pivot_index], e)
 
        for e in self.list[pivot_index:]:
            self.assertGreaterEqual(e, self.list[pivot_index])

    def in_order(self, numbers):
        accumulator = True
        for i in range(0, len(numbers) - 1):
            accumulator = accumulator and numbers[i] <= numbers[i+1]

        return accumulator


if __name__ == '__main__':
    unittest.main()
