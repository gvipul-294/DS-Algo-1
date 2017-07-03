import unittest
from array import *

#
# Example to run test cases individually:
#
# 'python -m unittest -v tests.TestArray.test_segregate'
# (Runs all test cases specific to segregate method)
#


class TestArray(unittest.TestCase):
    def test_segregate(self):
        self.assertEqual(segregate([1, 0]), [0, 1])
        self.assertEqual(segregate([0]), [0])

    def test_largest_sum_contiguous_subarray(self):
        self.assertEqual(largestSumContiguousSubarray([-2, -3, -1, -5, -4]), (-1, 2, 2))

if __name__ == "__main__":
    unittest.main()
