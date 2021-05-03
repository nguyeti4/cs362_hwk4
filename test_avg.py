import unittest
import avg

class Average(unittest.TestCase):
    def test_avg(self):
        actual = avg.calc_avg(elements = [1,2,3,4,5,6])
        expected = 3.5
        self.assertEqual(actual,expected)
    def test_avg_exception(self):
        with self.assertRaises(ValueError) as exception_context:
            avg.calc_avg(elements = [1,2,3,4,"5",6])
        self.assertEqual(
            str(exception_context.exception),"All elements should be ints"
        )
    def test_avg_exception2(self):
        with self.assertRaises(ValueError) as exception_context:
            avg.calc_avg(elements = [])
        self.assertEqual(
            str(exception_context.exception),"List should not be empty"
        )