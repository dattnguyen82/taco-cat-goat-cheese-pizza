import random
from function_timer import function_timer


class Game:
    cards = ['TACO', 'CAT', 'GOAT', 'CHEESE', 'PIZZA', 'BOMB']
    disarm = 'DISARM!'
    bomb_timer = 3

    def __init__(self, player):

        if player is None:
            raise Exception('Player cannot be null')

        self.current = -1
        self.current_player = player
        self.current_card = None

    def __validate_input(self, user_input, elapsed):
        if self.current_card == 'BOMB':
            return user_input.upper() == self.disarm and elapsed < self.bomb_timer
        return user_input.upper() == self.cards[self.current]

    @function_timer
    def __user_input(self, prompt):
        return input(f'{prompt}: ')

    def __get_card(self):
        self.current_card = random.choice(self.cards)
        self.current = (self.current + 1) % (len(self.cards) - 1)  # cycle through the card sequence but skip BOMB
        return self.current_card

    def __print_end_game(self):
        print('!!!!!!!!!!!!!!!!! GAME OVER !!!!!!!!!!!!!')
        self.current_player.print_player_stats()

    def run(self):
        while True:
            card = self.__get_card()
            user_input, elapsed = self.__user_input(card)
            if not self.__validate_input(user_input, elapsed):
                self.__print_end_game()
                break
            self.current_player.increment_score()
