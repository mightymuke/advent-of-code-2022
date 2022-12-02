class RockPaperScissors:
    def __init__(self):
        self.player1 = 0
        self.player2 = 0
        self.playbook = []

    score_win = 6
    score_draw = 3
    score_loss = 0

    score_rock = 1
    score_paper = 2
    score_scissors = 3

    score_shape = {
        'A': score_rock,
        'X': score_rock,
        'B': score_paper,
        'Y': score_paper,
        'C': score_scissors,
        'Z': score_scissors
    }

    def load(self, playbook):
        self.playbook = []
        if len(playbook) < 1:
            return

        for round in playbook:
            self.playbook.append(round.strip().split())

    def playRockPaperScissors(self, round):
        # If same, its a draw
        if (round[0] == round[1]):
            return [self.score_draw, self.score_draw]

        # If mod 3 of player 1 is 1 behind player 2, player 1 loses
        if (round[0] % 3 == round[1] - 1):
            return [self.score_loss, self.score_win]

        return [self.score_win, self.score_loss]

    def playStrategyOne(self):
        self.player1 = 0
        self.player2 = 0

        if len(self.playbook) < 1:
            return [self.player1, self.player2]

        for round in self.playbook:
            # Get the game score
            results = self.playRockPaperScissors([self.score_shape[round[0]], self.score_shape[round[1]]])

            # Add scores
            self.player1 += results[0] + self.score_shape[round[0]]
            self.player2 += results[1] + self.score_shape[round[1]]

        return [self.player1, self.player2]

    def playStrategyTwo(self):
        self.player1 = 0
        self.player2 = 0

        if len(self.playbook) < 1:
            return [self.player1, self.player2]

        for round in self.playbook:
            player1ShapeScore = self.score_shape[round[0]]
            player2ShapeScore = self.score_shape[round[0]]

            match round[1]:
                case 'X': # Lose
                    player2ShapeScore = (self.score_shape[round[0]] + 1) % 3 + 1
                case 'Z': # Win
                    player2ShapeScore = self.score_shape[round[0]] % 3 + 1

            # Get the game score
            results = self.playRockPaperScissors([player1ShapeScore, player2ShapeScore])

            # Add scores
            self.player1 += results[0] + player1ShapeScore
            self.player2 += results[1] + player2ShapeScore

        return [self.player1, self.player2]
