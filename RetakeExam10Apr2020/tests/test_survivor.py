import unittest

from project.survivor import Survivor


class TestingSurvivor(unittest.TestCase):
    """
    test constructor
    """

    def test_constructor_create_instance_correct(self):
        s: Survivor = Survivor('Pesho', 34)
        self.assertEqual(s.name, 'Pesho')
        self.assertEqual(s.age, 34)
        self.assertEqual(s.health, 100)
        self.assertEqual(s.needs, 100)
        self.assertEqual(s.needs_sustenance, False)
        self.assertEqual(s.needs_healing, False)

    """
    test name
    """

    def test_name_with_empty_string_raise_exception(self):
        with self.assertRaises(ValueError) as e:
            s: Survivor = Survivor('', 34)
        self.assertEqual(e.exception.__str__(), 'Name not valid!')

    """
    test age
    """

    def test_age_with_negative_value_raise_exception(self):
        with self.assertRaises(ValueError) as e:
            s: Survivor = Survivor('Pesho', -34)
        self.assertEqual(e.exception.__str__(), 'Age not valid!')

    """
    test health
    """

    def test_set_health_with_negative_value(self):
        s: Survivor = Survivor("Pesho", 34)
        with self.assertRaises(ValueError) as e:
            s.health = -1
        self.assertEqual(e.exception.__str__(), 'Health not valid!')

    def test_set_health_with_more_than_max(self):
        s: Survivor = Survivor("Pesho", 34)
        s.health = 300
        self.assertEqual(s.health, 100)

    """
    test needs
    """

    def test_set_needs_with_negative_value(self):
        s: Survivor = Survivor("Pesho", 34)
        with self.assertRaises(ValueError) as e:
            s.needs = -1
        self.assertEqual(e.exception.__str__(), 'Needs not valid!')

    def test_set_needs_with_more_than_max(self):
        s: Survivor = Survivor("Pesho", 34)
        s.needs = 300
        self.assertEqual(s.needs, 100)

    """
    test needs_sustenance
    """

    def test_needs_sustenance_under_100_return_true(self):
        s: Survivor = Survivor("Pesho", 34)
        s.needs = 90
        self.assertEqual(s.needs_sustenance, True)

    """
    test needs_healing
    """

    def test_needs_healing_under_100_return_true(self):
        s: Survivor = Survivor("Pesho", 34)
        s.health = 90
        self.assertEqual(s.needs_healing, True)


if __name__ == "__main__":
    unittest.main()
