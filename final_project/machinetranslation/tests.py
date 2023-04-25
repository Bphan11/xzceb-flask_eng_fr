import unittest

from translator import english_to_french, french_to_english

class TestStringMethods(unittest.TestCase):
    def text_englishToFrench(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class Test_french_to_english(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()