import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for max_integer"""
    def test_module_docstring(self):
        """Test for module docstring"""
        m = __import__("6-max_integer").__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Test for function docstring"""
        m = __import__("6-max_integer").max_integer.__doc__
        self.assertTrue(len(m) > 1)

    def test_max_positive_integr(self):
        """Test for all positive with max in beginning, middle and end"""
        self.assertEqual(max_integer([34, 6, 9]), 34)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([3, 16, 8]), 16)

    def test_max_negative_integer(slef):
        """Test for all positive with max in beginning, middle and end"""
        slef.assertEqual(max_integer([-45, -67, -12]), -12)
        slef.assertEqual(max_integer([-81, -22, -92]), -22)
        slef.assertEqual(max_integer([-100, -97, -35]), -35)

    def test_max_integer(self):
        """Test for any integer number"""
        self.assertEqual(max_integer([10, 0, -2]), 10)
        self.assertEqual(max_integer([-3, -7, 0, -2]), 0)

    def test_none(self):
        """Test for empty list []"""
        self.assertEqual(max_integer([]), None)

    def test_no_argumnet(self):
        """Test for no argument"""
        self.assertIsNone(max_integer())

    def test_one_argument(self):
        """Test one argumnet"""
        self.assertEqual(max_integer([-1]), -1)

    def test_none(self):
        """Test for None as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_wrong_type(self):
        """Test for wrong data type"""
        string = [1, 3, "wrong"]
        with self.assertRaises(TypeError):
            max_integer(string)


if __name__ == "__main__":
    unittest.main()
