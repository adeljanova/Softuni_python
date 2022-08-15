import unittest
from unittest import TestCase

from project.mammal import Mammal


class MammalTest(TestCase):
    NAME = 'Aleks'
    TYPE = 'mammal'
    SOUND = 'Woof'
    KINGDOM = 'animals'

    def setUp(self) -> None:
        self.animal = Mammal(self.NAME, self.TYPE, self.SOUND)

    def test_mammal_init(self):
        self.assertEqual(self.NAME, self.animal.name)
        self.assertEqual(self.TYPE, self.animal.type)
        self.assertEqual(self.SOUND, self.animal.sound)
        self.assertEqual('animals', self.animal._Mammal__kingdom)

    def test_make_sound_if_returns_correct_string(self):
        actual_result = self.animal.make_sound()
        expected_result = f"{self.NAME} makes {self.SOUND}"
        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom(self):
        actual_result = self.animal.get_kingdom()
        expected_result = 'animals'
        self.assertEqual(expected_result, actual_result)

    def test_info_if_returns_correct_string(self):
        actual_result = self.animal.info()
        expected_result = f"{self.animal.name} is of type {self.animal.type}"
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
