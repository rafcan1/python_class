'''
Midterm Programming Task, file mpt_01.py, 25 points
Double Six Dice Game
On the basis of: https://www.101computing.net/double-six-dice-game/

-- do not register in order to check the solution !!!!

In this challenge, your task is to create a 2-player dice game with the following rules:
- Each player has a pair of dice
- The first player rolls a pair of dice, and keeps rolling the dice again and again, until they roll a double six.
- It is then the turn of the the second player. They too will roll the dice and keep doing so until they roll a double six.
- The winner of the game is the user who rolled a double six in the smaller number of attempts.
- The game ends on a draw if both players used the same number of attempts to roll a double six.

In order to solve the task you have to implement 2 functions as below:

def get_roll_counter() -> int
def print_game_results(name1: str, counter1: int, name2: str, counter2: int) -> None

and use random number generator : random.randint(start,stop) function.

Details you can find on
https://www.w3schools.com/python/ref_random_randint.asp
https://www.geeksforgeeks.org/python-randint-function/

Exemplary result:

__________________________
|                          |
|   Double Six Dice Game   |
|__________________________|


Enter the name of player 1 ... John
Enter the name of player 2 ... Mark
==========
Player Mark won, with 25 double dice rolls!!!
Player John had, 175 attempts

'''


def get_roll_counter() -> int:
    '''
    Function rolls a pair of dice, and keeps rolling the dice again and again, until they roll a double six

    Returns:
        number of rolling attempts
    '''
    import random
    attempt = 0

    while True:
        roll_1 = random.randint(1, 6)
        roll_2 = random.randint(1, 6)
        attempt += 1
        if roll_1 == 6 and roll_2 == 6:
            return attempt


def print_game_results(name1: str, counter1: int, name2: str, counter2: int) -> None:
    '''
    Function prints the results of 'Double Six Dice Game' for 2 players

    Parameters:
        name1: name of the first player
        counter1: number of attempts of the first player until get DoubleSix    
        name2: name of the first player
        counter2: number of attempts of the first player until get DoubleSix
    Returns:
        None
    '''
    name1 = input("Enter the name of player 1...")
    name2 = input("Enter the name of player 2...")
    counter1 = get_roll_counter()
    counter2 = get_roll_counter()
    if counter2 == counter1:
        print(f'It is a draw!')
    elif counter1 < counter2:
        print(f'Player {name1} won, with {counter1} dice rolls!!!')
        print(f'Player {name2} had, {counter2} attempts')
    else:
        print(f'Player {name2} won, with {counter2} dice rolls!!!')
        print(f'Player {name1} had, {counter1} attempts')
    return None
# After implementing your functions continue the code here below:


def header():
    print("_" * 30)
    print("|" + " " * 28 + "|")
    print("|" + "   Double Six Dice Game     " + "|")
    print("|" + "_"*28 + "|")
    return None


header()
print(print_game_results("name1", "number1", "name2", "number2"))
