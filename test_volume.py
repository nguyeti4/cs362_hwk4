import unittest
import volume

class TestVolume(unittest.TestCase):
    def test_vol(self):
        actual = volume.calc_volume("5")
        expected = 125
        self.assertEqual(actual,expected)
    def test_vol_exception(self):
        with self.assertRaises(ValueError) as exception_context:
            volume.calc_volume("-4")
        self.assertEqual(
            str(exception_context.exception),"The length must be a positive integer"
        )
    def test_vol_exception2(self):
        with self.assertRaises(ValueError) as exception_context:
            volume.calc_volume("three")
        self.assertEqual(
            str(exception_context.exception),"The length must be a positive integer"
        )
    