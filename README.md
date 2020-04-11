# Blackjack-for-Python
Blackjack repository
Lets hope this README works. It's my first time doing any of this. Except programming. I have a little experience in programming. 

This project is a blackjack game on python. It follows the same basic rules of the game. 
The user faces the program in the game.

The "bot" that the user is against will only hit if it has a low enough value of cards, and will only stay if it has a high enough value. 
The bot can bust, and the bot can stay. 
It is a one player game (might work on making it two player or best out of 5, not sure yet)

Feel free to give constructive criticism and/or edit/add to the design!

Main framework for the game credits to "techbytes.io" Link: https://www.youtube.com/watch?v=yJz2at4Hco4&t=784s
Changes I have made: Bug fixes. Lots of bug fixes. Also added a small disclaimer and rule at the beginning of each game. Working on a restart option so that the player can restart in the middle of a game if they want, instead of throwing the game to start another one. 
 

Bugs Fixed:

The player can continue to play even though they have lost (Now, they cannot)

The bot will only hit if the player hits, and will only stay if the player stays (Now, it should hit if it has less than 16, and stay if it has more than 16)

If the bot busts, it will win, as long as the player has less than the bot even if the player did not bust (Now, if the bot busts, it will automatically lose, and if the player busts, the player will also lose.)


Bugs that need to be fixed:

If both the player and the bot bust, it says that the player busts, and the bot has one; then under that it says that the bot busts and the player has won; and at the bottom it says that both have busted and it is a tie. 
