import argparse
from datetime import datetime
import random

__version__ = '1.0.1'
__author__ = 'mrwolferinc'
__license__ = 'MIT'

def run_simulation(rounds, swap=True):
    """Run a simulation of the Monty Hall problem.

    :param rounds: The number of rounds to be played. Must be greater than 0 or else a ValueError will be raised.
    :type rounds: int
    :param swap: Determines if the player swaps doors or not. Defaults to True.
    :type swap: bool
    """
    if rounds > 0:
        wins = 0
        random.seed()
        for i in range(rounds):
            # Generate random door contents
            doors = ['goat', 'goat', 'car']
            random.shuffle(doors)

            # Pick a door
            door_choice = random.randrange(len(doors))
            print(f'Selecting door {door_choice + 1}...')

            # Show a door with a goat
            for j, contents in enumerate(doors):
                if j != door_choice and contents == 'goat':
                    goat_door = j
                    print(f'The host reveals a goat behind door {goat_door + 1}.')
                    break
            
            if swap:
                # Swap to the other door
                for j in range(len(doors)):
                    if j != door_choice and j != goat_door:
                        swap_to = j
                        print(f'Swapping to door {swap_to + 1}...')
            else:
                swap_to = door_choice
            
            if doors[swap_to] == 'car':
                wins += 1
                print('YOU WON THE CAR!!!\n')
            else:
                print('Sorry, but you\'re stuck with a goat.\n')
        
        if rounds > 1:
            if wins == rounds:
                print('You played', rounds, 'rounds, and won all of them!')
            elif wins < 1:
                print('You played', rounds, 'rounds, and didn\'t win any of them.')
            else:
                print('You played', rounds, 'rounds, and won', wins, 'of them!')
        elif rounds == 1:
            if wins > 0:
                print('You played a round and won!')
            else:
                print('You played a round and lost.')
    else:
        raise ValueError('"rounds" must be greater than 0')

def run():
    """Module entry point."""
    now = datetime.now()

    # Parse arguments
    parser = argparse.ArgumentParser(prog='montyhallsim', description=f'montyhallsim v{__version__}\n(c) {now.year} {__author__}. All rights reserved.', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-r', '--rounds', nargs='?', type=int, default=10, help='Set the number of rounds to be played - defaults to 10.')
    parser.add_argument('-n', '--no-swap', action='store_true', help='Run a simulation without swapping doors.')
    parser.add_argument('--version', action='store_true', help='Print the version - does not run the simulation.')

    args = parser.parse_args()
    # If the user asked for the version, print it, otherwise run the simulation
    if args.version:
        print(f'montyhallsim v{__version__}')
    else:
        try:
            if args.no_swap:
                run_simulation(args.rounds, False)
            else:
                run_simulation(args.rounds)
        except Exception as e:
            if e.message == '"rounds" must be greater than 0':
                print(f'{type(e).__name__}: --rounds must be greater than 0')
            else:
                print(f'{type(e).__name__}: {e.message}')

if __name__ == '__main__':
    run()
