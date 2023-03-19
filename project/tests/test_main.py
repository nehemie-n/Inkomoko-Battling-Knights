import unittest
from src.game import Game, KNIGHT_COLOR, ITEM_NAME, KNIGHT_STATUS

import json


class TestMain(unittest.TestCase):

    def test_parse_moves(self):
        game = Game(file_path="moves_test.txt")
        # Does it parse moves perfectly
        moves = game._Game__parse_moves()
        moves_len = len(moves)
        self.assertEqual(moves_len, 9)

    def test_play(self):
        game = Game(file_path="moves_test2.txt")
        game.play()
        self.assertEqual(game.state["red"][0], str([7, 0]))
        self.assertEqual(str(game.state["red"][1]), 'LIVE')
        self.assertEqual(game.state["red"][2], 'ITEM_NAME.'+ITEM_NAME.A._name_)
        # self.assertEqual(game.state["red"][3], 3)
        self.assertEqual(game.state["red"][4], 1)
        # game.state["red"][] = [7, 0], "LIVE", "Axe", 3, 1

    def test_play_result(self):
        game = Game()
        game.play()
        with open('final_state.json') as json_file:
            output = json.load(json_file)
            # red is live
            red = output["red"]
            self.assertEqual(red[1], "LIVE")
            # yellow drowned
            yellow = output["yellow"]
            self.assertEqual(yellow[1], "DROWNED")
            self.assertEqual(yellow[0], None)
            self.assertEqual(yellow[3], 0)
            self.assertEqual(yellow[4], 0)
            #
            self.assertIsNotNone(output)


if __name__ == '__main__':
    unittest.main()
