
from human import Human
from ai import AI
from time import sleep


human_one = Human()
human_two = Human()
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

    def human_game(self):
        print('')
        self.determine_human_winner()
    
    def determine_ai_winner(self):
        human_one.human_choice()
        ai.ai_choice()
        if ai.choice == human_one.choice:
            print('Tie! Try again')
            self.determine_ai_winner()
        elif human_one.choice == 'Rock' and (ai.choice == 'Scissors' or ai.choice == 'Lizard'):
            print("Human wins.")
            human_one.score += 1
            self.test_ai_winner()
        elif human_one.choice == 'Paper' and (ai.choice == 'Rock' or ai.choice == 'Spock'):
            print("Human wins.")
            human_one.score += 1
            self.test_ai_winner()
        elif human_one.choice == 'Scissors' and (ai.choice == 'Paper' or ai.choice == 'Lizard'):
            print("Human wins.")
            human_one.score += 1
            self.test_ai_winner()
        elif human_one.choice == 'Lizard' and (ai.choice == 'Paper' or ai.choice == 'Spock'):
            print("Human wins.")
            human_one.score += 1
            self.test_ai_winner()
        elif human_one.choice == 'Spock' and (ai.choice == 'Rock' or ai.choice == 'Scissors'):
            print("Human wins.")
            human_one.score += 1
            self.test_ai_winner()
        else:
            ai.score += 1
            print("AI wins.")
            self.test_ai_winner()

    def determine_human_winner(self):
        human_one.human_choice()
        human_two.human_choice()
        if human_one.choice == human_two.choice:
            print('Tie! Try again')
            self.determine_human_winner()
        elif human_one.choice == 'Rock' and (human_two.choice == 'Scissors' or human_two.choice == 'Lizard'):
            print("Human One wins.")
            human_one.score += 1
            self.test_human_winner()
        elif human_one.choice == 'Paper' and (human_two.choice == 'Rock' or human_two.choice == 'Spock'):
            print("Human One wins.")
            human_one.score += 1
            self.test_human_winner()
        elif human_one.choice == 'Scissors' and (human_two.choice == 'Paper' or human_two.choice == 'Lizard'):
            print("Human One wins.")
            human_one.score += 1
            self.test_human_winner()
        elif human_one.choice == 'Lizard' and (human_two.choice == 'Paper' or human_two.choice == 'Spock'):
            print("Human One wins.")
            human_one.score += 1
            self.test_human_winner()
        elif human_one.choice == 'Spock' and (human_two.choice == 'Rock' or human_two.choice == 'Scissors'):
            print("Human One wins.")
            human_one.score += 1
            self.test_human_winner()
        else:
            human_two.score += 1
            print("Human Two wins.")
            self.test_human_winner()


    def test_ai_winner(self):
        if human_one.score == 2:
            print('Human wins the game!')
            return
        elif ai.score == 2:
            print('AI wins the game!')
            return
        if human_one.score == 1:
            print('You almost got this!')
            self.determine_ai_winner()
        elif ai.score == 1:
            print('You almost got this!')
            self.determine_ai_winner()

    def test_human_winner(self):
        if human_one.score == 2:
            print('Human One wins the game!')
            return
        elif human_two.score == 2:
            print('Human Two wins the game!')
            return
        if human_one.score == 1:
            print('You almost got this!')
            self.determine_human_winner()
        elif human_two.score == 1:
            print('You almost got this!')
            self.determine_human_winner()

