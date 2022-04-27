
from human import Human
from ai import AI
from time import sleep


human = Human()
ai = AI()


class Game:
    def __init__(self):
        self.score = 0

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
        human.human_choice()
        ai.ai_choice()
        if ai.choice == human.choice:
            print('Tie! Try again')
            self.determine_ai_winner()
        elif human.choice == 1 and ai.choice == 3 or ai.choice == 4:
            print("Human wins.")
            human.score + 1
            self.test_winner()
        elif human.choice == 2 and ai.choice == 1 or ai.choice == 5:
            print("Human wins.")
            human.score + 1
            self.test_winner()
        elif human.choice == 3 and ai.choice == 2 or ai.choice == 4:
            print("Human wins.")
            human.score + 1
            self.test_winner()
        elif human.choice == 4 and ai.choice == 2 or ai.choice == 5:
            print("Human wins.")
            human.score + 1
            self.test_winner()
        elif human.choice == 5 and ai.choice == 1 or ai.choice == 3:
            print("Human wins.")
            human.score + 1
            self.test_winner()
        else:
            ai.score + 1
            print("AI wins.")
            self.test_winner()
        # else:
        #     print('Type a proper number! Start over now~~')
        #     self.determine_ai_winner()

    def test_winner(self):
        if human.choice == 2:
            print('Human wins!')
            return
        if ai.choice == 2:
            print('AI wins!')
            return




    
# when coming back to this! hello wednesday kendall. you have numbers now. make sure to loop a score so that it adds and when it gets to 2, break.
# configure ai vs human and then rework that into human vs human