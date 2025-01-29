# Maxime SENARD
# 01/27/2025
# A program that allows the user to play the game Three Card Monte, where a player bets that they can guess the location of the queen in a set of three cards.

import check_input
import random

BALANCE = 100
NUM_CARDS = 3

RESET = "\033[0m"
BOLD = "\033[1m"


def draw_greeting():
    """Draw a greeting message."""
    txt = """  _______   _                               _____                      _     __  __                   _          
 |__   __| | |                             / ____|                    | |   |  \\/  |                 | |         
    | |    | |__    _ __    ___    ___    | |        __ _   _ __    __| |   | \\  / |   ___    _ __   | |_    ___ 
    | |    | '_ \\  | '__|  / _ \\  / _ \\   | |       / _` | | '__|  / _` |   | |\\/| |  / _ \\  | '_ \\  | __|  / _ \\
    | |    | | | | | |    |  __/ |  __/   | |____  | (_| | | |    | (_| |   | |  | | | (_) | | | | | | |_  |  __/
    |_|    |_| |_| |_|     \\___|  \\___|    \\_____|  \\__,_| |_|     \\__,_|   |_|  |_|  \\___/  |_| |_|  \\__|  \\___|
    """
    print(txt)
    print(f"{BOLD}Find the queen to double your bet!{RESET}")


def draw_cards(cards: list[str] | list[int]):
    """Draw the cards on the screen.
    Args:
        cards (list[str] | list[int]): List of cards to draw.\n
        - if the card is a string, only the first character will be drawn.
        - If the card is an integer, it will be converted to a string and only the first digit will be show.
    """
    cards = [str(card)[0] for card in cards]
    txt = ("+-----+ " * len(cards))[:-1] + "\n"
    txt += ("|     | " * len(cards))[:-1] + "\n"
    txt += " ".join([f"|  {BOLD}{card}{RESET}  |" for card in cards]) + "\n"
    txt += ("|     | " * len(cards))[:-1] + "\n"
    txt += ("+-----+ " * len(cards))[:-1] + "\n"
    print(txt, end="")


def main():
    draw_greeting()

    balance: int = BALANCE
    while True:
        print(f"You have ${balance}")
        bet = check_input.get_int_range("How much you wanna bet? ", 1, balance)
        draw_cards(range(1, NUM_CARDS + 1))
        queen = random.randint(1, NUM_CARDS)
        guess = check_input.get_int_range("Find the queen: ", 1, NUM_CARDS)
        draw_cards(["K" if i != queen else "Q" for i in range(1, NUM_CARDS + 1)])
        if guess == queen:
            balance += bet
            print(f"You got lucky this time...")
        else:
            balance -= bet
            print(f"Sorry... you lose.")
        if balance <= 0:
            print("You're out of money. Beat it loser!")
            break
        if not check_input.get_yes_no("Play again? (Y/N): "):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
