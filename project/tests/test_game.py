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
        game._Game__move_knight(game.knights["R"], DIRECTION.S)
        game._Game__move_knight(game.knights["R"], DIRECTION.S)
        game._Game__move_knight(game.knights["R"], DIRECTION.E)
        self.assertFalse(game.items["A"].is_equiped)
        game._Game__move_knight(game.knights["R"], DIRECTION.E)
        print(game.board.get_knight(2, 2), " : BOARD")
        self.assertEqual(game.knights["R"].position, (2, 2))
        self.assertEqual(game.knights["R"].item, game.items["A"])
        self.assertTrue(game.items["A"].is_equiped)
        # Position of knight should also update on board
        self.assertEqual(game.board.get_knight(
            game.knights["R"].position[0], game.knights["R"].position[1]), game.knights["R"])

    def test_item_moved_with(self):
        game = Game()
        game._Game__move_knight(game.knights["R"], DIRECTION.S)
        game._Game__move_knight(game.knights["R"], DIRECTION.S)
        game._Game__move_knight(game.knights["R"], DIRECTION.E)
        self.assertFalse(game.items["A"].is_equiped)
        game._Game__move_knight(game.knights["R"], DIRECTION.E)
        self.assertEqual(game.knights["R"].position, (2, 2))
        self.assertEqual(game.knights["R"].item, game.items["A"])
        self.assertTrue(game.items["A"].is_equiped)
