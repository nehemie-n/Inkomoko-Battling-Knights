import unittest
from src.game import Game, DIRECTION


class TestGame(unittest.TestCase):

    def test_parse_moves(self):
        game = Game()
        game.play()

    def test_fight(self):
        game = Game()
        game.play()

    def test_item_owned(self):
        game = Game()
        red = game.knights["R"]
        game._Game__move_knight(red, DIRECTION.S)
        game._Game__move_knight(red, DIRECTION.S)
        game._Game__move_knight(red, DIRECTION.E)
        self.assertFalse(game.items["A"].is_equiped)
        game._Game__move_knight(red, DIRECTION.E)
        self.assertEqual(red.position, (2, 2))
        self.assertEqual(red.item, game.items["A"])
        self.assertTrue(game.items["A"].is_equiped)
        # Position of knight should also update on board
        self.assertEqual(game.board.get_knight(red.position[0], red.position[1]), red)

    def test_item_moved_with(self):
        game = Game()
        red = game.knights["R"]
        game._Game__move_knight(red, DIRECTION.S)
        game._Game__move_knight(red, DIRECTION.S)
        game._Game__move_knight(red, DIRECTION.E)
        self.assertFalse(game.items["A"].is_equiped)
        game._Game__move_knight(red, DIRECTION.E)
        self.assertEqual(red.position, (2, 2))
        self.assertEqual(red.item, game.items["A"])
        self.assertTrue(game.items["A"].is_equiped)
        