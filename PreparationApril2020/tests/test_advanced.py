import unittest

from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):

    def test_constructor_with_valid_input(self):
        advanced = Advanced("a")
        self.assertEqual(advanced.username, 'a')
        self.assertEqual(advanced.health, 250)
        self.assertFalse(advanced.is_dead)

    # testing username
    def test_username_with_empty_string_raise_error(self):
        with self.assertRaises(ValueError) as e:
            Advanced('')
        self.assertEqual(str(e.exception), "Player's username cannot be an empty string.")

    def test_username_with_correct_string(self):
        advanced = Advanced('a')
        self.assertEqual(advanced.username, 'a')

    # testing health
    def test_health_with_negative_number_raise_error(self):
        advanced = Advanced('a')
        with self.assertRaises(ValueError) as e:
            advanced.health = -1
        self.assertEqual(str(e.exception), "Player's health bonus cannot be less than zero.")

    def test_health_with_correct_number(self):
        advanced = Advanced('a')
        advanced.health = 10
        self.assertEqual(advanced.health, 10)

    # testing take_damage
    def test_take_damage_with_negative_number_raise_error(self):
        advanced = Advanced('a')
        with self.assertRaises(ValueError) as e:
            advanced.take_damage(-1)
        self.assertEqual(str(e.exception), "Damage points cannot be less than zero.")

    def test_take_damage_with_correct_number(self):
        advanced = Advanced('a')
        before = advanced.health
        advanced.take_damage(100)
        after = advanced.health
        self.assertEqual(before, 250)
        self.assertEqual(after, 150)

    # testing is_dead
    def test_is_dead_correct_result(self):
        advanced = Advanced('a')
        before = advanced.is_dead
        advanced.take_damage(250)
        after = advanced.is_dead
        self.assertEqual(before, False)
        self.assertEqual(after, True)






































