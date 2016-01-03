#!/usr/bin/env python2

import unittest


class ChangeMaker:

    def __init__(self, max_amount, denominations):
        first_row = [[0] + [float('inf')] * (max_amount)]

        self.table = first_row + [[0] + [float('inf')] * (max_amount)] * len(denominations)

        self.fill_table(max_amount, denominations)

    def fill_table(self, max_amount, denominations):
        for amount in range(1, max_amount + 1):
            for j, denomination in enumerate(denominations):
                if denomination <= amount:
                    new_entry = min(self.table[j][amount],
                                    self.table[j+1][amount-denomination] + 1)
                else:
                    new_entry = self.table[j][amount]

                self.table[j+1][amount] = new_entry

    def amount(self, amount):
        if amount <= len(self.table[0]):
            return self.table[len(self.table) - 1][amount]
        else:
            return None


class ChangeMakerTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_noDenomination(self):
        change_maker = ChangeMaker(1, [])

        print(change_maker.table)

        self.assertEqual(float('inf'), change_maker.amount(1))

    def test_only_one_pence(self):
        change_maker = ChangeMaker(10, [1])

        print(change_maker.table)

        for i in range(11):
            self.assertEqual(i, change_maker.amount(i))

    def test_cad(self):
        change_maker = ChangeMaker(100, [1, 5,10,25,100])

        print(change_maker.table)

        self.assertEqual(4, change_maker.amount(76))
        self.assertEqual(1, change_maker.amount(100))

if __name__ == '__main__':
    unittest.main()
