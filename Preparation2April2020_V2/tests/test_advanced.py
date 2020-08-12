import unittest

from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):

    # constructor
    def test_constructor(self):
        a = Advanced('a')
        self.assertEqual(a.username, 'a')
        self.assertEqual(a.health, 250)

    # is dead
    def test_is_dead(self):
        a = Advanced('a')
        self.assertFalse(a.is_dead)

    # username err
    def test_username_empty_str(self):
        a = Advanced('a')
        with self.assertRaises(ValueError) as e:
            a.username = ''
        self.assertEqual(str(e.exception), "Player's username cannot be an empty string.")

    # username set correct
    def test_username_correct_str(self):
        a = Advanced('a')
        before = a.username
        a.username = 'b'
        after = a.username
        self.assertEqual(before, 'a')
        self.assertEqual(after, 'b')

    # health err
    def test_health_negative_int(self):
        a = Advanced('a')
        with self.assertRaises(ValueError) as e:
            a.health = -1
        self.assertEqual(str(e.exception), "Player's health bonus cannot be less than zero.")

    # health set correct
    def test_health_correct_int(self):
        a = Advanced('a')
        before = a.health
        a.health = 100
        after = a.health
        self.assertEqual(before, 250)
        self.assertEqual(after, 100)

    # take_damage err
    def test_take_damage_negative_int(self):
        a = Advanced('a')
        with self.assertRaises(ValueError) as e:
            a.take_damage(-1)
        self.assertEqual(str(e.exception), "Damage points cannot be less than zero.")

    # take_damage works correct
    def test_take_damage_correct_int(self):
        a = Advanced('a')
        before = a.health
        a.take_damage(100)
        after = a.health
        self.assertEqual(before, 250)
        self.assertEqual(after, 150)
