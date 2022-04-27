
from human import Human
from ai import AI
from time import sleep

class Game:
    def __init__(self):
        return
    
    def run_game(self):
        print('Welcome to RPSLS!')
        sleep(0.5)
        print('')
        print('This is a best two out of three.')
        print('May the best player win.')
        print('')
        print('Rock crushes Scissors')
        sleep(0.5)
        print('Paper covers Rock')
        sleep(0.5)
        print('Rock crushes Lizard')
        sleep(0.5)
        print('Lizard poisons Spock')
        sleep(0.5)
        print('Spock smashes Scissors')
        sleep(0.5)
        print('Scissors decapitates Lizard')
        sleep(0.5)
        print('Lizard eats Paper')
        sleep(0.5)
        print('Paper disproves Spock')
        sleep(0.5)
        print('Spock vaporizes Rock')
        print('')
        print('Press 1 for Human vs. AI, press 2 for Human vs. Human: ')
        self.answer = int(input())
        self.human_or_ai()

    def human_or_ai(self):
        if self.answer == 1:
            self.ai_game()
        elif self.answer == 2:
            self.human_game()
        elif self.answer != 1 or 2:
            print("Please start over.")
            self.run_game()

    def ai_game(self):
        print('')
        self.determine_ai_winner()
    
    def determine_ai_winner(self):
        human = Human()
        human.human_choice()
        ai = AI()
        ai.ai_choice()
        if ai.choice == human.choice:
            print('Tie! Try again')
            self.determine_ai_winner()
        else:
            print('testing')
            self.determine_ai_winner()
    
# when coming back to this! hello wednesday kendall. you have numbers now. make sure to loop a score so that it adds and when it gets to 2, break.
# configure ai vs human and then rework that into human vs human