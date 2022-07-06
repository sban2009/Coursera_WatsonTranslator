"""
Testing Module
"""
import unittest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import translator as t


class TestTranslator(unittest.TestCase):
    def test_nullInput_f2e(self):
        self.assertEqual(t.french_to_english(""), "")

    def test_HelloBonjour_f2e(self):
        self.assertEqual(t.french_to_english("Bonjour"), "Hello")

    def test_HelloBonjour_f2e_not(self):
        self.assertNotEqual(t.french_to_english("Bonjour"), "Yes")

    def test_nullInput_e2f(self):
        self.assertEqual(t.english_to_french(""), "")

    def test_BonjourHello_e2f(self):
        self.assertEqual(t.english_to_french("Hello"), "Bonjour")

    def test_BonjourHello_e2f_not(self):
        self.assertNotEqual(t.english_to_french("Hello"), "J'Taime")


if "__name__" == "__main__":
    unittest.main()
