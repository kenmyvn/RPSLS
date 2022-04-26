
from player import Player
from time import sleep

class Human(Player):
    def __init__(self):
        super().__init__()
        self.score = 0


    def human_choice(self):
        self.choice = input('Please select Rock, Paper, Scissors, Lizard, or Spock: ')
        sleep(1)
        print(f'Human has chosen {self.choice}')
    