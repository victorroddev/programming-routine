import unittest

from ghostgoobble import eat_ghost, score, loser, win

class TestEatGhost(unittest.TestCase):

    def test1(self):
        self.assertEqual(eat_ghost(False, False), False)
        self.assertEqual(eat_ghost(True, True), True)
        self.assertEqual(eat_ghost(False, True), False)

class TestScore(unittest.TestCase):
    def test1(self):
        self.assertEqual(score(False,False), False)
        self.assertEqual(score(True, True), True)
        self.assertEqual(score(True, False), True)
        self.assertEqual(score(False, True), True)

class TestLoser(unittest.TestCase):
    def test1(self):
        self.assertEqual(loser(False, True), True)
        self.assertEqual(loser(True, True), False)
        self.assertEqual(loser(False, False), False)
        self.assertEqual(loser(True, False), False)

class TestWin(unittest.TestCase):
    def test1(self):
        
        self.assertEqual(win(True, True, False ), True)
        self.assertEqual(win(True, True, True), True)
        self.assertEqual(win(True, False, True), False)
        self.assertEqual(win(False, False, False), False)
        self.assertEqual(win(False, True, True), False)
        self.assertEqual(win(False, False, True),False)
        self.assertEqual(win(False,True, False), False)

unittest.main()
