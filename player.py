class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0

    def increment_score(self):
        self.score += 1

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def print_player_stats(self):
        print('===============GAME STATS================')
        print(f'Player: {self.get_name()}')
        print(f'Score: {self.get_score()}')
        print('=========================================')