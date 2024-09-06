import unittest
from rps_main import round_winner_testing_gui

#Κλάση Testing
class TestClass(unittest.TestCase):
    #Test για ισοπαλία
    def test_tie(self):
        self.assertEqual(round_winner_testing_gui("R","R"), "Tie")
        self.assertEqual(round_winner_testing_gui("P","P"), "Tie")
        self.assertEqual(round_winner_testing_gui("S","S"), "Tie")
    
    #Test για νίκη παίκτη
    def test_player_win(self):
        self.assertEqual(round_winner_testing_gui("R","S"), "Player wins")
        self.assertEqual(round_winner_testing_gui("P","R"), "Player wins")
        self.assertEqual(round_winner_testing_gui("S","P"), "Player wins")

    #Test για νίκη υπολογιστή
    def test_computer_wins(self):
        self.assertEqual(round_winner_testing_gui("R","P"), "Computer wins")
        self.assertEqual(round_winner_testing_gui("P","S"), "Computer wins")
        self.assertEqual(round_winner_testing_gui("S","R"), "Computer wins")

unittest.main(argv=[""], verbosity=2, exit=False)
