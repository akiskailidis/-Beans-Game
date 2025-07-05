
import random
from typing import Dict

def initialize_game() -> (int, int, Dict[int, int]): # type: ignore
    while True:
        players = int(input('Enter number of players (>=2): '))
        if players >= 2:
            break
        print('Please enter 2 or more players.')

    beans = int(input('Enter initial number of beans per player: '))
    budgets = {i: beans for i in range(1, players + 1)}
    return players, beans, budgets

def print_status(pot: int, budgets: Dict[int, int]):
    print(f"\nPot: {pot}")
    for pid, beans in budgets.items():
        if beans > 0:
            print(f"Player {pid} beans: {beans}")
        else:
            print(f"Player {pid} is eliminated.")

def player_spin(pot: int, player_id: int, budgets: Dict[int, int], options: list) -> int:
    choice = random.choice(options)
    print(f"Player {player_id} spins: {choice}")

    if choice == 'Put One':
        if budgets[player_id] > 0:
            budgets[player_id] -= 1
            pot += 1
    elif choice == 'Put Two':
        to_put = min(2, budgets[player_id])
        budgets[player_id] -= to_put
        pot += to_put
    elif choice == 'Put them all':
        pot += budgets[player_id]
        budgets[player_id] = 0
    elif choice == 'Take One':
        if pot >= 1:
            budgets[player_id] += 1
            pot -= 1
    elif choice == 'Take Two':
        to_take = min(2, pot)
        budgets[player_id] += to_take
        pot -= to_take
    elif choice == 'Take them all':
        budgets[player_id] += pot
        pot = 0
    return pot

def play_game():
    pot = 0
    options = ['Put One', 'Put Two', 'Put them all', 'Take One', 'Take Two', 'Take them all']
    players, initial_beans, budgets = initialize_game()

    active_players = players
    round_count = 0
    current_player = random.randint(1, players)
    print(f"Player {current_player} starts first.\n")

    while active_players > 1:
        round_count += 1
        print(f"\n--- Round {round_count} ---")
        print("Each player contributes 1 bean to the pot.")

        for pid in budgets:
            if budgets[pid] > 0:
                budgets[pid] -= 1
                pot += 1

        while pot > 0 and active_players > 1:
            print_status(pot, budgets)

            if budgets[current_player] == 0:
                current_player = (current_player % players) + 1
                continue

            pot = player_spin(pot, current_player, budgets, options)

            if budgets[current_player] == 0:
                active_players -= 1

            current_player = (current_player % players) + 1

    for pid, beans in budgets.items():
        if beans > 0:
            print(f"\nGame Over! Player {pid} wins with {beans} beans.")
            break

if __name__ == "__main__":
    play_game()
