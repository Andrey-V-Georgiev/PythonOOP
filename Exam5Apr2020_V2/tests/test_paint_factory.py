import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):

    # test constructor
    def test_constructor(self):
        pf = PaintFactory("pf", 3)
        self.assertEqual(pf.name, "pf")
        self.assertEqual(pf.capacity, 3)
        self.assertEqual(len(pf.ingredients), 0)

    # test add_ingredient wrong type
    def test_add_ingredient_wrong_type(self):
        pf = PaintFactory("pf", 3)
        with self.assertRaises(TypeError) as e:
            pf.add_ingredient("fake", 3)
        self.assertEqual(str(e.exception), "Ingredient of type fake not allowed in PaintFactory")

    # test add_ingredient wrong quantity
    def test_add_ingredient_wrong_quantity(self):
        pf = PaintFactory("pf", 3)
        with self.assertRaises(ValueError) as e:
            pf.add_ingredient("white", 8)
        self.assertEqual(str(e.exception), "Not enough space in factory")

    # test add_ingredient correct
    def test_add_ingredient_correct(self):
        pf = PaintFactory("pf", 3)
        pf.add_ingredient("white", 3)
        self.assertEqual(len(pf.ingredients), 1)

    # test remove_ingredient wrong type
    def test_remove_ingredient_wrong_type(self):
        pf = PaintFactory("pf", 3)
        with self.assertRaises(KeyError) as e:
            pf.remove_ingredient("fake", 3)
        self.assertEqual(str(e.exception), "'No such ingredient in the factory'")

    # test remove_ingredient wrong quantity
    def test_remove_ingredient_wrong_quantity(self):
        pf = PaintFactory("pf", 3)
        pf.add_ingredient("white", 3)
        with self.assertRaises(ValueError) as e:
            pf.remove_ingredient("white", 8)
        self.assertEqual(str(e.exception), "Ingredient quantity cannot be less than zero")

    # test remove_ingredient correct
    def test_remove_ingredient_correct(self):
        pf = PaintFactory("pf", 3)
        pf.add_ingredient("white", 2)
        before = pf.ingredients["white"]
        pf.remove_ingredient("white", 1)
        after = pf.ingredients["white"]
        self.assertEqual(before, 2)
        self.assertEqual(after, 1)

    # test product
    def test_product_correct(self):
        pf = PaintFactory('pf', 3)
        pf.add_ingredient('yellow', 3)
        self.assertEqual(len(pf.products), 1)


