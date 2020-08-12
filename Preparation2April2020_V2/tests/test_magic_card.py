import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):

    # test constructor
    def test_constructor(self):
        mc = MagicCard('mc')
        self.assertEqual(mc.name, 'mc')
        self.assertEqual(mc.damage_points, 5)
        self.assertEqual(mc.health_points, 80)

    # test name er
    def test_name_with_empty_string(self):
        with self.assertRaises(ValueError) as e:
            mc = MagicCard('')
        self.assertEqual(str(e.exception), "Card's name cannot be an empty string.")

    # test name correct
    def test_name_with_correct_string(self):
        mc = MagicCard('mc')
        before = mc.name
        mc.name = "new_name"
        after = mc.name
        self.assertEqual(before, 'mc')
        self.assertEqual(after, 'new_name')

    # test damage_points err
    def test_damage_points_with_negative_int(self):
        mc = MagicCard('mc')
        with self.assertRaises(ValueError) as e:
            mc.damage_points = -1
        self.assertEqual(str(e.exception), "Card's damage points cannot be less than zero.")

    # test damage_points correct
    def test_damage_points_with_correct_int(self):
        mc = MagicCard('mc')
        before = mc.damage_points
        mc.damage_points = 10
        after = mc.damage_points
        self.assertEqual(before, 5)
        self.assertEqual(after, 10)

    # test health_points err
    def test_health_points_with_negative_int(self):
        mc = MagicCard('mc')
        with self.assertRaises(ValueError) as e:
            mc.health_points = -1
        self.assertEqual(str(e.exception), "Card's HP cannot be less than zero.")

    # test health_points correct
    def test_health_points_with_correct_int(self):
        mc = MagicCard('mc')
        before = mc.health_points
        mc.health_points = 90
        after = mc.health_points
        self.assertEqual(before, 80)
        self.assertEqual(after, 90)



