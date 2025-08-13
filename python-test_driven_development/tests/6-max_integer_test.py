#!/usr/bin/python3
"""
Unittest for max_integer function
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_empty_list(self):
        """Test empty list returns None"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_single_element(self):
        """Test list with single element"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-1]), -1)

    def test_positive_numbers(self):
        """Test list with positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negative_numbers(self):
        """Test list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-10, -5, -1]), -1)

    def test_mixed_numbers(self):
        """Test list with positive and negative numbers"""
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([-5, -10, 3, 2]), 3)
        self.assertEqual(max_integer([10, -20, 30, -40]), 30)

    def test_duplicate_numbers(self):
        """Test list with duplicate numbers"""
        self.assertEqual(max_integer([1, 1, 1]), 1)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([3, 3, 7, 7]), 7)

    def test_max_at_beginning(self):
        """Test when maximum is at the beginning"""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)
        self.assertEqual(max_integer([100, 50, 25]), 100)

    def test_max_at_end(self):
        """Test when maximum is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)
        self.assertEqual(max_integer([25, 50, 100]), 100)

    def test_max_in_middle(self):
        """Test when maximum is in the middle"""
        self.assertEqual(max_integer([1, 10, 2]), 10)
        self.assertEqual(max_integer([5, 1, 9, 3]), 9)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)
        self.assertEqual(max_integer([2**31 - 1, 2**30]), 2**31 - 1)

    def test_zero(self):
        """Test lists containing zero"""
        self.assertEqual(max_integer([0, 1, 2]), 2)
        self.assertEqual(max_integer([-1, 0, -2]), 0)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_two_elements(self):
        """Test lists with exactly two elements"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)
        self.assertEqual(max_integer([-1, -2]), -1)

    def test_long_list(self):
        """Test with a longer list"""
        long_list = list(range(1, 101))  # [1, 2, 3, ..., 100]
        self.assertEqual(max_integer(long_list), 100)

        # Reverse order
        long_list_reverse = list(range(100, 0, -1))  # [100, 99, 98, ..., 1]
        self.assertEqual(max_integer(long_list_reverse), 100)

    def test_float_like_integers(self):
        """Test with numbers that could be confused with floats"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
        # All integers, should work fine

    def test_same_numbers_different_positions(self):
        """Test multiple occurrences of max value"""
        self.assertEqual(max_integer([5, 3, 5, 1]), 5)
        self.assertEqual(max_integer([7, 7, 2, 7]), 7)


if __name__ == '__main__':
    unittest.main()
