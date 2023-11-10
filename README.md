# Wordle

## About the project
This was an assignment for my `COMP202 - Foundations of Programming` class. Wordle is a simple word game where the user has 6 guesses to guess a five letter word. 
In the original game, the user can only play once a day, since a five letter word is only generated once a day.
In the context of this project, the user can play how many times they want, as a five letter word will be randomly generated from the wordle database for each game.
Additionally, in this context, there can be 2 players whereas the original Wordle is a single player game.

Here is how the game works (1P):
- Each guess will be printed in the shell
- The shell will highlight each letter with one of the following colors: grey, yellow and green
- `Grey`: This letter is not in the word
- `Yellow`: This letter is in the word but in the incorrect place
- `Green`: This letter is in the word and in the correct place

Here is how the game works (2P):
-   Player1 chooses a five letter word and writes it to the shell, after 2 seconds the word will disappear from the shell
-   Player2 must guess the word in 6 tries
-   The same gameplay as 1P applies afterwards

## How to run the game locally

Each function contains docstrings to facilitate understanding.

Run the function `main`
- Enter the number of players in the shell
- Have fun!
