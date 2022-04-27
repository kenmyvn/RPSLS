
from player import Player
from time import sleep

class Human(Player):
    def __init__(self):
        super().__init__()


    def human_choice(self):
        self.choice = int(input('Please select 1 for Rock, 2 for Paper, 3 for Scissors, 4 for Lizard, or 5 for Spock: '))
        sleep(1)
        if self.choice == 1:
            print("Human has chosen Rock")
        elif self.choice == 2:
            print("Human has chosen Paper")
        elif self.choice == 3:
            print("Human has chosen Scissors")
        elif self.choice == 4:
            print("Human has chosen Lizard")
        elif self.choice == 5:
            print("Human has chosen Spock")
        return self.choice