import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase): 
    def testnull(self):
        self.assertIsNone(english_to_french(""), None)
    def test_translate(self):
        self.assertAlmostEqual(english_to_french("Hello"), "Bonjour")

class TestF2E(unittest.TestCase): 
    def testnull(self):
        self.assertIsNone(french_to_english(""), None)
    def test_translate(self):
        self.assertAlmostEqual(french_to_english("Bonjour"), "Hello")
        
unittest.main()



