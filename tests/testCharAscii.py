import unittest
from sys import path

path.append('..')

from charq.charq import CharAscii


teste = CharAscii()


class TestCharAscii(unittest.TestCase):

    def test_class(self):
        self.assertEqual(type(teste.val), list)

    def test_ascii(self):
        self.assertEqual(len(teste.ascii()), 97)
        self.assertEqual(len(teste.ascii(35, 54)), 20)
        self.assertEqual(len(teste.ascii(30, 130)), 97)

    def test_num(self):
        self.assertEqual(len(teste.num()), 10)

    def test_lower(self):
        self.assertEqual(len(teste.lower()), 26)
        self.assertEqual(len(teste.lower(0)), 28)

    def test_up(self):
        self.assertEqual(len(teste.up()), 26)
        self.assertEqual(len(teste.up(0)), 28)

    def test_lower_up(self):
        self.assertEqual(len(teste.lower_up()), 52)
        self.assertEqual(len(teste.lower_up(0)), 54)

    def test_lower_up_num(self):
        self.assertEqual(len(teste.lower_up_num()), 62)
        self.assertEqual(len(teste.lower_up_num(0)), 64)

    def test_symbols(self):
        self.assertEqual(len(teste.symbols()), 37)

    def test_as_str(self):
        self.assertEqual(type(teste.as_str()), str)

    def test_get_bin(self):
        self.assertEqual(len(teste.get_bin()[0]), 8)


if __name__ == '__name__':
    unittest.main()
