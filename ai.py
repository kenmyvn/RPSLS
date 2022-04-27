
from player import Player
import random
from time import sleep

class AI(Player):
    def __init__(self):
        super().__init__()


    def ai_choice(self):
        n = random.randint(0,4)
        self.choice = self.list[n]
        sleep(1)
        print(f"AI has chosen {self.choice}")
