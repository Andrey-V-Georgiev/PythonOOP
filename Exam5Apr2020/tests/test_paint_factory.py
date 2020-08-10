import unittest

from project.factory.paint_factory import PaintFactory


class TestingPaintFactory(unittest.TestCase):
    """ testing constructor """

    def test_constructor_with_correct_arguments(self):
        pf = PaintFactory('pf', 3)
        self.assertEqual(pf.name, 'pf')
        self.assertEqual(pf.capacity, 3)
        self.assertEqual(len(pf.ingredients), 0)

    """ testing add_ingredient """

    def test_add_ingredient_with_incorrect_ingredient_type_raise_error(self):
        pf = PaintFactory('pf', 3)
        with self.assertRaises(TypeError) as e:
            pf.add_ingredient('fake', 2)
        self.assertEqual(e.exception.__str__(), 'Ingredient of type fake not allowed in PaintFactory')

    def test_add_ingredient_with_incorrect_ingredient_quantity_raise_error(self):
        pf = PaintFactory('pf', 3)
        with self.assertRaises(ValueError) as e:
            pf.add_ingredient('yellow', 7)
        self.assertEqual(e.exception.__str__(), 'Not enough space in factory')

    def test_add_ingredient_with_correct_input(self):
        pf = PaintFactory('pf', 3)
        pf.add_ingredient('yellow', 3)
        before_length = len(pf.ingredients)
        after_length = len(pf.ingredients) + 1
        self.assertNotEqual(before_length, after_length)

    """ testing remove_ingredient """

    def test_remove_ingredient_with_incorrect_ingredient_type_raise_error(self):
        pf = PaintFactory('pf', 3)
        pf.add_ingredient('yellow', 3)
        with self.assertRaises(KeyError) as e:
            pf.remove_ingredient('blue', 2)
        self.assertEqual(str(e.exception), "'No such ingredient in the factory'")

    def test_remove_ingredient_with_incorrect_quantity_raise_error(self):
        pf = PaintFactory('pf', 3)
        pf.add_ingredient('yellow', 3)
        with self.assertRaises(ValueError) as e:
            pf.remove_ingredient('yellow', 7)
        self.assertEqual(str(e.exception), 'Ingredient quantity cannot be less than zero')

    def test_remove_ingredien_with_correct_input(self):
        pf = PaintFactory('pf', 3)
        pf.add_ingredient('blue', 3)
        before_length = pf.ingredients['blue']
        pf.remove_ingredient('blue', 1)
        after_length = pf.ingredients['blue']
        self.assertNotEqual(before_length, after_length)

    """ testing remove_ingredient """
    def test_products_return_correct_dict(self):
        pf = PaintFactory('pf', 3)
        pf.add_ingredient('yellow', 3)
        self.assertEqual(len(pf.products), 1)


if __name__ == "__main__":
    unittest.main()
