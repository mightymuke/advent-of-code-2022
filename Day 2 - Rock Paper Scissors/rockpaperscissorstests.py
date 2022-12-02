import unittest
from rockpaperscissors import RockPaperScissors

class RockPaperScissorsTests(unittest.TestCase):

    def test_stategy_one_with_example_playbook(self):
        playbook = [
            'A Y',
            'B X',
            'C Z'
        ]

        rps = RockPaperScissors()
        rps.load(playbook)

        self.assertEqual(rps.playStrategyOne()[1], 15)

    def test_stategy_one_using_provided_input_file(self):
        f = open("input.txt", "r")
        playbook = f.readlines()
        f.close()

        rps = RockPaperScissors()
        rps.load(playbook)

        self.assertEqual(rps.playStrategyOne(), [9226, 15632])

    def test_stategy_two_with_example_playbook(self):
        playbook = [
            'A Y',
            'B X',
            'C Z'
        ]

        rps = RockPaperScissors()
        rps.load(playbook)

        self.assertEqual(rps.playStrategyTwo()[1], 12)

    def test_stategy_two_using_provided_input_file(self):
        f = open("input.txt", "r")
        playbook = f.readlines()
        f.close()

        rps = RockPaperScissors()
        rps.load(playbook)

        self.assertEqual(rps.playStrategyTwo(), [9310, 14416])

if __name__ == '__main__':
    unittest.main()