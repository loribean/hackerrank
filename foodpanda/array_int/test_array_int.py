import array_int_improved
import unittest


class TestGetMaxChar(unittest.TestCase):
    def test_case_one(self):
        self.assertEqual(array_int_improved.get_max_char("abCB"), "B")

    def test_case_two(self):
        self.assertEqual(array_int_improved.get_max_char("a"), "NO")

    def test_case_three(self):
        self.assertEqual(array_int_improved.get_max_char("ABCDabc"), "C")

    def test_case_four(self):
        self.assertEqual(array_int_improved.get_max_char(""), "NO")

    def test_case_five(self):
        self.assertEqual(array_int_improved.get_max_char("AaBbCc"), "C")

    def test_case_six(self):
        self.assertEqual(array_int_improved.get_max_char("abcdefgh"), "NO")

    def test_case_seven(self):
        self.assertEqual(array_int_improved.get_max_char("AaAa"), "A")

    def test_case_eight(self):
        self.assertEqual(array_int_improved.get_max_char("abCdefG"), "NO")

    def test_case_nine(self):
        self.assertEqual(array_int_improved.get_max_char("XYZxyz"), "Z")
    
    # def test_case_none(self):
    #     self.assertEqual(array_int_improved.get_max_char(None), "NO")

    # def test_case_int(self):
    #     self.assertEqual(array_int_improved.get_max_char(123), "NO")

    def test_case_string_int(self):
        self.assertEqual(array_int_improved.get_max_char("123"), "NO")

    def test_case_empty_string(self):
        self.assertEqual(array_int_improved.get_max_char(""), "NO")

if __name__ == '__main__':
    unittest.main()