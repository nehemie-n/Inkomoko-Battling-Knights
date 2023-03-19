import unittest
from src.game import Game

import json


class TestMain(unittest.TestCase):

    def test_parse_moves(self):
        game = Game(file_path="moves_test.txt")
        # Does it parse moves perfectly
        moves = game._Game__parse_moves()
        moves_len = len(moves)
        self.assertEqual(moves_len, 9)

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
