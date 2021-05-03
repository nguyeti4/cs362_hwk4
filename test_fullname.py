import unittest
import fullname

class Fullname(unittest.TestCase):
    def test_full(self):
        actual = fullname.gen_fullname("Timothy","Nguyen")
        expected = "Timothy Nguyen"
        self.assertEqual(actual,expected)
    def test_full_exception(self):
        with self.assertRaises(ValueError) as exception_context:
            fullname.gen_fullname("","Nguyen")
        self.assertEqual(
            str(exception_context.exception),"You are missing a first name"
        )
    def test_full_exception2(self):
        with self.assertRaises(ValueError) as exception_context:
            fullname.gen_fullname("Timothy","Ngu123")
        self.assertEqual(
            str(exception_context.exception),"All characters in last name must be a letter"
        )   
       
       
     