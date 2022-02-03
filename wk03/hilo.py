import random, sys

class Player:
    def __init__(self):
        self.high_low = 'yes'
        self.score = 300
    def get_inputs(self):
        self.high_low = input('Higher or lower? [h/l] ') 
    def add_100(self):
        self.score += 100
    def loss_75(self):
        self.score -= 75
    def get_score(self):
        return self.score
   
class Dealer:
    def __init__(self):
        self.is_playing = True
        self.new_card = Card()
        self.player = Player()
        self.card = 0
        
    def play_game(self):
        while self.is_playing:
            self.get_card()
            self.player.get_inputs()
            print(f'The new card: {self.new_card.value}')
            self.compare()
            if  self.player.score <= 0:
                print('you lose')
                sys.exit()
            continue_play = input('Do you want to keep playing? (y/n):')
            print()
            if continue_play == 'n':
                self.is_playing = False
            
    def get_card(self):
        self.card = self.new_card
        self.new_card = Card()
        while self.new_card.value == self.card.value:
                self.new_card = Card()
        print(f'The old card: {self.card.value}')

    def compare(self):
        result = self.new_card.value > self.card.value
        if (result is True and self.player.high_low == 'h') or (result is not True and self.player.high_low != 'h'):
            self.player.add_100()
        else:
            self.player.loss_75()
        print(f'Your score is {self.player.score}')
    
class Card():
    def __init__(self):
        self.value = random.randint(1, 13)

def main():
    dealer = Dealer()
    dealer.play_game()

main()
