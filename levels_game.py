from games.hangman.hangman import game_start
from games.tictactoe.tictactoe import GameStart
from games.hotncold.hotncold import HotCold


class LevelGameStart:
    def __init__(self, option):
        self.option = option
        self.tictactoe = GameStart()
        self.hot_cold = Hot_Cold()
        self.result = False
        self.score = 0

    def load_game(self):
        if self.option == '2':
            hot_cold = HotCold()
            result = self.hot_cold.win
            if result:
                self.option = str(int(self.option) + 1)
                self.score += 50
        if self.option == '3':
            tictactoe.run()
            result = self.tictactoe.win
            if result:
                self.option = str(int(self.option) + 1)
                self.score += 50
        if self.option == '4':
            result = game_start(False)
            if result:
                self.option = str(int(self.option) + 1)
                self.score += 50


def main(option):
    start = LevelGameStart(option)
    return start.load_game()
