import unittest

from project.controller import Controller
from project.player.beginner import Beginner


class TestController(unittest.TestCase):

    # test constructor
    def test_constructor(self):
        controller = Controller()
        self.assertEqual(0, controller.player_repository.count)
        self.assertEqual(0, controller.card_repository.count)

    # test add_player
    def test_add_player(self):
        controller = Controller()
        before = controller.player_repository.count
        controller.add_player("Beginner", "b")
        after = controller.player_repository.count
        self.assertEqual(0, before)
        self.assertEqual(1, after)

    # test add_card
    def test_add_card(self):
        controller = Controller()
        before = controller.card_repository.count
        controller.add_card("Magic", "mc")
        after = controller.card_repository.count
        self.assertEqual(0, before)
        self.assertEqual(1, after)

    # test add_player_card
    def test_add_player_card(self):
        controller = Controller()
        controller.add_player("Beginner", "b")
        found_player = controller.player_repository.find("b")
        controller.add_card("Magic", "mc")
        before = len(found_player.card_repository.cards)
        controller.add_player_card("b", "mc")
        after = len(found_player.card_repository.cards)
        self.assertEqual(0, before)
        self.assertEqual(1, after)

    # test fight


    # test report













































