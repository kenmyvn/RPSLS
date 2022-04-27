
from player import Player
import random
from time import sleep

class AI(Player):
    def __init__(self):
        super().__init__()


    def ai_choice(self):
        self.choice = random.randint(1,5)
        sleep(1)
        if self.choice == 1:
            print("AI has chosen Rock")
        elif self.choice == 2:
            print("AI has chosen Paper")
        elif self.choice == 3:
            print("AI has chosen Scissors")
        elif self.choice == 4:
            print("AI has chosen Lizard")
        elif self.choice == 5:
            print("AI has chosen Spock")
        return self.choice