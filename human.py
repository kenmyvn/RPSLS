
from player import Player
from time import sleep

class Human(Player):
    def __init__(self):
        super().__init__()


    def human_choice(self):
        n = int(input('Please select 1 for Rock, 2 for Paper, 3 for Scissors, 4 for Lizard, or 5 for Spock: '))
        self.choice = self.list[n-1]
        sleep(1)
        print(f"Human has chosen {self.choice}")