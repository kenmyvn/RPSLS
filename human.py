
from player import Player
from time import sleep

class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name


    def human_choice(self):
        self.human_choice = (input('Please select Rock, Paper, Scissors, Lizard, or Spock: '))
        sleep(1)
        print(f'(self.name) has chosen {self.human_choice}')
    