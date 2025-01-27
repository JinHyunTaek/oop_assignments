import check_input
import random

ci = check_input

def print_one_to_three():
    print('+-----+ +-----+ +-----+')
    print('|     | |     | |     |')
    print('|  1  | |  2  | |  3  |')
    print('|     | |     | |     |')
    print('+-----+ +-----+ +-----+')

def find_queen(bet,balance):
    my_choice = ci.get_int_range('Find the queen: ',1,3)
    rand = random.randint(1,3)
    print('+-----+ +-----+ +-----+')
    print('|     | |     | |     |')
    print(f'|  {'Q' if rand == 1 else 'K'}  | |  {'Q' if rand == 2 else 'K'}  | |  {'Q' if rand == 3 else 'K'}  |')
    print('|     | |     | |     |')
    print('+-----+ +-----+ +-----+')
    if my_choice == rand:
        print('You got lucky this time...')
        return bet + balance
    else:
        print('Sorry... you lose.')
        return balance - bet


def main():
    print('-Three Card Monte-')
    print('Find the queen to double your bet!\n')
    balance = 100
    while balance > 0:
        print(f'You have {balance}.')
        bet = ci.get_int_range('How much you wanna bet? ',1,balance)
        print_one_to_three()
        balance =  find_queen(bet,balance)
        if not balance:
            print('You\'re out of money. Beat it loser!')
            return
        is_continue = ci.get_yes_no('Play again? (Y/N): ')
        if not is_continue:
            return

main()