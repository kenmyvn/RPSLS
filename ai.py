
from player import Player
import random
from time import sleep

class AI(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def ai_choice(self):
        self.ai_choice = random.choice(self.choices)
        sleep(1)
        print(f'(self.name) has chosen {self.ai_choice}')