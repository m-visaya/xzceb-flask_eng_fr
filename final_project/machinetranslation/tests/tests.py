import unittest

from .machinetranslation import english_to_french, french_to_english

class TestE2F(unittest.TestCase): 
    def testnull(self):
        self.assertNotEqual(english_to_french("Hello"), None)
    def test_translate(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class TestF2E(unittest.TestCase): 
    def testnull(self):
        self.assertNotEqual(french_to_english("Bonjour"), None)
    def test_translate(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        
unittest.main()



