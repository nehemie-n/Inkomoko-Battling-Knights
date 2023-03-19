import unittest
from src.game import Knight, KNIGHT_COLOR, KNIGHT_STATUS


class TestKnight(unittest.TestCase):

    def test_islive(self):
        knight = Knight(KNIGHT_COLOR.R, (0, 0))
        self.assertTrue(knight.is_alive())
        knight.status = KNIGHT_STATUS.DEAD
        self.assertFalse(knight.is_alive())
        knight.status = KNIGHT_STATUS.DROWNED
        self.assertFalse(knight.is_alive())

    def test_drawn(self):
        knight = Knight(KNIGHT_COLOR.R, (0, 0))
        knight.drawn()
        self.assertEqual(knight.status, KNIGHT_STATUS.DROWNED)
        self.assertFalse(knight.is_alive())

    def test_dead(self):
        knight = Knight(KNIGHT_COLOR.R, (0, 0))
        knight.dead()
        self.assertEqual(knight.status, KNIGHT_STATUS.DEAD)
        self.assertFalse(knight.is_alive())
