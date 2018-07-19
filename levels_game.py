from games.hangman.hangman import game_start


class LevelGameStart:
    def __init__(self, option):
        self.option = option

    def load_game(self):
        if self.option == '2':
            level1game = hot_cold.Start()
            result, score = level1game.run()
            if result:
                self.option = str(int(self.option) + 1)
            return result, score
        if self.option == '3':
            level2game = tic_tac_toe.Start()
            result, score = level2game.run()
            if result:
                self.option = str(int(self.option) + 1)
            return result, score
        if self.option == '4':
            result, score = game_start(False)
            if result:
                self.option = str(int(self.option) + 1)
            return result, score


def main(option):
    start = LevelGameStart(option)
    return start.load_game()