#!python

import unittest

class CalculatorTest(unittest.TestCase):

    def test_contains_only_two_parameters(self):
      pass

    # def test_divide_by_zero(self):
    #     assert divide()
    
    def test_add(self):
      self.assertEqual(add(8, 9)) == 17

    def values():
      return 2,

if __name__ == '__main__':
    unittest.main()
