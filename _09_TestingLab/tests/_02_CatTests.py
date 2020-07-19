import unittest

from Cat import Cat


class CatTests(unittest.TestCase):
    """
    Cat's name is initialized correct
    """
    def test_cat_is_initialized_with_correct_name(self):
        self.cat = Cat('Pesho')
        self.assertEqual(self.cat.name, 'Pesho')

    """
    Cat's size is increased after eating
    """
    def test_cat_size_is_increased_after_eating(self):
        self.cat = Cat('Pesho')
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    """
    Cat is fed after eating
    """
    def test_cat_is_fed_after_eating(self):
        self.cat = Cat('Pesho')
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    """
    Cat cannot eat if already fed, raises an error
    """
    def test_cat_cannot_eat_if_already_fed(self):
        self.cat = Cat('Pesho')
        self.cat.eat()
        with self.assertRaises(Exception):
            self.cat.eat()

    """
    Cat cannot fall asleep if not fed, raises an error
    """
    def test_cat_cannot_sleep_if_not_fed(self):
        self.cat = Cat('Pesho')
        with self.assertRaises(Exception):
            self.cat.sleep()

    """
    Cat is not sleepy after sleeping
    """
    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat = Cat('Pesho')
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()

