"""Tests for quadraticsolver/quadraticsolver"""
from quadraticvalues import calc
import unittest


class QuadraticCalcYValues(unittest.TestCase):
    """Test that calculations for quadratics are correct"""

    def test_single_value_output(self):
        self.assertListEqual(calc([1]), [4])

    def test_list_multiple_values_output(self):
            self.assertListEqual(calc([0, 1, 2, 3, 4]), [1, 4, 9, 16, 25])
