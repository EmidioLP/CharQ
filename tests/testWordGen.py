import unittest
from sys import path

path.append('..')

from src.charq import WordGenerate

teste = WordGenerate()

class TestWordGenerate(unittest.TestCase):

    def test_class(self):
        self.assertEqual(type(teste.val), str)
        self.assertEqual(teste.val, 'CharQ')

    def test_word(self):
        self.assertEqual(len(teste.word(12)), 12)
        self.assertEqual(teste.word().islower(), True)
        self.assertEqual(teste.word(case='up').isupper(), True)
        self.assertEqual(teste.word(case='camel').islower(), False)
        self.assertEqual(teste.word(case='camel').isupper(), False)

    def test_num(self):
        self.assertEqual(type(teste.num(typen='str')), str)
        self.assertEqual(type(teste.num()), int)
        self.assertEqual(len(teste.num(tam=12, typen='str')), 12)

    def test_passw(self):
        self.assertEqual(type(teste.passw()), str)
        self.assertEqual(len(teste.passw(12)), 12)


if __name__ == '__name__':
    unittest.main()


"""
    def test_word(self):
        self.assertEqual(type(teste.val), str)

    def test_word(self):
        self.assertEqual(type(teste.val), str)

    def test_word(self):
        self.assertEqual(type(teste.val), str)
"""
