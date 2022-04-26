
from player import Player
import random
from time import sleep

class AI(Player):
    def __init__(self):
        super().__init__()
        self.score = 0

    def ai_choice(self):
        self.choice = random.choice(self.choices)
        sleep(1)
        print(f'AI has chosen {self.choice}')