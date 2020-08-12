import unittest

from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):

    # test constructor
    def test_constructor(self):
        tc = TrapCard('tc')
        self.assertEqual(tc.name, 'tc')
        self.assertEqual(tc.damage_points, 120)
        self.assertEqual(tc.health_points, 5)

    # test name er
    def test_name_with_empty_string(self):
        with self.assertRaises(ValueError) as e:
            tc = TrapCard('')
        self.assertEqual(str(e.exception), "Card's name cannot be an empty string.")

    # test name correct
    def test_name_with_correct_string(self):
        tc = TrapCard('tc')
        before = tc.name
        tc.name = "new_name"
        after = tc.name
        self.assertEqual(before, 'tc')
        self.assertEqual(after, 'new_name')

    # test damage_points err
    def test_damage_points_with_negative_int(self):
        tc = TrapCard('tc')
        with self.assertRaises(ValueError) as e:
            tc.damage_points = -1
        self.assertEqual(str(e.exception), "Card's damage points cannot be less than zero.")

    # test damage_points correct
    def test_damage_points_with_correct_int(self):
        tc = TrapCard('tc')
        before = tc.damage_points
        tc.damage_points = 130
        after = tc.damage_points
        self.assertEqual(before, 120)
        self.assertEqual(after, 130)

    # test health_points err
    def test_health_points_with_negative_int(self):
        tc = TrapCard('tc')
        with self.assertRaises(ValueError) as e:
            tc.health_points = -1
        self.assertEqual(str(e.exception), "Card's HP cannot be less than zero.")

    # test health_points correct
    def test_health_points_with_correct_int(self):
        tc = TrapCard('tc')
        before = tc.health_points
        tc.health_points = 90
        after = tc.health_points
        self.assertEqual(before, 5)
        self.assertEqual(after, 90)



