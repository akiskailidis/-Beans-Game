# Beans-Game

A multiplayer terminal-based game where players put or take beans from a shared pot based on randomly chosen actions. The last remaining player with beans wins!

## Project Overview

This is a Python-based implementation of the classic "Beans on the Table" game. Each player starts with a certain number of beans. During the game, players take turns spinning a wheel (random choice) that decides whether they put beans into the pot or take some out. Players are eliminated when they run out of beans. The game continues until one player remains.

## Game Rules

- At the start of each round, all active players contribute 1 bean to the pot.
- On each turn, a player randomly "spins" one of the following actions:

'Put One', 'Put Two', 'Put them all',
'Take One', 'Take Two', 'Take them all'


- Players are eliminated when they have zero beans.
- The last remaining player with beans is declared the winner.

## Features

- Terminal-based input/output
- Multiple players (minimum 2)
- Random action selection per turn
- Automatic elimination of players with zero beans
- Final winner announcement

## How to Run

1. Clone or download this repository.
2. Run the game using Python 3:

```bash
python beans_game.py
Follow the prompts:

Enter number of players

Enter starting number of beans per player

Enter number of players (>=2): 3
Enter initial number of beans per player: 5
Player 2 starts first.

--- Round 1 ---
Each player contributes 1 bean to the pot.

Pot: 3
Player 1 beans: 4
Player 2 beans: 4
Player 3 beans: 4
Player 2 spins: Put Two

...

Game Over! Player 3 wins with 2 beans.

