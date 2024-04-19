import random
play_again = ''
print('***ROCK PAPER SCISSORS***')
print('Conditions to WIN in the game are :\n'
        + 'Rock vs Paper -> Paper WINS \n'
        + 'Rock vs Scissors -> Rock WINS \n'
        + 'Paper vs Scissors -> Scissors WINS')

def rock_paper_scissors():
    print('Enter your choice:')
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    print('rock,paper,scissors')
    user_choice = input()
    user_choice = user_choice.lower()
    print('\nYour choice:', user_choice) 
    print('Computer is choosing...')
    print('Computer choice:', computer_choice)
    if user_choice == computer_choice:
        print('It is a tie!\n')
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print('Computer WINS!\n')
        else:
            print('You WIN!\n')
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            print('Computer WINS!\n')
        else:
            print('You WIN!\n')
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print('Computer WINS!\n')
        else:
            print('You WIN!\n')
    else:
        print('Invalid choice!\n')
    print('Do you want to play again? (yes or no)')
    play_again = input()
    response = play_again.lower()
    if response == 'no':
        print('\nThank you for playing!')
    else:
        print('\nWelcome back to the game!')
        rock_paper_scissors()
rock_paper_scissors()
