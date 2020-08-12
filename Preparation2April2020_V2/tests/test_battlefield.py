import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):

    # test attacker is dead raise err
    def test_fight_attacker_is_dead_raise_err(self):
        attacker = Beginner('attacker')
        attacker.health = 0
        enemy = Beginner('enemy')
        with self.assertRaises(ValueError) as e:
            BattleField.fight(attacker, enemy)
        self.assertEqual(str(e.exception), "Player is dead!")

    # test enemy is dead raise err
    def test_fight_enemy_is_dead_raise_err(self):
        attacker = Beginner('attacker')
        enemy = Beginner('enemy')
        enemy.health = 0
        with self.assertRaises(ValueError) as e:
            BattleField.fight(attacker, enemy)
        self.assertEqual(str(e.exception), "Player is dead!")


    # test if attacker is Beginner
    def test_attacker_is_beginner_increase_health_and_damage_points(self):
        attacker = Beginner('attacker')
        attacker_card = TrapCard('atc')
        attacker.card_repository.add(attacker_card)
        before_health = attacker.health
        before_card_damage_points = attacker_card.damage_points

        enemy = Beginner('enemy')
        enemy_card = TrapCard('etc')
        enemy.card_repository.add(enemy_card)

        BattleField.fight(attacker, enemy)
        after_health = attacker.health
        attacker_find_card = attacker.card_repository.find('atc')
        after_card_damage_points = attacker_find_card.damage_points

        self.assertEqual(50, before_health)
        self.assertEqual(95, after_health)
        self.assertEqual(120, before_card_damage_points)
        self.assertEqual(150, after_card_damage_points)

    # test if enemy is Beginner
    def test_enemy_is_beginner_increase_health_and_damage_points(self):
        attacker = Beginner('attacker')
        attacker_card = TrapCard('atc')
        attacker.card_repository.add(attacker_card)

        enemy = Beginner('enemy')
        enemy_card = TrapCard('etc')
        enemy.card_repository.add(enemy_card)
        before_health = enemy.health
        before_card_damage_points = enemy_card.damage_points

        BattleField.fight(attacker, enemy)
        after_health = enemy.health
        enemy_find_card = enemy.card_repository.find('etc')
        after_card_damage_points = enemy_find_card.damage_points

        self.assertEqual(50, before_health)
        self.assertEqual(-55, after_health)
        self.assertEqual(120, before_card_damage_points)
        self.assertEqual(150, after_card_damage_points)

    # test attacker bonus


    # test enemy bonus


    # test attacker attack


    # test enemy attack





