import unittest

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPLayerRepository(unittest.TestCase):

    # test constructor
    def test_constructor(self):
        pr = PlayerRepository()
        self.assertEqual(len(pr.players), 0)

    # test count
    def test_count(self):
        pr = PlayerRepository()
        self.assertEqual(pr.count, 0)

    # test add err
    def test_add_existing_player_raise_err(self):
        pr = PlayerRepository()
        player1 = Beginner("b")
        pr.add(player1)
        with self.assertRaises(ValueError) as e:
            pr.add(player1)
        self.assertEqual(str(e.exception), "Player b already exists!")

    # test add correct
    def test_add_with_correct_player(self):
        pr = PlayerRepository()
        player = Beginner("b")
        before = pr.count
        pr.add(player)
        after = pr.count
        self.assertEqual(before, 0)
        self.assertEqual(after, 1)

    # test remove err
    def test_remove_with_empty_string_raise_err(self):
        pr = PlayerRepository()
        with self.assertRaises(ValueError) as e:
            pr.remove("")
        self.assertEqual(str(e.exception), "Player cannot be an empty string!")

    # test remove correct
    def test_remove_with_correct_string(self):
        pr = PlayerRepository()
        player = Beginner("b")
        pr.add(player)
        before = pr.count
        pr.remove("b")
        after = pr.count
        self.assertEqual(before, 1)
        self.assertEqual(after, 0)

    # test find
    def test_find(self):
        pr = PlayerRepository()
        insert_player = Beginner("b")
        pr.add(insert_player)
        find_player = pr.find("b")
        self.assertEqual(insert_player, find_player)









































