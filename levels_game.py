from games.hangman.hangman import game_start
from games.tictactoe.tictactoe import GameStart
from games.hotncold.hotncold import HotCold


class LevelGameStart:
    def __init__(self, option):
        self.option = option
        self.tictactoe = GameStart()
        self.hot_cold = HotCold()
        self.result = False

    def load_game(self):
        if self.option == 1:
            self.hot_cold.run()
            self.result = self.hot_cold.win
        if self.option == 2:
            self.tictactoe.run()
            self.result = self.tictactoe.win
        if self.option == 3:
            self.result = game_start(False)
