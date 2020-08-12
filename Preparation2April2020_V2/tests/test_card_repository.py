import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):

    # test constructor
    def test_constructor(self):
        cr = CardRepository()
        self.assertEqual(len(cr.cards), 0)

    # test count
    def test_count(self):
        cr = CardRepository()
        self.assertEqual(cr.count, 0)

    # test add err
    def test_add_with_existing_card_raise_err(self):
        cr = CardRepository()
        card = MagicCard('mc')
        cr.add(card)
        with self.assertRaises(ValueError) as e:
            cr.add(card)
        self.assertEqual(str(e.exception), "Card mc already exists!")

    # test add correct
    def test_add_card_correct(self):
        cr = CardRepository()
        card = MagicCard('mc')
        before = cr.count
        cr.add(card)
        after = cr.count
        self.assertEqual(before, 0)
        self.assertEqual(after, 1)

    # test remove err
    def test_remove_with_empty_string_raise_err(self):
        cr = CardRepository()
        with self.assertRaises(ValueError) as e:
            cr.remove("")
        self.assertEqual(str(e.exception), "Card cannot be an empty string!")

    # test remove correct
    def test_remove_correct_string(self):
        cr = CardRepository()
        card = MagicCard('mc')
        cr.add(card)
        before = cr.count
        cr.remove('mc')
        after = cr.count
        self.assertEqual(before, 1)
        self.assertEqual(after, 0)

    # test find
    def test_find(self):
        cr = CardRepository()
        insert_card = MagicCard('mc')
        cr.add(insert_card)
        find_card = cr.find('mc')
        self.assertEqual(insert_card, find_card)
