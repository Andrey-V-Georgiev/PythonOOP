import unittest

from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):

    # constructor
    def test_constructor(self):
        b = Beginner('b')
        self.assertEqual(b.username, 'b')
        self.assertEqual(b.health, 50)

    # is dead
    def test_is_dead(self):
        b = Beginner('b')
        self.assertFalse(b.is_dead)

    # username err
    def test_username_empty_str(self):
        b = Beginner('b')
        with self.assertRaises(ValueError) as e:
            b.username = ''
        self.assertEqual(str(e.exception), "Player's username cannot be an empty string.")

    # username set correct
    def test_username_correct_str(self):
        b = Beginner('b')
        before = b.username
        b.username = 'c'
        after = b.username
        self.assertEqual(before, 'b')
        self.assertEqual(after, 'c')

    # health err
    def test_health_negative_int(self):
        b = Beginner('b')
        with self.assertRaises(ValueError) as e:
            b.health = -1
        self.assertEqual(str(e.exception), "Player's health bonus cannot be less than zero.")

    # health set correct
    def test_health_correct_int(self):
        b = Beginner('b')
        before = b.health
        b.health = 100
        after = b.health
        self.assertEqual(before, 50)
        self.assertEqual(after, 100)

    # take_damage err
    def test_take_damage_negative_int(self):
        b = Beginner('b')
        with self.assertRaises(ValueError) as e:
            b.take_damage(-1)
        self.assertEqual(str(e.exception), "Damage points cannot be less than zero.")

    # take_damage works correct
    def test_take_damage_correct_int(self):
        b = Beginner('b')
        before = b.health
        b.take_damage(10)
        after = b.health
        self.assertEqual(before, 50)
        self.assertEqual(after, 40)
